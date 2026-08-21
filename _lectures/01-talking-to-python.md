---
title: "01 — Talking to Python: the Interpreter, Types, and Errors"
---

**Wednesday, August 26**

**Reading:** _Python for Everybody_, §1.3, §1.5, §1.7–1.8, §1.10, and §2.1, §2.5–2.7, §2.11

**Goal for today:** by the end of the period you will have written, saved, and run a Python program of your own.

---

## 1. Whats a program

A **program** is a sequence of instructions written down in a language the computer can follow. The hard part of this course is not learning the instructions, the hard part is learning to say what you mean with enough precision that a machine gets it right.

1. **Say it precisely.** Break a problem into steps small enough that each one is obviously correct.
2. **Read what it actually did.** When the machine does something surprising, the machine is right and your instructions were wrong.

---

## 2. The Python prompt

Open **IDLE** from the Start menu. You get a window with this in it:

```
Python 3.x.x
>>>
```

Those three angle brackets are a **prompt**. Python is telling you it is waiting, and that it will respond to whatever you type.
This is the **interactive interpreter**, it's the best way to quickly test a statement.

---

## 3. Arithmetic

Let's test a couple basic math statements to see what python does.

<details class="code-example" markdown="1">
<summary>Live code — arithmetic at the prompt</summary>

```python
>>> 2 + 3
5
>>> 100 - 7
93
>>> 6 * 7
42
>>> 10 / 4
2.5
>>> 10 / 5
2.0
>>> (5 + 9) * (15 - 7)
112
```

Notes on what you just saw:

- `10 / 4` gives `2.5`, not `2`. Fine so far.
- `10 / 5` gives `2.0`, **not** `2`. Division produces a decimal number even when it divides evenly.
- Parentheses control the order of operations, just like algebra.

</details>

As you typed expressions into the interpreter it cycled through three stages

- **Read** happens automatically as you type
- **Evaluate** happens behind the scens when you hit enter
- **Print** happens when Python responds to you

This is know as a **REPL** or read, evaluate, print loop

### Order of operations

<details class="code-example" markdown="1">
<summary>Live code — precedence</summary>

```python
>>> 1 + 2 * 5
11
>>> 6 + 4 / 2
8.0
>>> 5 - 3 - 1
1
```

Python uses basic PEMDAS, grouping into ''tiers'' - within a tier it works left to right.

**When in doubt, use parentheses.** They cost nothing and make your intentions explicit.

</details>

There are some more arithmetic operators, but we leave them til later.

---

## 4. `print`

At the prompt, Python shows you the value of every expression you type (this is the **print** part of REPL). In a saved program the print is not automatic, we have to do it ourselves.

<details class="code-example" markdown="1">
<summary>Live code — print</summary>

```python
>>> print(4)
4
>>> print(2 + 3)
5
>>> print('Hello, World!')
Hello, World!
>>> print('The answer is', 42)
The answer is 42
```

Three things to notice:

1. `print` needs **parentheses** around what you want printed.
2. Text goes in **quotes**. `'Hello'` is text; `Hello` without quotes means something completely different.
3. If you give `print` several things separated by commas, it sticks them together with a space between them.

</details>

`print` is a **function**: a named piece of work that somebody else already wrote, which you can use by name. We write our own in a few weeks. For now, know that `name(...)` means "run the thing called _name_ on the stuff in the parentheses."

---

## 5. Basic Types

Every value in Python has a **type**, and the type decides what Python will do with it. Ask with the `type` function.

<details class="code-example" markdown="1">
<summary>Live code — the three types we care about</summary>

```python
>>> type(17)
<class 'int'>
>>> type(3.2)
<class 'float'>
>>> type('Hello, World!')
<class 'str'>
```

- **`int`** — a whole number
- **`float`** — a number with a decimal point
- **`str`** — a string, any piece of text (a string of characters)

What's going on here?

```python
>>> type('17')
<class 'str'>
```

`17` is a number. `'17'` is a string that looks like a number.

</details>

---

## 6. Error Messages

If we try to break the rules Python will tell us with an error message. The error message is informative: it tells us what went wrong. Learning how to read error messages is an important skill

<details class="code-example" markdown="1">
<summary>Live code — three errors, on purpose</summary>

**A syntax error.** You broke a rule about how Python sentences are written.

```python
>>> print('hello)
  File "<stdin>", line 1
    print('hello)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

We opened a quote and never closed it, so Python reached expecting a quote it never found. The `^` tells use where the problem started, not where it finished.

Similarly, we have to close and parenthesis we open. Try this in the IDLE shell:

```python
>>> print('hello'
```

The shell expects more so it never evaluates. Try this in a file (name it first.py)

```python
print('hello'
print('world')
```

```
  File "first.py", line 1
    print('hello'
         ^
SyntaxError: '(' was never closed
```

This is a common error you will make all semester, and it is usually just a typo.

**A name error.** You used a word which is not in the vocabularly.

```python
>>> print(hello)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
```

Without quotes, `hello` is not text — it is a _name_, and Python goes looking for something called `hello`.
hello

````

The quotes are the entire difference between "the word hello" and "the thing named hello."

**A type error.** You tried comparing apples and oranges.

```python
>>> 'hello' + 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
````

Adding a number to a word is not a meaningful request. Python is telling you it has a `str` and an `int` and no idea what you want to do with them.

</details>

**How to read an error message:** The last line tells you the type of error you made or what went wrong. The block of text above it (often very large) is a **traceback**, Python's best guess of where the problem is.

---

## 7. Our first program

When we work in the IDLE shell everything we type goes away as soon as we close the shell.

Real programs live in files. Make a folder on your desktop with your name - this is where you should save all your programs for this class, for ease of use.

In IDLE: **File → New File**, you will get a blank text editor - this is not an interpreter its a document.

<details class="code-example" markdown="1">
<summary>Live code — <code>hello.py</code></summary>

Type this into the new window:

```python
print('Hello, World!')
```

Then **File → Save As**, name it `hello.py`, and save it in the folder. Then press **F5** to run it.

Check the shell and you should see:

```
Hello, World!
```

Try some of our arithmetic statements in the `hello.py` file:

</details>

<details class="code-example" markdown="1">
<summary>Live code</summary>

```python
2 + 3
'Hello again'
```

Nothing new appears in the output.

At the `>>>` prompt, typing `2 + 3` shows you `5`, because interactive mode displays the value of whatever you type. **In a saved program, it does not.** Python evaluates `2 + 3`, gets `5`, and throws it away, because you never asked it to do anything with it.

We have to print explicity:

```python
print(2 + 3)
print('Hello again')
```

</details>

---

## 8. Comments

<details class="code-example" markdown="1">
<summary>Live code — comments</summary>

```python
# hello.py -- my first program
# Dr. West, CSCI 131

print('Hello, World!')   # this part greets the world
```

Everything from a `#` to the end of the line is ignored by Python completely. It is there for the human reading the code

</details>

---

## Before Friday

1. **Read** §1.3, §1.5, §1.7–1.8, §1.10, and §2.1, §2.5–2.7, §2.11 of _Python for Everybody_ (py4e.com/book).

Friday we cover variables and how to get information _from_ a user.
