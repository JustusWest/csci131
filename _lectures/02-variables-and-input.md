---
title: "02 — Variables, Input, and the Four-Step Shape"
published: false
---

**Friday, August 28**

**Reading:** *Python for Everybody*, §2.2–2.4, §2.10, §2.12

**Goal for today:** by the end of the period you will have written a program that asks a person a question and computes an answer from what they typed.

That last sentence is also a description of Monday's assignment. Today is the day that makes Monday possible, so if you are going to type along with one class this semester, make it this one.

---

## 0. Where we left off

Wednesday you learned that Python evaluates expressions and prints things, that quotes are the difference between text and a name, that every value has a type, and that in a saved file nothing appears unless you `print` it.

One thing from Wednesday to keep in the front of your mind all period:

```python
>>> type(17)
<class 'int'>
>>> type('17')
<class 'str'>
```

Same characters on the screen. Different kinds of thing. Today that distinction stops being trivia and starts costing points.

---

## 1. Variables

A **variable** is a name that refers to a value. You make one with an **assignment statement**.

<details class="code-example" markdown="1">
<summary>Live code — assignment</summary>

```python
>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415926535897931
>>> print(n)
17
>>> print(message)
And now for something completely different
>>> print(n + 3)
20
```

Notice that the assignment lines print nothing. Assignment is not a question, it is an instruction: *store this value under this name.* Python stores it and says nothing back.

</details>

### `=` does not mean "equals"

This is the biggest conceptual hurdle in Chapter 2, and it costs people points on Test 1 every year.

In math, `x = 5` is a **claim** — a statement about the world that is either true or false. In Python, `x = 5` is a **command**: *put 5 in the box labeled x.* A command can be given again, with a different value, and nothing is contradicted.

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

The name `x` did not change. What it *points at* changed, three times — and the third time it started pointing at something of an entirely different type. A variable's type is just the type of whatever is in it right now.

</details>

Read every assignment **right to left**: work out the right-hand side first, then point the name on the left at the result. That habit will pay off properly on September 4, when the right-hand side starts mentioning the variable being assigned.

### Naming rules

Names can contain letters, digits, and underscores. They **cannot start with a digit**, and they cannot be one of Python's reserved keywords.

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

The first is illegal because it starts with a number. The second is illegal because `class` is a **keyword** — one of the 35 words Python has reserved for itself: `if`, `for`, `def`, `while`, `and`, `or`, `not`, `import`, `return`, `True`, `False`, `None`, and 23 others.

You do not need to memorize the list. You need to recognize the symptom: *if a name that looks fine gives you a syntax error, it is probably a keyword.* The full list is on page 21 of the book.

</details>

### Names are for humans

Python does not care what you call things. These three programs are identical to Python:

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

Only one of them is readable, and the person it needs to be readable to is **you, three weeks from now, at 11pm.** Use **mnemonic** names — names that remind you what the value means. This is graded, lightly, all semester.

---

## 2. `input` — and the trap the whole course walks into

So far every program does the same thing every time you run it. To make it depend on *who is running it*, use `input`.

<details class="code-example" markdown="1">
<summary>Live code — asking a question</summary>

```python
>>> name = input('What is your name? ')
What is your name? Chuck
>>> print(name)
Chuck
>>> print('Hello', name)
Hello Chuck
```

`input` does three things: it prints the prompt you gave it, it stops and waits for the user to type something and press Enter, and it hands back what they typed.

Put a space at the end of your prompt string — `'What is your name? '` — or the user's typing will be jammed up against your question.

</details>

### Now the trap

We are going to write the pay program from Monday's assignment, badly, on purpose. Watch closely.

<details class="code-example" markdown="1">
<summary>Live code — the bug everybody writes</summary>

```python
>>> hours = input('Enter Hours: ')
Enter Hours: 35
>>> rate = input('Enter Rate: ')
Enter Rate: 2.75
>>> pay = hours * rate
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```

Why? Ask Python what it thinks it has:

```python
>>> type(hours)
<class 'str'>
>>> print(hours)
35
```

It *prints* as `35`. It *is* the string `'35'`.

> **`input` always gives you back a string. Always. Even when the user types digits.**

This is the single most important sentence in Chapter 2. Python has no way to know you wanted a number — the user typed characters on a keyboard, and characters are text.

And here is the genuinely nasty version — the one that does not crash:

```python
>>> print(hours + rate)
352.75
```

No error. No warning. Python took `'35'` and `'2.75'` and glued them end to end. It did not add them, and nothing told you so. If you had not been paying attention, you would have handed that in.

*(Why `+` glues strings instead of adding them is a September 4 question. Today the lesson is only that it does, silently, and that a number is not the same thing as text that looks like a number.)*

</details>

