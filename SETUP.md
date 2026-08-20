# Setting up a GitHub Pages site for CSCI 131

Mirrors your CSCI 264 setup: Jekyll + the `minima` theme, built by GitHub's
classic Pages builder (no Actions workflow, no local build required to publish).

Target URL: **https://justuswest.github.io/csci131/**

I have already scaffolded the files at `C:\Users\micha\git-repos\csci131`.
Steps 1 and 2 below are the only parts you have to do by hand.

---

## What 264 actually is (so you know what you're copying)

| Piece | Value |
|---|---|
| Repo | `JustusWest/csci264`, branch `main`, site at repo root |
| Builder | GitHub's built-in Jekyll 3.10 (the `github-pages` gem), *not* a workflow |
| Theme | `minima`, overridden by `assets/main.scss` |
| `baseurl` | `/csci264` — required because it's a project page, not a user page |
| Content | `_lectures/` collection → `/lectures/:name/`; `labs/`, `code/`, `files/` are plain static folders that the `.md` pages enumerate with Liquid |

The clever bit worth preserving: `labs.md` and `code.md` don't list anything by
hand. They loop over `site.static_files` and pick up whatever you drop in those
folders. Add a PDF to `labs/`, commit, and it appears on the site.

---

## Step 1 — Create the empty repo on GitHub

1. Go to <https://github.com/new>.
2. Owner `JustusWest`, repository name **`csci131`** (lowercase — it becomes the URL path).
3. **Public.** GitHub Pages on a free account only publishes public repos.
4. Do **not** check "Add a README", ".gitignore", or a license. The local folder already has files; an initialized remote just forces you to merge.
5. Create repository.

## Step 2 — Push the scaffolded folder

In a terminal (Git Bash, PowerShell, or the VS Code terminal):

```bash
cd C:/Users/micha/git-repos/csci131
git init -b main
git add .
git commit -m "Initial site scaffold"
git remote add origin https://github.com/JustusWest/csci131.git
git push -u origin main
```

## Step 3 — Turn Pages on

1. In the new repo: **Settings → Pages** (left sidebar, under "Code and automation").
2. **Source:** `Deploy from a branch`.
3. **Branch:** `main`, folder `/ (root)`. Save.
4. Wait 1–2 minutes. The Actions tab will show a `pages build and deployment`
   run; when it goes green, the site is live at
   `https://justuswest.github.io/csci131/`.

If you get a 404 for a couple of minutes after the build succeeds, that's DNS/CDN
propagation — give it five minutes before assuming something is wrong.

## Step 4 — Sanity-check the `baseurl`

This is the one thing that reliably breaks project-page sites. `_config.yml`
already has:

```yaml
baseurl: "/csci131"
```

That must match the repo name exactly. Every internal link in the scaffold goes
through `{{ "/path" | relative_url }}`, which prepends the baseurl. If you ever
hard-code `/files/whatever.pdf` in a page, it will 404 on GitHub while working
fine locally. Always use `relative_url`.

## Step 5 — Local preview (optional but worth it)

Same as 264:

```bash
cd C:/Users/micha/git-repos/csci131
bundle install     # first time only
bundle exec jekyll serve
```

Then open <http://localhost:4000/csci131/> — note the baseurl is part of the
local URL too.

If `bundle install` complains about Ruby, you already have a working Ruby+DevKit
from the 264 site, so this should just work. `Gemfile.lock` is gitignored, which
is what you want when GitHub does the real build.

---

## What's in the scaffold

```
csci131/
├── _config.yml            title/baseurl/theme/collections — edit the title, term
├── Gemfile                github-pages + webrick, identical to 264
├── .gitignore             _site/, .jekyll-cache/, Gemfile.lock
├── index.md               home page — YOUR SECTION TIMES ARE "TODO" HERE
├── lectures.md            auto-lists the _lectures collection
├── labs.md                auto-lists PDFs in labs/
├── code.md                auto-lists files in code/
├── assets/main.scss       copied verbatim from 264 (the .code-example styling)
├── _lectures/
│   └── 01-python-intro.md placeholder — overwrite or delete
├── labs/    .gitkeep      drop lab PDFs here
├── code/    .gitkeep      drop .py examples here
├── files/   .gitkeep      syllabus PDF goes here
└── figures/ .gitkeep      images referenced from lecture notes
```

### Before you push, edit these

1. **`index.md`** — the Sections table has `TODO` placeholders for days, times,
   and rooms. Instructor block and office hours were carried over from 264;
   confirm they're still right for the fall.
2. **`files/`** — drop in your CSCI 131 syllabus PDF named
   `CSCI131_Syllabus_Fall26.pdf`, or change the link in `index.md` to match
   whatever you name it. Right now that link points at a file that doesn't exist.
3. **Term** — I assumed Fall 2026 (matching 264). The syllabus in your project is
   the Spring 2026 version taught by Prof. Rufinus, so if you're building this
   for spring, change `description:` in `_config.yml` and the date line in
   `index.md`.
4. **`_lectures/01-python-intro.md`** — placeholder text. It exists so the
   Lecture Notes page isn't empty on the first build.

---

## Day-to-day workflow after setup

Adding a lecture:

```bash
# create _lectures/03-loops.md with front matter:
#   ---
#   title: "03 Loops: while and for"
#   ---
git add . && git commit -m "Add lecture 03" && git push
```

Adding a lab or code example: drop the file in `labs/` or `code/`, commit, push.
No index to update — the Liquid loops handle it.

Files are sorted by filename, so keep the `01_`, `02_` numeric prefixes you used
in 264 or the ordering will go alphabetical on you.

---

## Two things that differ from 264 and are worth deciding now

**Python code display.** Your 264 notes use `<details class="code-example">`
blocks with side-by-side Python/C tables. For 131 there's no second language to
compare against, so plain fenced code blocks may read better than the collapsible
`<details>` wrapper. The CSS is there either way — the scaffold keeps
`assets/main.scss` verbatim so you can use it or ignore it.

**Runnable examples.** Intro Python students benefit from being able to run
snippets without installing anything. If you want that, linking each example to
a pre-filled Python Tutor or Google Colab URL is a low-effort addition; it needs
no change to the Jekyll setup. Not necessary, just easier here than it was for
assembly.
