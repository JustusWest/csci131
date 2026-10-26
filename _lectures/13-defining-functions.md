---
title: "13 — Defining Functions"
published: true
---

**Monday, October 26**

**Reading:** *Python for Everybody*,  §4.1–4.9 and §4.12


---

## 1. Functions you already use

Many of the things we've written thus far use the `()` syntax, but we haven't named it yet. These are called **functions**:

```python
name = input('Name: ')
age = int('19')
n = len('banana')
highest = max(scores)
print('Hello')
```

Every one of these is a **function call**: a name, then parentheses with the values you hand it inside. For example:

```
len('banana')
```

- `len` is the **name** of the function.
- `'banana'` is the **argument**: the value you hand to the function.
- `6` is the **return value**: the value the call is replaced by.

A function is a piece of code with a **name**, which you can **use** without rewriting it.

### Functions in a module

Some functions aren't available until you import them. They live in a **module**, a file of functions someone else wrote, and `import` brings it in:

<details class="code-example" markdown="1">
<summary>Live code — <code>math</code> and <code>random</code></summary>

```python
>>> import math
>>> math.sqrt(16)
4.0
>>> math.sqrt(2)
1.4142135623730951
>>> import random
>>> random.randint(1, 6)
4
```

</details>

`math.sqrt` means *the `sqrt` function from the `math` module*. It is the same dot as in `word.upper()`. You have seen `random` before, in the starter code for rock paper scissors. (Your `randint` will probably give a different number. That's the point of it.)

---

## 2. Writing a function: `def`

Open a new file:

<details class="code-example" markdown="1">
<summary>Live code — <code>menu.py</code>, first try</summary>

```python
# menu.py -- CSCI 131, Monday Oct 26

def show_menu():
    print('1. Add a score')
    print('2. Show the average')
    print('3. Quit')
```

</details>

- `def` is short for *define*. It starts a **function definition**.
- `show_menu` is the name we are giving the function. Function names follow the same rules as variable names.
- The parentheses are required. This function takes no arguments, so they are empty.
- The colon and the indented lines below it are the same shape as an `if` or a `while`. The first line is the **header**; the indented lines are the **body**.

> **Ask:** what happens when you run this code?

<details class="code-example" markdown="1">
<summary>Answer</summary>

Nothing. No error, and nothing printed.

</details>

`def` doesn't run the body. It **stores** the body under the name `show_menu`, so it can be run later. To run it, you **call** the function by writing the name, then parentheses.

<details class="code-example" markdown="1">
<summary>Live code — <code>menu.py</code>, with a call</summary>

```python
# menu.py -- CSCI 131, Monday Oct 26

def show_menu():
    print('1. Add a score')
    print('2. Show the average')
    print('3. Quit')

show_menu()
```

```
1. Add a score
2. Show the average
3. Quit
```

</details>

The call `show_menu()` is not indented, so it isn't part of the function. It is the program. Call it twice and you get the menu twice, without writing the three `print`s again.

### Try it in the shell

Once you run your code, the IDLE shell knows about every function in your file. You can call them there to try them out:

```python
>>> show_menu()
1. Add a score
2. Show the average
3. Quit
```

This is the quickest way to check a function you just wrote. Use it.

---

## 3. Flow of execution

Python still runs a program from top to bottom, one line at a time. A function call changes that: Python **jumps** into the function's body, runs it, and then **comes back** to the line after the call.

<details class="code-example" markdown="1">
<summary>Live code — <code>menu.py</code>, with lines around the call</summary>

```python
# menu.py -- CSCI 131, Monday Oct 26

def show_menu():
    print('1. Add a score')
    print('2. Show the average')
    print('3. Quit')

print('Welcome!')
show_menu()
print('Pick one.')
```

```
Welcome!
1. Add a score
2. Show the average
3. Quit
Pick one.
```

</details>

In order, Python:

1. reads the `def` and stores the body under `show_menu` (no output)
2. prints `Welcome!`
3. sees `show_menu()`, and jumps to the body
4. prints the three lines of the menu
5. reaches the end of the body, and comes back to the line after the call
6. prints `Pick one.`


### Define it before you call it

What if the call comes first?

<details class="code-example" markdown="1">
<summary>Live code — calling before the <code>def</code></summary>

```python
show_menu()

def show_menu():
    print('1. Add a score')
    print('2. Show the average')
    print('3. Quit')
```

```
Traceback (most recent call last):
  File "menu.py", line 1, in <module>
    show_menu()
NameError: name 'show_menu' is not defined
```

</details>

Python is still going top to bottom. On line 1 it hasn't reached the `def` yet, so it has never heard of `show_menu`. It is the same error you get from using a variable before you assign it.

So every program in this unit has the same layout: **all the `def`s at the top, the program underneath.**

---

## 4. Parameters

`show_menu` does exactly the same thing every time. Most useful functions need to be **given** something to work on, the way `len` is given a string. Here is a function that prints a word with a line above and below it:

<details class="code-example" markdown="1">
<summary>Live code — <code>banner.py</code></summary>

```python
# banner.py -- CSCI 131, Monday Oct 26

def banner(word):
    line = '=' * len(word)
    print(line)
    print(word)
    print(line)

banner('Widener')
banner('CSCI 131')
```

```
=======
Widener
=======
========
CSCI 131
========
```

</details>

`word` in the header is a **parameter**: a name for whatever value the function is handed. `'Widener'` in the call is the **argument**: the value it is handed this time.

When Python runs `banner('Widener')`, it starts the function by doing an assignment for you:

```python
word = 'Widener'
```

and then runs the body. For `banner('CSCI 131')`, it starts with `word = 'CSCI 131'` instead. Same body, different value, so the line comes out a different length. (`'=' * len(word)` is string repetition from Unit 1 and `len` from Unit 4.)

### The argument's name doesn't matter

The argument can be a variable, or any expression:

<details class="code-example" markdown="1">
<summary>Live code — variables as arguments</summary>

```python
school = 'Widener'
banner(school)
banner(school + ' Pride')
```

```
=======
Widener
=======
=============
Widener Pride
=============
```

</details>

The variable is called `school`, and the parameter is called `word`. That's fine. Python works out the **value** of the argument (`'Widener'`, then `'Widener Pride'`) and hands that value over. Inside `banner`, it is always called `word`, whatever it was called outside.

---

## 5. Conclusion

| word | meaning | in `banner` |
| - | - | - |
| **definition** | `def`, a header and an indented body; stores the code, doesn't run it | the whole `def banner(word):` block |
| **header** | the first line: `def`, name, parameters, colon | `def banner(word):` |
| **body** | the indented lines that run when the function is called | the four lines under the header |
| **parameter** | a name in the header for the value the function is handed | `word` |
| **call** | the name and parentheses; runs the body | `banner('Widener')` |
| **argument** | the value in the call | `'Widener'` |

```python
def show_menu():                # no parameters: parentheses still required
    print('1. Add a score')

def banner(word):               # one parameter
    line = '=' * len(word)
    print(line)
    print(word)
    print(line)

show_menu()                     # calls: the program goes under the defs
banner('Widener')               # starts with word = 'Widener'
```

- `def` **stores** a function. Nothing runs until you **call** it.
- A call jumps into the body, runs it, and comes back to the line after the call.
- Define a function before you call it, so put every `def` at the top of the file.
- A call starts by assigning the argument to the parameter. The argument's name outside doesn't matter.
- Once you have run your file, call your functions in the shell to try them out.

On Wednesday: functions with more than one parameter, and lists as arguments.

---

## 6. Exercise — `box.py`

Write a function `box(word)` that prints the word inside a box of `*` characters, with one space on each side of the word:

```
***********
* Widener *
***********
```

Under the function, call it twice, with `'Widener'` and `'Python'`, and check that each box fits its word:

```
***********
* Widener *
***********
**********
* Python *
**********
```

**If you finish:** change the program so it asks for your name and puts it in a box. The argument is now a variable, not a string you typed.

```
Your name: Ana Lopez
*************
* Ana Lopez *
*************
```

<details class="code-example" markdown="1">
<summary>Solution</summary>

```python
# box.py -- CSCI 131, Monday Oct 26

def box(word):
    edge = '*' * (len(word) + 4)
    print(edge)
    print('* ' + word + ' *')
    print(edge)

box('Widener')
box('Python')

name = input('Your name: ')
box(name)
```

</details>
