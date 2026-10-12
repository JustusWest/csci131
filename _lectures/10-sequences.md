---
title: "10 — Sequences: Positions, Slices, and in"
published: true
---

**Monday, October 12**

**Reading:** *Python for Everybody*, §6.1–6.4, §6.7, §8.1 and §8.5

**A change of plan:** the syllabus lists Functions as Unit 4 and lists and strings as Unit 5. We are swapping them, so this unit is lists and strings and Functions comes next.

---

## 1. Indexing

We have already seen indexing, to start the largest-value pattern like this:

<details class="code-example" markdown="1">
<summary>Live code — the first item of a list</summary>

```python
>>> nums = [7, 4, 19, 12, 1]
>>> nums[0]
7
>>> largest = nums[0]
```

</details>

`nums[0]` means *the item at position 0 in `nums`*.

A list is a **sequence**: items in order, each one at a numbered position. A string is also a sequence, of characters. Almost everything works **the same way** on both.

| | string `word = 'banana'` | list `nums = [7, 4, 19, 12, 1]` |
| - | - | - |
| `x[0]` | | |
| `x[-1]` | | |
| `len(x)` | | |
| `x[a:b]` | | |
| `item in x` | | |
| `for item in x` | | |

We will fill in this table as we go.

---

## 2. Indexing — one item by its position

The number inside the square brackets is called the **index**. Positions start at `0`.

```
 b   a   n   a   n   a
 0   1   2   3   4   5
```

<details class="code-example" markdown="1">
<summary>Live code — indexing at the prompt</summary>

```python
>>> word = 'banana'
>>> word[0]
'b'
>>> word[1]
'a'
>>> nums = [7, 4, 19, 12, 1]
>>> nums[0]
7
>>> nums[2]
19
```

</details>

`word[1]` is the **second** letter, not the first. The index is how far you are from the start: the first item is `0` steps away.

### The last item

`'banana'` has 6 letters, at positions `0` to `5`. The last item is always at `len(x) - 1`.

<details class="code-example" markdown="1">
<summary>Live code — one past the end</summary>

```python
>>> len(word)
6
>>> word[5]
'a'
>>> word[len(word) - 1]
'a'
>>> word[6]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    word[6]
IndexError: string index out of range
>>> nums[5]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    nums[5]
IndexError: list index out of range
```

</details>

There is no position `6` in a 6-letter word. `IndexError` means you asked for a position that does not exist. When you see it, the first thing to check is whether you are one past the end.

### Counting from the end

A **negative** index counts backwards from the end. `-1` is the last item, `-2` the one before it, and so on.

