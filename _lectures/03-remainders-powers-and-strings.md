---
title: "03 — Remainders, Powers, and Strings"
published: true
---

**Friday, September 4**

**Reading:** *Python for Everybody*, §2.5, §2.7–2.9, and §2.2 again

---

## 1. Different Division

<details class="code-example" markdown="1">
<summary>Live code — <code>/</code> vs <code>//</code> vs <code>%</code></summary>

```python
>>> 7 / 3
2.3333333333333335
>>> 7 // 3
2
>>> 7 % 3
1
```

- `/` is regular division. **It always gives a float**, even when it divides evenly: `10 / 5` is `2.0`, not `2`.
- `//` is **floor division** or **integer division** — divide and throw away the remainder.
- `%` is the **modulus** operator — it gives the remainder.

</details>

`%` is not commonly used in math, but is very useful in programming:

<details class="code-example" markdown="1">
<summary>Live code — modulus uses</summary>

```python
>>> 18 % 2      # remainder 0 means it divides evenly -- so, even
0
>>> 17 % 2      # remainder 1 -- odd
1
>>> 1234 % 10   # the last digit
4
>>> 1234 // 10  # everything except the last digit
123
```

</details>

---

## 2. Reassignment

Recall that we read assignment statements right to left.

<details class="code-example" markdown="1">
<summary>Live code — <code>x = x + 1</code></summary>

```python
>>> x = 5
>>> print(x)
5
>>> x = x + 1
>>> print(x)
6
```

`x = x + 1` is nonsense as algebra — no number equals itself plus one. It is very common in Python.

Read it right to left, exactly as the machine does it:

1. Work out the right-hand side using the value `x` has **right now**: `5 + 1` is `6`.
2. Point the name `x` at that result.

The old value is used to compute the new one, and then it is gone.

</details>


---

## 3. Putting it together

A common pattern for using `%`, `//` and reassignment involves deconstructing a value piece by piece.

<details class="code-example" markdown="1">
<summary>Live code — <code>seconds.py</code>, stage 1</summary>

A duration in seconds, and we want hours, minutes, seconds.

```python
# seconds.py -- CSCI 131, Friday Sept 4

total = int(input('Total seconds: '))

hours = total // 3600
print('Hours:', hours)
```

```
Total seconds: 3725
Hours: 1
```

`int`, not `float` — this is a count of seconds, and half a second is not a thing we care about here right now.

</details>

<details class="code-example" markdown="1">
<summary>Live code — <code>seconds.py</code>, stage 2</summary>

Now the leftover. This is the line that matters:

```python
total = int(input('Total seconds: '))

hours = total // 3600
total = total % 3600          # <-- keep only what the hours did not use

minutes = total // 60
print('Hours:', hours)
print('Minutes:', minutes)
```

```
Total seconds: 3725
Hours: 1
Minutes: 2
```

`total = total % 3600` is the reassignment; it gives us the piece we didn't count in hours.

</details>

<details class="code-example" markdown="1">
<summary>Live code — the finished <code>seconds.py</code></summary>

```python
total = int(input('Total seconds: '))

hours = total // 3600
total = total % 3600

minutes = total // 60
total = total % 60

print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', total)
```

```
Total seconds: 3725
Hours: 1
Minutes: 2
Seconds: 5
```

Check it against something you know: 3725 = 3600 + 120 + 5. One hour, two minutes, five seconds. Correct.

Try `7384` as well — it should give 2 hours, 3 minutes, 4 seconds. Work that one out on paper first, then run it.

</details>

The shape is always the same:

```
big_unit = amount // size
amount   = amount % size
```

Divide to get the whole units, take the remainder to get what is left, move to the next size down. Our next assignment will use this shape.

---

## 4. Powers

<details class="code-example" markdown="1">
<summary>Live code — <code>**</code></summary>

```python
>>> 2 ** 10
1024
>>> 5 ** 2
25
>>> 2 ** 0.5
1.4142135623730951
```

`**` is exponentiation. 

Remember order of operations (PEMDAS) `**` has priority over `*` and `/`, which have priority over `+` and `-`:

```python
>>> 2 * 3 ** 2
18
>>> (2 * 3) ** 2
36
>>> 3 + 4 ** 2
19
>>> (3 + 4) ** 2
49
```

</details>

---

## 5. String Concatenation


<details class="code-example" markdown="1">
<summary>Live code — string operators</summary>

```python
>>> 'Widener' + 'University'
'WidenerUniversity'
>>> 'Widener' + ' ' + 'University'
'Widener University'
>>> 'ha' * 3
'hahaha'
>>> '-' * 30
'------------------------------'
```

- `+` on two strings does **not** add — it glues them end to end. This is called **concatenation**. It glues *exactly* what you gave it, so if you want a space between two words you have to supply the space yourself.
- `*` on a string and a number repeats it. `'-' * 30` is a very convenient way to draw a line.

</details>


---

## 6. Choosing `int` or `float` on purpose

Ask what the quantity *is*:

- **A count** — people, coins, seconds, pizzas, students. It cannot be fractional. Use `int`.
- **A measurement** — money, temperature, hours worked, a rate. It can be fractional. Use `float`.

<details class="code-example" markdown="1">
<summary>Live code — <code>int</code> truncation</summary>

```python
>>> int(3.99999)
3
>>> int(-2.3)
-2
>>> float(35)
35.0
```

`int` does **not** round. It throws the fractional part away. `int(3.99999)` is `3`, not `4`.

And `int` cannot take a string with a decimal point in it at all:

```python
>>> int('2.75')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '2.75'
```

So if you use `int` on a value the user might reasonably type as `2.75`, your program crashes.

</details>

The `seconds.py` example used `int` throughout, on purpose: `//` and `%` on a whole number of seconds are exactly the right tools, and a float would have given you `1.0` hours instead of `1`.

---

## Before Wednesday

Next class is your **second graded programming assignment**; tt is more demanding than the first one — each problem uses several of today's operators together rather than one at a time.

Test 1 is Friday, September 11 and covers all of Chapters 1 and 2. 
