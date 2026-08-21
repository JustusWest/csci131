# Running the site locally (macOS)

`SETUP.md` covers creating and publishing the repo, and its local-preview step
assumes the Windows machine the site was originally scaffolded on. This is the
macOS version, start to finish.

Everything here is one-time setup except Step 6.

---

## What we are matching

GitHub builds this site with the `github-pages` gem, which pins the whole
toolchain for you:

| | Version |
|---|---|
| `github-pages` gem | 232 |
| Jekyll | 3.10.0 |
| Ruby | 3.3.x |

Any Ruby **3.3** works locally. GitHub itself uses 3.3.4; Homebrew ships 3.3.12.
The patch level does not matter — the minor version does.

Two things to avoid:

- **macOS's built-in Ruby.** It is old and system-owned. `gem install` into it
  wants `sudo` and then breaks in confusing ways later.
- **Ruby 3.4 or newer.** Ruby 3.4 moved `csv`, `base64`, and `logger` out of the
  default gems. Jekyll 3.10 does not declare them as dependencies, so it dies at
  startup with `cannot load such file -- csv`. Jekyll 4 fixed this, but the
  `github-pages` gem does not ship Jekyll 4 — so stay on 3.3 and the problem
  never comes up.

---

## Step 1 — Xcode Command Line Tools

```bash
xcode-select -p          # if this prints a path, skip to Step 2
xcode-select --install
```

Needed to compile the native gems (`nokogiri`, `ffi`, `http_parser.rb`).

## Step 2 — Homebrew

```bash
brew --version           # if this works, skip to Step 3
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

On Apple Silicon the installer finishes by printing two `eval` lines to add to
`~/.zprofile`. Run them, or `brew` will not be on your `PATH` in new terminals.

## Step 3 — Install Ruby 3.3 and chruby

```bash
brew install ruby@3.3 chruby
```

`ruby@3.3` is a **prebuilt bottle** — it downloads and it is done. Its `openssl`
and `psych` extensions are already built and working.

> **Why not `ruby-install`?** Building Ruby from source on macOS means pointing
> `configure` at Homebrew's OpenSSL and libyaml by hand, and when it fails to
> find them it does not stop — it finishes, reports success, and leaves you with
> a Ruby that cannot open an HTTPS connection or parse YAML. The failure only
> surfaces later as `Could not load OpenSSL` from `bundle install`. The bottle
> sidesteps that entire class of problem. See "If you would rather build from
> source" at the bottom if you need a specific patch level.

chruby does not look in Homebrew's cellar, so link the bottle into the place it
does look:

```bash
mkdir -p ~/.rubies
ln -s "$(brew --prefix ruby@3.3)" ~/.rubies/ruby-3.3
```

The link is deliberately named `ruby-3.3`, without a patch level, so Homebrew
can bump 3.3.12 → 3.3.13 underneath it without breaking anything.

## Step 4 — Wire chruby into zsh

```bash
echo 'source "$(brew --prefix)/opt/chruby/share/chruby/chruby.sh"' >> ~/.zshrc
echo 'source "$(brew --prefix)/opt/chruby/share/chruby/auto.sh"'   >> ~/.zshrc
echo 'chruby ruby-3.3'                                             >> ~/.zshrc
```

**Open a new terminal window** — not a new tab, which inherits the old `PATH` —
then confirm all four of these:

```bash
ruby -v        # ruby 3.3.x ... [arm64-darwin24]
which ruby     # /Users/michaelwest/.rubies/ruby-3.3/bin/ruby