```
 b   a   n   a   n   a
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

<details class="code-example" markdown="1">
<summary>Live code — negative indexes</summary>

```python
>>> word[-1]
'a'
>>> word[-6]
'b'
>>> nums[-1]
1
>>> nums[-2]
12
```

</details>

`word[-1]` is a shorter way of writing `word[len(word) - 1]`, and it works no matter how long the word is.

### What is an item?

<details class="code-example" markdown="1">
<summary>Live code — the type of an item</summary>

```python
>>> type(word[0])
<class 'str'>
>>> type(nums[0])
<class 'int'>
```

</details>

- An item of a string is a string with **one character** in it. Python has no separate type for a single character.
- An item of a list is **whatever was stored there**: an `int`, a `float`, a `str`, and so on.

The index doesn't have to be a number you type in. Any expression that gives an `int` works, including a variable: `word[i]`, `word[i + 1]`.

---

## 3. Slicing — several items at once

A **slice** gives you a piece of a sequence. `x[a:b]` follows the same rule as `range(a, b)`: it **includes** position `a` and **stops before** position `b`.

<details class="code-example" markdown="1">
<summary>Live code — slices</summary>

```python
>>> word[0:3]
'ban'
>>> word[2:5]
'nan'
>>> nums[1:3]
[4, 19]
```

</details>

`word[2:5]` is positions `2`, `3` and `4`: three items, because `5 - 2` is `3`.

### Leaving off an end

Leave off the first number and the slice starts at the beginning. Leave off the second and it goes to the end.

<details class="code-example" markdown="1">
<summary>Live code — open-ended slices</summary>

```python
>>> word[:3]
'ban'
>>> word[3:]
'ana'
>>> word[-3:]
'ana'
>>> nums[:2]
[7, 4]
>>> nums[-2:]
[12, 1]
```

</details>

`x[:3]` is *the first three*, and `x[-3:]` is *the last three*. Those two are worth remembering.

### A slice has the same type as what you sliced

<details class="code-example" markdown="1">
<summary>Live code — an index vs. a slice</summary>

```python
>>> nums[0]
7
>>> nums[0:1]
[7]
```

</details>

An index gives you **one item**. A slice gives you **a smaller sequence of the same type**: a slice of a string is a string, and a slice of a list is a list, even if there is only one item in it.

### Slices are forgiving; indexes are not

<details class="code-example" markdown="1">
<summary>Live code — slicing past the end</summary>

```python
>>> word[3:100]
'ana'
>>> word[10:20]
''
>>> nums[10:20]
[]
```

</details>

A slice that runs off the end just stops at the end, and a slice with nothing in it gives you an empty string or an empty list. `word[100]` would be an `IndexError`, but `word[3:100]` is fine.

> **Ask:** what do these give?

```python
word[1:4]
nums[-3:]
word[5:6]
word[6:7]
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```python
>>> word[1:4]
'ana'
>>> nums[-3:]
[19, 12, 1]
>>> word[5:6]
'a'
>>> word[6:7]
''
```

`word[6:7]` starts past the end, so there is nothing in it. As a slice, that's an empty string, not an error.

</details>

---

## 4. `in` — is it in there?

`in` asks *does this sequence contain that?* The answer is a `bool`.

<details class="code-example" markdown="1">
<summary>Live code — <code>in</code> on a string</summary>

```python
>>> 'a' in 'banana'
True
>>> 'z' in 'banana'
False
>>> 'nan' in 'banana'
True
>>> 'bnn' in 'banana'
False
```

</details>

On a string, `in` finds any **substring**: one character, or several characters **in a row**. `'bnn'` is not in `'banana'`, because those letters never appear next to each other.

<details class="code-example" markdown="1">
<summary>Live code — <code>in</code> on a list</summary>

```python
>>> 19 in nums
True
>>> 5 in nums
False
>>> roster = ['Ana', 'Falilou', 'Khailah', 'Jadon', 'Afia', 'Tyson']
>>> 'Ana' in roster
True
>>> 'An' in roster
False
```

</details>

On a list, `in` matches **whole items only**. `'An'` is part of `'Ana'`, but it is not an item of the list.

This is the first row of the table where the two columns are a little different.

### The search pattern, already written

Here is `roster.py` from Assignment 6, using the search pattern from Lecture 09:

```python
found = False
for student in roster:
    if student == name:
        found = True

if found:
    print(name, 'is on the roster.')
```

`in` does that whole loop for you:

<details class="code-example" markdown="1">
<summary>Live code — <code>roster.py</code> with <code>in</code></summary>

```python
# roster.py -- CSCI 131, Monday Oct 12

roster = ['Ana', 'Falilou', 'Khailah', 'Jadon', 'Afia', 'Tyson']
name = input('Name: ')

if name in roster:
    print(name, 'is on the roster.')
else:
    print(name, 'is not on the roster.')
```

```
Name: Afia
Afia is on the roster.
```

```
Name: Zoe
Zoe is not on the roster.
```

</details>

---

## 5. Looping over positions

`for ch in word` gives you each **item**, but it never tells you **where** that item is. Sometimes the position is the thing you need.

The book (§6.3) walks through a string with a `while` loop and an index. This is the counter loop from Unit 3, with an index added:

<details class="code-example" markdown="1">
<summary>Live code — <code>while</code> with an index</summary>

```python
word = 'banana'
index = 0

while index < len(word):
    letter = word[index]
    print(index, letter)
    index = index + 1
```

```
0 b
1 a
2 n
3 a
4 n
5 a
```