### The fix: convert

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

`int` and `float` are **type conversion functions**. Hand them a string that looks like a number and they hand back an actual number.

Which one do you use?

- `int` when the value can only be whole — a count of people, a number of pizzas.
- `float` when it can have a decimal part — money, temperature, hours worked.

**When you are unsure, use `float`.** It handles `35` just fine (as `35.0`); `int` cannot handle `2.75` at all. We will make this choice more carefully on September 4; for Monday, "when unsure use float" is the whole rule.

Two ways to write it. Both are correct:

```python
# spelled out
rate_text = input('Enter Rate: ')
rate = float(rate_text)

# nested -- convert as it comes in
rate = float(input('Enter Rate: '))
```

The nested version reads inside-out: `input` runs first and produces text, then `float` converts that text, then `=` stores the result. This is the form you will see everywhere, including on Monday's handout.

</details>

<details class="code-example" markdown="1">
<summary>What if the user types something that isn't a number?</summary>

```python
>>> speed = input('How fast? ')
How fast? an African or a European swallow
>>> int(speed)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'an African or a European swallow'
```

Your program crashes. For now that is fine and expected — **Monday's assignment assumes the user types a number.** Handling bad input gracefully needs `try` / `except`, which is Chapter 3. File it away; do not go looking for it yet.

</details>

---

## 3. Putting it together

Every program you write this week has the same four-step shape:

1. **Prompt** — `input` a value
2. **Convert** — `int` or `float` it
3. **Compute** — do the arithmetic
4. **Print** — report the answer

Here is all of today in one file. We build it a few lines at a time, running it after each addition. **Get something that runs, then grow it.** Do not write twenty lines and then start debugging.

<details class="code-example" markdown="1">
<summary>Live code — <code>dinner.py</code>, stage 1</summary>

The smallest thing that runs:

```python
# dinner.py -- CSCI 131, Friday Aug 28

bill = float(input('Bill total: '))
print('Bill:', bill)
```

```
Bill total: 40
Bill: 40.0
```

Four lines including a comment and a blank one, and it works. Note `40.0` — you typed `40`, `float` made it a decimal number. That is correct, not a bug.

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

One more input, one more line of arithmetic:

```python
# dinner.py -- CSCI 131, Friday Aug 28
# Dr. West

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

Things to notice on the way through:

- `people` is `int` — you cannot seat 3.7 people. `bill` is `float`, because money has cents.
- Every line of output is a `print`. Nothing appears on its own in a saved file — that was Wednesday's lesson and it has not changed.
- The prompts end with a space, so what the user types does not run into the question.

</details>

### Check it against something you already know

The last thing to do before calling a program finished: run it with numbers whose answer you can work out in your head.

A $40 bill, a 20% tip, four people. That is $8 of tip, $48 total, $12 each — no calculator needed. If the program had printed `Each person pays: 10.0`, it would still have *run*. No error message, no crash, nothing to alert you. A silent wrong answer is only catchable by checking it against an answer you already have.

**Every problem on Monday's assignment gives you a sample run with the correct output in it. That is not decoration.**

---

## What you should be able to do now

- [ ] Create a variable, print it, and reassign it to a different value and a different type.
- [ ] Say why `=` is a command and not a claim.
- [ ] Say why `76trombones` and `class` are illegal names.
- [ ] Use `input` with a prompt that ends in a space.
- [ ] **State from memory that `input` always returns a string**, and convert with `int` or `float` before doing arithmetic.
- [ ] Recognize the silent version of that bug — output that looks like two numbers stuck together.
- [ ] Write a program with the four-step shape: prompt, convert, compute, print.
- [ ] Check a finished program against an answer you already know.

## Before Monday

Monday is your **first graded programming session**. You write it in the room on the lab machines, and you submit before you leave. I will spend the first part of the period working an example at the board and the rest circulating while you work. Asking me for help is the intended use of that period.

To be ready:

1. **Read §2.2–2.4, §2.10, and §2.12.** You have seen most of it now.
2. **Do Exercise 4 at the end of Chapter 2.** Given `width = 17` and `height = 12.0`, write down the value *and the type* of each of `width//2`, `width/2.0`, `height/3`, and `1 + 2 * 5`. Then check yourself at the `>>>` prompt. One of those uses an operator we have not covered — predict what it does from the answer Python gives you, and bring your guess Friday.
3. **Make sure you can open IDLE, create a file, save it, and run it with F5 without help.** If any of those four steps is shaky, come to office hours before Monday — M–F 2:00–3:00, right before class, Freedom 319. Do not let a file-menu problem cost you points on a programming problem.
4. If Exercise 4 produces an error you cannot decode, **write the last line of the message down and bring it Monday.**

You have everything you need. See you Monday.