# these must print a version, not raise LoadError
ruby -e "require 'openssl'; puts OpenSSL::OPENSSL_VERSION"
ruby -e "require 'psych'; puts Psych::VERSION"
```

Do not move on until all four pass. `which ruby` pointing at `/usr/bin/ruby` or
into `~/.rvm/` means chruby is not winning — see Troubleshooting.

The `auto.sh` line makes chruby switch based on a `.ruby-version` file. This
repo has one containing `3.3`, so `cd`-ing into it always selects the right Ruby
even if you install others later.

## Step 5 — Install the site's gems

```bash
cd ~/git-repos/courses/csci131
gem install bundler
bundle install
```

First run pulls about ninety gems and compiles a few of them — give it a few
minutes. `Gemfile.lock` is gitignored on purpose, since GitHub does the real
build; you never commit it.

## Step 6 — Serve the site

```bash
cd ~/git-repos/courses/csci131
bundle exec jekyll serve --livereload
```

Open **<http://localhost:4000/csci131/>**

The `/csci131/` is not optional — it is the `baseurl`, and it is part of the
local URL too. Plain `localhost:4000` will 404.

`Ctrl-C` stops the server.

## Step 7 — Check the lab pages

- <http://localhost:4000/csci131/labs/> — the index should list
  "Lab 1 — Input, Arithmetic, and Output" with its due date.
- <http://localhost:4000/csci131/labs/Lab1/> — should show the embedded handout
  PDF, then `fahrenheit.py`, `hello.py`, and `pay.py` inline as highlighted code,
  each with a download link.

---

## Day to day

| You changed | What to do |
|---|---|
| A `.md` page, a lecture, `assets/main.scss`, a lab file | Nothing — livereload refreshes the browser |
| `_config.yml` | Restart the server (`Ctrl-C`, then serve again) |
| `Gemfile` | `bundle install`, then restart |

Jekyll does not rebuild on `_config.yml` changes. If an edit there seems to do
nothing, that is why.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `Could not load OpenSSL. You must recompile Ruby with OpenSSL support.` from `bundle install` | A source-built Ruby whose `openssl` extension never compiled | Use the Homebrew bottle — Step 3 |
| `cannot load such file -- openssl` or `-- psych` | Same as above | Same as above |
| `cannot load such file -- csv` (or `base64`, `logger`) | You are on Ruby 3.4+ | Select 3.3: `chruby ruby-3.3` |
| `which ruby` points into `~/.rvm/` | RVM is installed and its wrappers are on `PATH` | See "RVM is in the way" below |
| `ruby -v` shows an old Ruby even though the chruby lines are in `~/.zshrc` | The shell started before `~/.rubies/ruby-3.3` existed, so `chruby` had nothing to select and quietly did nothing | Open a brand-new terminal window, not a tab |
| `gem install` asks for `sudo` / permission denied | You are on the system Ruby | chruby is not loading — recheck Step 4 in a fresh terminal |
| `Could not find gem 'github-pages'` | Gems not installed for this Ruby | `bundle install` from inside the repo |
| `bundler: command not found: jekyll` | Same as above, or wrong directory | `cd` into the repo, `bundle install` |
| `nokogiri` / `ffi` fails to build | Xcode Command Line Tools missing | Step 1 |
| `Address already in use` on port 4000 | An old server is still running | `bundle exec jekyll serve --port 4001`, or kill the old one |
| Everything 404s at `localhost:4000` | Missing the baseurl | Use `localhost:4000/csci131/` |
| A link works locally but 404s on GitHub | Hard-coded path | Route links through the `relative_url` filter rather than writing `/files/whatever.pdf` |
| Changes to a lab's files do not appear | New files in a watched directory sometimes need a restart | `Ctrl-C` and serve again |

### RVM is in the way

If `which ruby` points somewhere under `~/.rvm/`, an old RVM install is
shadowing chruby. RVM puts wrapper scripts in `~/.rvm/bin` and adds that
directory to `PATH` from your shell profile. When chruby succeeds it prepends
its own path and wins; any time chruby fails, RVM's wrappers are what is left.

Check what is loading it:

```bash
grep -n 'rvm\|chruby' ~/.zshrc ~/.zprofile ~/.zlogin ~/.bash_profile ~/.bashrc ~/.profile 2>/dev/null
```

RVM and chruby do not coexist gracefully. If nothing on the machine still needs
RVM, remove it:

```bash
[ -d ~/.rvm ] && rvm implode          # asks you to type "yes"
rm -rf ~/.rvm ~/.rvmrc
```

`rvm implode` does not touch your shell files, so strip its lines yourself.
Read the grep output first and confirm every match is RVM's — none of the
chruby lines contain the string `rvm`, so this is safe when it is:

```bash
for f in ~/.zshrc ~/.bash_profile ~/.profile; do
  [ -f "$f" ] || continue
  cp "$f" "$f.bak-rvm"
  sed -i '' '/rvm/d' "$f"
done
```

Backups land beside each file as `.bak-rvm`. Then open a brand-new terminal.

### If you would rather build from source

Only worth it if you need an exact patch level. Install the build dependencies
and point `configure` at them explicitly — Ruby will not find them on its own:

```bash
brew install ruby-install openssl@3 libyaml

ruby-install ruby 3.3.4 -- \
  --with-openssl-dir="$(brew --prefix openssl@3)" \
  --with-libyaml-dir="$(brew --prefix libyaml)"
```

Then **verify the extensions actually built** before trusting it:

```bash
~/.rubies/ruby-3.3.4/bin/ruby -e "require 'openssl'; require 'psych'; puts 'ok'"
```

A source build can print `Successfully installed ruby` while `openssl` and
`psych` silently failed to compile. Do not use `--disable-install-doc` here: the
RDoc step needs psych, so its failure is often the only loud signal that
anything went wrong. Watch for `*** Following extensions are not compiled:` and
check `~/src/ruby-3.3.4/ext/openssl/mkmf.log` if you see it.
