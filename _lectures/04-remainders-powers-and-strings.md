---
title: "04 — Remainders, Powers, and Strings"
---

**Friday, September 4**

**Reading:** *Python for Everybody*, §2.5, §2.7–2.9, and §2.2 again

**Goal for today:** the rest of Chapter 2's operators — everything you need for Wednesday's assignment.

Back in the room, back on the keyboards. Type along.

---

## 0. Where we left off

Two weeks ago you learned the four-step shape — prompt, convert, compute, print — and Monday's assignment was three variations on it. Wednesday we looked at what the machine was doing underneath.

I have been deferring three things since the first day. Today you get all of them, plus the explanation for a bug I showed you on August 28 and refused to explain.

One of them you have already met. In Exercise 4 you evaluated `width//2` with `width = 17` and got `8`. Let us start there.

---

## 1. Two more ways to divide

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
- `//` is **floor division** — divide and throw away the remainder. It answers *"how many whole times does it go in?"*
- `%` is the **modulus** operator — the remainder. It answers *"what is left over?"*

So: 7 divided by 3 is 2, with 1 left over. `//` gives you the 2 and `%` gives you the 1. Between them they say everything about the division, and neither one loses information to a decimal point.

</details>

`%` looks like a curiosity and turns out to be everywhere. Two uses to file away right now:

<details class="code-example" markdown="1">
<summary>Live code — two standard tricks</summary>

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

"Is it even?" and "what is the last digit?" are both remainder questions. You will use the first one constantly once we have conditionals.

</details>

---

## 2. Reassignment: a variable that eats its own value

On August 28 I told you to read every assignment **right to left** and said the habit would pay off later. Later is now.

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

`x = x + 1` is nonsense as algebra — no number equals itself plus one. It is completely routine as Python, because `=` is a command, not a claim.

Read it right to left, exactly as the machine does it:

1. Work out the right-hand side using the value `x` has **right now**: `5 + 1` is `6`.
2. Point the name `x` at that result.

The old value is used to compute the new one, and then it is gone.

</details>

This matters today because it lets you take a quantity apart piece by piece. Pull off the largest chunk, keep what is left, repeat.

---

## 3. Putting those together: the cascade

Here is the pattern that `//`, `%`, and reassignment exist to serve. We build it in stages, running it after each addition.

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

`int`, not `float` — this is a count of seconds, and half a second is not a thing we care about here. And `//`, because one and a bit hours is one hour.

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

`total = total % 3600` is the reassignment from §2 doing real work. After it, `total` no longer means "the whole duration" — it means "the part that did not fit into whole hours." 3725 seconds is one hour with 125 seconds left over, so `total` becomes 125, and 125 // 60 is 2 minutes.

</details>

<details class="code-example" markdown="1">
<summary>Live code — the finished <code>seconds.py</code></summary>

```python
# seconds.py -- CSCI 131, Friday Sept 4
# Dr. West

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

Divide to get the whole units, take the remainder to get what is left, move to the next size down. Wednesday's assignment uses this shape with different numbers, so make sure you can explain — out loud, to the person next to you — why the second line is there.

---

## 4. Powers, and a parenthesis that matters

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

`**` is exponentiation. Note that it is **not** `^` — in Python `^` means something else entirely, and it will not give you an error, it will quietly give you a wrong answer.

`**` binds tighter than `*` and `/`, which bind tighter than `+` and `-`:

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

Look hard at those last two. `3 + 4 ** 2` is `19` and `(3 + 4) ** 2` is `49`. Both run. Neither errors. One of them is the answer you wanted and the other is a **semantic error** — the silent kind from Wednesday.

There is no trick for spotting these. There is only the parenthesis you type because you thought about it, and the sample output you check yourself against.

---

## 5. What `+` really does to text

Time to explain August 28.

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

Now put it beside the numeric version:

<details class="code-example" markdown="1">
<summary>Live code — one operator, two jobs</summary>

```python
>>> 10 + 15
25
>>> '10' + '15'
'1015'
```

Same operator. Different types. Different meaning. Python is not being sloppy — it is paying attention to what kind of thing is on either side of the `+` and choosing accordingly.

And *this* is what happened on August 28:

```python
>>> hours = input('Enter Hours: ')
Enter Hours: 35
>>> rate = input('Enter Rate: ')
Enter Rate: 2.75
>>> print(hours + rate)
352.75
```

`input` handed back two strings. `+` saw two strings and did the string thing. `'35'` glued to `'2.75'` is `'352.75'`, which looks enough like a number to slip past you.

That bug is not Python being weird. It is Python being consistent, applied to data whose type you had not checked.

</details>

---

## 6. Choosing `int` or `float` on purpose

On August 28 the rule was "when unsure, use `float`." That got you through Monday. Now do it deliberately.

Ask what the quantity *is*:

- **A count** — people, coins, seconds, pizzas, students. It cannot be fractional. Use `int`.
- **A measurement** — money, temperature, hours worked, a rate. It can be fractional. Use `float`.

The distinction is not cosmetic, because `int` and `float` behave differently:

<details class="code-example" markdown="1">
<summary>Live code — <code>int</code> chops</summary>

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

So if you use `int` on a value the user might reasonably type as `2.75`, your program crashes on a perfectly sensible input. That is a real bug, not a technicality.

</details>

The `seconds.py` example used `int` throughout, on purpose: `//` and `%` on a whole number of seconds are exactly the right tools, and a float would have given you `1.0` hours instead of `1`.

---

## What you should be able to do now

- [ ] Use `/`, `//`, and `%`, and say what each one answers.
- [ ] Use `%` to test whether a number is even, and to get its last digit.
- [ ] Read `x = x + 1` right to left and explain what it does.
- [ ] Write the cascade — `unit = amount // size` then `amount = amount % size` — and explain why the second line is needed.
- [ ] Use `**`, and know it is not `^`.
- [ ] Predict `3 + 4 ** 2` and `(3 + 4) ** 2`, and say which kind of error the wrong one would be.
- [ ] Say what `+` and `*` do to strings, and explain the `352.75` bug from August 28.
- [ ] Choose `int` or `float` deliberately, and say what `int(3.99999)` gives you.

## Before Wednesday

Wednesday, September 9 is your **second graded programming session**, run exactly like the first: starter files from Canvas, written in the room, submitted before you leave, same resubmission window. It is more demanding than the first one — each problem uses several of today's operators together rather than one at a time.

To be ready:

1. **Read §2.5, §2.7–2.9, and re-read §2.2.**
2. **Do Chapter 2 Exercise 4 again**, now that you have met `//` properly. You should be able to give the value *and type* of all four expressions without running them.
3. **Modify `seconds.py`** so it also reports the number of whole days. One new line before the hours line, and one change to the line after it. If you can do that, you can do Wednesday's first problem.
4. At the prompt, work out what `'5' * 3` does, and then what `5 * 3` does, and be sure you can say why they differ.

Test 1 is Friday, September 11 and covers all of Chapters 1 and 2 — everything from August 26 through Wednesday. Bring questions to the assignment period; I would rather answer them then than have you save them for the test.
