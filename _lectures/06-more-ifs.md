---
title: "06 — more ifs"
published: false
---
NOTE: Lecture 5 was far too long, had to cut content into another one.

---

## 6. Order matters

<details class="code-example" markdown="1">
<summary>Live code — example mistake</summary>

```python
score = int(input('Score: '))

if score >= 60:
    print('D')
elif score >= 70:
    print('C')
elif score >= 80:
    print('B')
elif score >= 90:
    print('A')
else:
    print('F')
```

```
Score: 95
D
```

</details>

Every condition in there is correct. `95 >= 60` really is `True`. The chain is just in the wrong order.

Remember rule 1: the first open door wins. A 95 walks down the hallway, tries `score >= 60`, finds it open, and goes through. It never reaches the `>= 90` test at all. In fact **every** passing score prints `D`, and the other three branches are unreachable.

<details class="code-example" markdown="1">
<summary>Live code — <code>grade.py</code>, fixed</summary>

```python
# grade.py

score = int(input('Score: '))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```

```
Score: 95
A
```

```
Score: 83
B
```

```
Score: 70
C
```

```
Score: 12
F
```

</details>

Only the order changed. Nothing else.

Notice what the fixed version lets you leave out. The `elif score >= 80` branch does **not** need to say "and less than 90". If we had got to that line at all, the `>= 90` test already failed — so the score is already known to be under 90. Each branch in a chain gets to assume every condition above it was `False`.

**The rule:** in a chain of overlapping conditions, put the **most restrictive test first**, and work outward.

> **Ask:** does the order matter in `weekday.py`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

No. A day cannot be both `1` and `3`, so no two conditions can be `True` at once, and shuffling the branches changes nothing.

Order matters exactly when the conditions **overlap**. `>=` and `<=` tests overlap almost every time; `==` tests against distinct values almost never do.

</details>

---

## 7. `elif` against a stack of separate `if`s

A chain of `elif` and a pile of separate `if` statements look similar and behave differently. Here is the same `score` run through both.

<details class="code-example" markdown="1">
<summary>Live code — four separate <code>if</code> statements</summary>

```python
score = 95

if score >= 90:
    print('A')
if score >= 80:
    print('B')
if score >= 70:
    print('C')
if score >= 60:
    print('D')
```

```
A
B
C
D
```

</details>

Four independent questions, each asked and answered. All four are true of a 95, so all four print.

<details class="code-example" markdown="1">
<summary>Live code — the same conditions as a chain</summary>

```python
score = 95

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
```

```
A
```

</details>

One question with four possible answers. The first match wins and the rest are skipped.

Ask yourself which one you are writing:

- **Separate `if`s** — independent checks. Any number of them may apply. *Does this order qualify for free shipping? Is the customer a member? Is it a holiday?* All three can be true at once.
- **An `elif` chain** — one decision with several possible outcomes. Exactly one applies. *Which letter grade? Which shipping band? Positive, negative, or zero?*

---

## 8. Putting it together — `ticket.py`

Let's build one from nothing, the way we built `seconds.py`. Admission is \$12, but children 12 and under pay \$7 and seniors 65 and over pay \$9.

<details class="code-example" markdown="1">
<summary>Live code — stage 1: read the input</summary>

Start with the part you already know how to write, and run it.

```python
# ticket.py -- CSCI 131, Wednesday Sept 16

age = int(input('Age: '))
print('Age is', age)
```

```
Age: 40
Age is 40
```

An age is a count, so `int`. Always run the boring version first — if the input is wrong, nothing after it can be right.

</details>

<details class="code-example" markdown="1">
<summary>Live code — stage 2: one branch at a time</summary>

Take the cases in order. Most restrictive first — the youngest band, then the oldest, then everyone else.

```python
age = int(input('Age: '))

if age <= 12:
    price = 7
elif age >= 65:
    price = 9
else:
    price = 12

print('Price:', price)
```

```
Age: 8
Price: 7
```

```
Age: 70
Price: 9
```

```
Age: 40
Price: 12
```

</details>

Look closely at what each branch does. It does **not** print. It assigns to `price`, and a single `print` after the chain does the talking.

That is worth making a habit of. The branches decide; the code after the chain acts. Change the wording of the output later and there is exactly one line to edit, not three.

<details class="code-example" markdown="1">
<summary>Live code — stage 3: the day of the week</summary>

Tuesdays are \$2 off, for everybody.

```python
age = int(input('Age: '))
day = input('Day: ')

if age <= 12:
    price = 7
elif age >= 65:
    price = 9
else:
    price = 12

if day == 'Tuesday':
    price = price - 2

print('Price:', price)
```

```
Age: 40
Day: Tuesday
Price: 10
```

```
Age: 8
Day: Friday
Price: 7
```

</details>

Two decisions, so two separate structures — a chain for the age band, and then an independent `if` for the discount. The discount is not a fourth kind of customer; it applies on top of whichever band you landed in. This is section 7 in practice.

Also note `price = price - 2`: that is reassignment, from September 4, doing exactly what it did there. Work out the right-hand side with the value `price` has right now, then point the name at the result.

And note `day` is **not** converted. It is a word, so it stays a `str`, and `==` compares two strings perfectly well:

<details class="code-example" markdown="1">
<summary>Live code — comparing strings</summary>

```python
>>> 'Tuesday' == 'Tuesday'
True
>>> 'Tuesday' == 'tuesday'
False
>>> 'Tuesday' == 'Tuesday '
False
```

String comparison is exact. Capital letters count. A trailing space counts. This is a real source of "but I typed it right" bugs, and for now the answer is simply to tell the user exactly what to type.

</details>

---

## 9. One more — `shipping.py`

<details class="code-example" markdown="1">
<summary>Live code</summary>

Shipping is free on orders of \$50 or more, \$5 on orders of \$20 or more, and \$9 otherwise.

```python
# shipping.py

total = float(input('Order total: '))

if total >= 50:
    shipping = 0
elif total >= 20:
    shipping = 5
else:
    shipping = 9

print('Shipping:', shipping)
print('Amount due:', total + shipping)
```

```
Order total: 64.25
Shipping: 0
Amount due: 64.25
```

```
Order total: 31.00
Shipping: 5
Amount due: 36.0
```

```
Order total: 12.50
Shipping: 9
Amount due: 21.5
```

</details>

A money total is a measurement, so `float` — someone will type `31.00`, and `int` would crash on it. Same judgment call as September 4: ask what the quantity *is*.

Check the boundaries by hand before you trust a program like this. Exactly \$50 should be free, and it is, because the test is `>=` and not `>`. Exactly \$20 should be \$5. Those two values are where the bugs live, so those two values are what you test.

---

## 10. The shapes, all together

```python
if condition:              # sometimes runs
    ...

if condition:              # exactly one of the two
    ...
else:
    ...

if condition:              # exactly one of the several
    ...
elif other_condition:
    ...
elif third_condition:
    ...
else:
    ...
```

- `if` needs a condition. `elif` needs a condition. `else` never takes one.
- Every one of those lines ends in a colon, and every block under them is indented four spaces.
- In a chain, the first `True` condition wins and the rest are skipped.
- Order the branches most restrictive first whenever the conditions overlap.

---

## Before Friday

Read §3.3–3.5 if you have not. Then take `grade.py` and `ticket.py` and run them on the boundary values — 90, 89, 12, 13, 65, 64 — and satisfy yourself that each one lands in the band you expect. Boundaries are where these programs break.

Friday is your **third graded programming assignment**, on paper from the start — no starter files this time. Three short programs, all of them decisions.

Monday we add `and`, `or` and `not`, which let a single branch ask about more than one thing at once.
