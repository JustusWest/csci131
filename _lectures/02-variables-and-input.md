---
title: "02 — Variables and Input"
published: true
---

**Reading:** _Python for Everybody_, §2.2–2.4, §2.10, §2.12

**Goal for today:** write a program which takes input from the user and computes output based on input.

---

## 0. Review

Last time we learned about REPL, the difference between names and strings, types, and the difference between using the interpreter and writing a script.

Remember:

```python
>>> type(17)
<class 'int'>
>>> type('17')
<class 'str'>
```

They may look the same, but Python treats them differently.

## 1. Variables

A **variable** is a name that refers to a value. We create them with **assignment statements**

<details class="code-example" markdown="1">
<summary>Live code — assignment</summary>

```python
>>> message = 'Hello world'
>>> n = 14
>>> pi = 3.1415926535897931
>>> n
14
>>> print(n)
14
>>> print(message)
Hello world
>>> print(n + pi)
17.1415926535897931

```

Notice that the assignment lines print nothing. Assignment is an instruction: _store this value under this name._

</details>

### `=` does not mean "equals"

In algebra, `x = 5` is a **claim**: a statement about the world that is either true or false. In Python, `x = 5` is an **instruction**: _put 5 in the box named x._ An instruction can be given again to overwrite the value in the box.

<details class="code-example" markdown="1">
<summary>Live code — a variable varies</summary>

```python
>>> x = 5
>>> print(x)
5
>>> x = 7
>>> print(x)
7
>>> x = 'now I am a string'
>>> print(x)
now I am a string
>>> type(x)
<class 'str'>
```

The variable name `x` does not change, it's the same box. With different assignment statements, we **vary** the value in the box.

</details>

Assignment statements work **right to left**; first we evaluate the expression on the right hand side, then assign the variable name on the left to that value.

### Naming rules

Names can contain letters, digits, and underscores. They can't start with a digit, and certain names are **reserved** by Python because they already refer to something.

<details class="code-example" markdown="1">
<summary>Live code — illegal names</summary>

```python
>>> 76trombones = 'big parade'
  File "<stdin>", line 1
    76trombones = 'big parade'
     ^
SyntaxError: invalid decimal literal

>>> class = 'Advanced Theoretical Zymurgy'
  File "<stdin>", line 1
    class = 'Advanced Theoretical Zymurgy'
          ^
SyntaxError: invalid syntax
```

The first is illegal because it starts with a number. The second is illegal because `class` is a **reserved keyword**.

</details>

Here is the full list, but you don't need to memorize it:

|          |            |           |            |
| -------- | ---------- | --------- | ---------- |
| `False`  | `await`    | `else`    | `import`   |
| `None`   | `break`    | `except`  | `in`       |
| `True`   | `class`    | `finally` | `is`       |
| `and`    | `continue` | `for`     | `lambda`   |
| `as`     | `def`      | `from`    | `nonlocal` |
| `assert` | `del`      | `global`  | `not`      |
| `async`  | `elif`     | `if`      | `or`       |
| `pass`   | `return`   | `try`     | `while`    |
| `raise`  | `with`     | `yield`   |            |

Names are arbitrary, they don't have any impact on the execution of the program. These are all equivalent behind the scenes:

```python
x = 35
y = 2.75
z = x * y
```

```python
a1b2c3 = 35
qq = 2.75
whatever = a1b2c3 * qq
```

```python
hours = 35
rate = 2.75
pay = hours * rate
```

The only impact of naming is readability - it's good practice to name things based on what they mean

## 2. `input`

If we want a variable to be set when we run the program, we use `input`:

<details class="code-example" markdown="1">
<summary>Live code — input</summary>

```python
>>> name = input('What is your name? ')
What is your name? Chuck
>>> print(name)
Chuck
>>> print('Hello', name)
Hello Chuck
```

`input` does three things: it prints the prompt you gave it, waits for the user to type something and press Enter, and assigns the typed value to the variable.

It is good practice to put a space at the end of the `input` prompt so the user text is separated (i.e. `input('What is your name? ')`)

</details>

What type comes out of input?

<details class="code-example" markdown="1">
<summary>Live code</summary>

```python
>>> apples = input('Enter apples: ')
Enter apples: 10
>>> oranges = input('Enter oranges: ')
Enter oranges: 5
>>> total = apples + oranges
'105'
```