</details>

The condition is `index < len(word)`, not `<=`. With `<=`, `index` would reach `6`, and `word[6]` is an `IndexError`.

In Lecture 08 we rewrote `sum_to_n.py` from a `while` into a `for` with `range`. The same move works here. `range(len(word))` is `range(6)`, which is `0, 1, 2, 3, 4, 5`: exactly the positions in `word`.

<details class="code-example" markdown="1">
<summary>Live code — the same loop with <code>for</code></summary>

```python
word = 'banana'

for i in range(len(word)):
    print(i, word[i])
```

```
0 b
1 a
2 n
3 a
4 n
5 a
```

</details>

`i` is the position and `word[i]` is the item at that position. Using `i` as the name is convention (*i* for *index*).

### Where is it?

<details class="code-example" markdown="1">
<summary>Live code — <code>where.py</code></summary>

```python
# where.py -- CSCI 131, Monday Oct 12

word = 'banana'

for i in range(len(word)):
    if word[i] == 'a':
        print('a at position', i)
```

```
a at position 1
a at position 3
a at position 5
```

</details>

`for ch in word` could count the `a`s, but it could not say *where* they are.

**Rule of thumb:** if you only need *what* the items are, use `for item in x`. If you need *where* they are, use `for i in range(len(x))` and get each item with `x[i]`.

---

## 6. Neighbours

With positions, you can compare an item with the one **next to it**. Here are the daily highs from Assignment 6. How many days were warmer than the day before?

<details class="code-example" markdown="1">
<summary>Live code — <code>warmer.py</code>, first try</summary>

```python
# warmer.py -- CSCI 131, Monday Oct 12

highs = [78, 84, 81, 69, 90, 88, 75, 31, 45, 82, 79, 93, 66, 58]
count = 0

for i in range(len(highs)):
    if highs[i + 1] > highs[i]:
        count = count + 1

print('Warmer than the day before:', count)
```

```
Traceback (most recent call last):
  File "warmer.py", line 7, in <module>
    if highs[i + 1] > highs[i]:
IndexError: list index out of range
```

</details>

> **Ask:** there are 14 days, at positions `0` to `13`. What is `i` when it crashes?

<details class="code-example" markdown="1">
<summary>Answer</summary>

On the last time through, `i` is `13`, so `highs[i + 1]` is `highs[14]`, and there is no position `14`.

The last day has no day after it, so there is nothing to compare it to. The loop should stop one position early:

```python
for i in range(len(highs) - 1):
    if highs[i + 1] > highs[i]:
        count = count + 1
```

```
Warmer than the day before: 5
```

</details>

Whenever you write `x[i + 1]`, check what happens on the last `i`.

---

## 7. Conclusion

| | string `word = 'banana'` | list `nums = [7, 4, 19, 12, 1]` |
| - | - | - |
| `x[0]` | `'b'` | `7` |
| `x[-1]` | `'a'` | `1` |
| `len(x)` | `6` | `5` |
| `x[1:3]` | `'an'` (a string) | `[4, 19]` (a list) |
| `item in x` | any substring: `'nan' in word` | whole items only: `19 in nums` |
| `for item in x` | each character | each item |

```python
x[0]                           # the first item
x[-1]                          # the last item
x[len(x) - 1]                  # also the last item
x[a:b]                         # positions a, a+1, ..., b-1
x[:3]                          # the first three
x[-3:]                         # the last three
item in x                      # True or False

for item in x:                 # when you need what
    ...

for i in range(len(x)):        # when you need where
    ... x[i] ...

for i in range(len(x) - 1):    # when you compare x[i] with x[i + 1]
    ...
```

- Strings and lists are both **sequences**. Positions start at `0`, and the last one is `len(x) - 1`, or `-1`.
- An index past the end is an `IndexError`. A slice past the end just stops at the end.
- An index gives you one item. A slice gives you a sequence of the same type.
- `in` on a string matches any substring. `in` on a list matches whole items only.
- Loop over `range(len(x))` when you need the position. Stop at `len(x) - 1` when you look at the next item.

---