What happened? Remember how we can check under the hood:

```python
>>> print(total)
105
>>> type(total)
<class 'str'>

```

</details>

**`input` always gives you back a string regardless of what the user types.**

In this example, the `+` oeprator glued the two strings together (don't worry about why just yet).

This example fails silently, but that won't always be the case:

<details class="code-example" markdown="1">
<summary>Live code</summary>

```python
>>> pay = input('Enter pay: ')
Enter pay: 10
>>> hours = input('Enter hours: ')
Enter hours: 40
>>> total = pay * hours
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```

In this example, we used the `*` operator, which is not valid for strings so the program crashes.

</details>

### Type conversion.

<details class="code-example" markdown="1">
<summary>Live code — <code>int</code> and <code>float</code></summary>

```python
>>> int('35')
35
>>> float('2.75')
2.75
>>> int(hours) * float(rate)
96.25
```

`int` and `float` are some of the reserved keywords. They refer to **type conversion functions**, we can give them some data and they do their best to convert it into a number.

Which one do you use?

- `int` is short for integer; it refers to whole numbers.
- `float` is short for floating point number; it refers to numbers that have a decimal place

**If you are unsure, use `float`.** It handles `35` as `35.0`; `int` cannot handle `2.75`.

```python
# spelled out
pay_str = input('Enter pay: ')
pay = float(pay_str)

# nested -- convert as it comes in
pay = float(input('Enter pay: '))
```

The nested version reads inside-out: `input` runs first and produces text, then `float` converts that text, then `=` stores the result.

</details>

<details class="code-example" markdown="1">
<summary>What if the user types something that isn't a number?</summary>

```python
>>> pay = input('Enter pay: ')
Enter pay: apple
>>> int(pay)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: apple'
```

The program crashes on unexpected input. For now, we assume the user gives us the right input type; we will learn how to handle this gracefully later.

</details>

---

## 3. Putting it together

For this weeks assignment, programs will have this shape:

1. **Prompt** — `input` a value
2. **Convert** — `int` or `float` it
3. **Compute** — do the arithmetic
4. **Print** — the answer

We will build this up one step at a time

<details class="code-example" markdown="1">
<summary>Live code — <code>dinner.py</code>, stage 1</summary>

```python

bill = float(input('Bill total: '))
print('Bill:', bill)
```

```
Bill total: 40
Bill: 40.0
```

</details>

<details class="code-example" markdown="1">
<summary>Live code — <code>dinner.py</code>, stage 2</summary>

Add the tip:

```python
bill = float(input('Bill total: '))
tip_percent = float(input('Tip percent: '))

tip = bill * tip_percent / 100
total = bill + tip

print('Bill:', bill)
print('Tip:', tip)
print('Total:', total)
```

```
Bill total: 40
Tip percent: 20
Bill: 40.0
Tip: 8.0
Total: 48.0
```

</details>

<details class="code-example" markdown="1">
<summary>Live code — the finished <code>dinner.py</code></summary>

Split it:

```python

bill = float(input('Bill total: '))
tip_percent = float(input('Tip percent: '))
people = int(input('How many people? '))

tip = bill * tip_percent / 100
total = bill + tip
each_pays = total / people

print('Bill:', bill)
print('Tip:', tip)
print('Total:', total)
print('Each person pays:', each_pays)
```

```
Bill total: 40
Tip percent: 20
How many people? 4
Bill: 40.0
Tip: 8.0
Total: 48.0
Each person pays: 12.0
```

</details>

Let's check the correctness with a test case (something we already know the answer for):

A $40 bill, a 20% tip, four people. That is $8 of tip, $48 total, $12 each. If your program is printing something else, there is an error somewhere. This error will not surface with an error message, we call it a **semantic error** meaning the program runs but theres something wrong in the logic.
---
### Practice
Assume that we execute the following assignment statements:

```python
  width = 17
  height = 12.0
```
For each of the following expressions, guess the value and type of the expression:
1. width//2
2. width/2.0
3. height/3
4. width//height
5. width/height
6. 1+ 2 * 5

Use the Python interpreter to check your guesses.

What is the difference between `//` and `/`?


---

## Before Next Class

Next time is our **first graded programming assignment**. You write it in the room on the lab machines, and you submit before you leave.

1. **Read §2.2–2.4, §2.10, and §2.12.** We've covered most of this content during lecture.
