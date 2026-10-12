---
title: "11 — Changing Sequences: Methods and Return Values"
published: true
---

**Wednesday, October 14**

**Reading:** *Python for Everybody*, §6.5, §6.9, §8.2, `sort` in §8.6, §8.8, and the first item of §8.14

---

## 1. List vs String Difference

Last time, we said the lists and string are both sequences, so *almost* everything works the same. Here is the case where they don't:

<details class="code-example" markdown="1">
<summary>Live code — changing an item of a list</summary>

```python
>>> nums = [7, 4, 19, 12, 1]
>>> nums[0] = 99
>>> nums
[99, 4, 19, 12, 1]
```

</details>

An index on the **left** of `=` is an assignment to the sequence. It means *put this value at that position*. The list now holds `99` where the `7` used to be.

<details class="code-example" markdown="1">
<summary>Live code — changing a character of a string</summary>

```python
>>> greeting = 'Hello'
>>> greeting[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
```

</details>

- A list is **mutable**: you can change its items after it is made.
- A string is **immutable**: once it is made, it can never be changed.

To get `'Jello'`, make a **new** string out of the pieces you want, and point the name at it:

<details class="code-example" markdown="1">
<summary>Live code — building a new string</summary>

```python
>>> greeting = 'J' + greeting[1:]
>>> greeting
'Jello'
```

</details>

`greeting[1:]` is `'ello'`, a slice from Monday, and `+` joins two strings, from Unit 1. The old `'Hello'` was never changed. `greeting` now names a different string.

---

## 2. Changing every item in a list

Add 5 points to every score in a list. Here is the first thing most people try:

<details class="code-example" markdown="1">
<summary>Live code — <code>bonus.py</code>, first try</summary>

```python
# bonus.py -- CSCI 131, Wednesday Oct 14

scores = [70, 92, 85, 64, 79]

for score in scores:
    score = score + 5

print(scores)
```

```
[70, 92, 85, 64, 79]
```

</details>

No error, and nothing changed. `score` is a copy the `for` makes of each item in turn. `score = score + 5` adds to a **new** number. The list doesn't know about the name `score`, so it still holds the old numbers.

To change what is **in the list**, you have to say which position to change, so loop over positions:

<details class="code-example" markdown="1">
<summary>Live code — <code>bonus.py</code>, working</summary>

```python
scores = [70, 92, 85, 64, 79]

for i in range(len(scores)):
    scores[i] = scores[i] + 5

print(scores)
```

```
[75, 97, 90, 69, 84]
```

</details>

Read `scores[i] = scores[i] + 5` as: *take the item at position `i`, add 5, and put the result back at position `i`*.

This is the third reason to loop over positions, after *where is it?* and *what's next to it?*: **changing the item**.

---

## 3. Return values

When we use a keyword followed by parentheses, it is a *function call*. Lots of things that we have used so far are function calls, such as:
- `input()`
- `print()`
- `range()` 

When Python runs a function call, the call evaluates to **the value it returns**.

```python
total = len('banana') + 1
total = 6 + 1                  # len('banana') returns 6
total = 7
```

```python
age = int(input('Age: '))      # the user types 19
age = int('19')                # input returns the string '19'
age = 19                       # int returns the number 19
```

`input` returns a `str`. `len` returns an `int`. `int` and `float` return numbers. That value is what you store, print, or use in the rest of the expression. In Unit 5 you will write your own functions, and you will decide what they return.

Some functions don't have anything useful to return. They return a special value called `None`, which means *no value*.

<details class="code-example" markdown="1">
<summary>Live code — what does <code>print</code> return?</summary>

```python
>>> x = print('hi')
hi
>>> print(x)
None
>>> type(x)
<class 'NoneType'>
```

</details>

`print` does its job (putting `hi` on the screen), then returns `None`. Keep `None` in mind; it comes back in section 5.

---

## 4. String methods

In Lecture 09 we wrote `scores.append(x)`: a value, a dot, and a function that belongs to that value. A function like that is called a **method**. Methods are functions that only work on specific data types. `append` only works on lists, for example. Strings have methods too.

<details class="code-example" markdown="1">
<summary>Live code — <code>upper</code>, <code>lower</code> and <code>strip</code></summary>

```python
>>> word = 'banana'
>>> word.upper()
'BANANA'
>>> 'Ana Lopez'.lower()
'ana lopez'
>>> '  Ana Lopez  '.strip()
'Ana Lopez'
```

</details>

- `upper()` and `lower()` change every letter to capitals, or to lower case.
- `strip()` removes spaces from **both ends**. The space in the middle stays.
- The parentheses are required, even when there is nothing inside them.

<details class="code-example" markdown="1">
<summary>Live code — <code>replace</code> and <code>find</code></summary>

```python
>>> word.replace('a', 'o')
'bonono'
>>> '610-555-0123'.replace('-', '')
'6105550123'
>>> word.find('n')
2
>>> word.find('nan')
2
>>> word.find('z')
-1
```

</details>

- `replace(old, new)` replaces **every** `old` with `new`. Replacing with `''` deletes.
- `find(text)` returns the position where `text` **first** appears. If it isn't there, `find` returns `-1`. That is not an error, so your program keeps going.

### The original doesn't change

Strings are immutable, so a string method **can't** change the string. Each one returns a **new** string instead.

<details class="code-example" markdown="1">
<summary>Live code — the original after <code>upper</code></summary>

```python
>>> word = 'banana'
>>> word.upper()
'BANANA'
>>> word
'banana'
```

</details>

At the prompt, Python shows you the value that came back, so it looks like something happened. In a program, nothing shows it to you:

<details class="code-example" markdown="1">
<summary>Live code — <code>answer.py</code>, first try</summary>

```python
# answer.py -- CSCI 131, Wednesday Oct 14

answer = input('Keep going? ')
answer.strip()
answer.lower()
print('[' + answer + ']')

if answer == 'yes':
    print('OK, keep going.')
else:
    print('Stopping.')
```

```
Keep going?   YES 
[  YES ]
Stopping.
```

</details>

`answer.strip()` returned a new, cleaned-up string, and the program threw it away. The square brackets show that `answer` still has its spaces and capitals. To keep the result, **assign it**:

<details class="code-example" markdown="1">
<summary>Live code — <code>answer.py</code>, working</summary>

```python
answer = input('Keep going? ')
answer = answer.strip()
answer = answer.lower()
print('[' + answer + ']')

if answer == 'yes':
    print('OK, keep going.')
else:
    print('Stopping.')
```

```
Keep going?   YES 
[yes]
OK, keep going.
```

</details>

Those two lines can be one:

```python
answer = answer.strip().lower()
```

`answer.strip()` is replaced by the string it returns, and then `.lower()` is called on **that** string. This is the usual way to clean up what a user types before you compare it to anything.

---

## 5. List methods change the list

Lists are mutable, so list methods work the other way round: they **change the list** and return `None`. You already know `append`. The other one we need is `sort`.

<details class="code-example" markdown="1">
<summary>Live code — <code>append</code> and <code>sort</code></summary>

```python
>>> nums = [7, 4, 19, 12, 1]
>>> nums.append(5)
>>> nums
[7, 4, 19, 12, 1, 5]
>>> nums.sort()
>>> nums
[1, 4, 5, 7, 12, 19]
```

</details>

Neither line shows anything at the prompt, because there is no value to show: both return `None`. So what happens if you assign the result, the way you have to with a string method?

<details class="code-example" markdown="1">
<summary>Live code — assigning the result of <code>sort</code></summary>

```python
>>> nums = [7, 4, 19, 12, 1]
>>> nums = nums.sort()
>>> print(nums)
None
```

</details>

`nums.sort()` sorted the list, then returned `None`, and `nums = ` pointed the name at that `None`. The sorted list is gone. This is one of the most common bugs in Python.

| string methods | list methods |
| - | - |
| `upper`, `lower`, `strip`, `replace`, `find` | `append`, `sort` |
| return a **new value** | **change the list** |
| the original is unchanged | return `None` |
| **assign it:** `name = name.strip()` | **don't assign it:** `nums.sort()` |

> **Ask:** what does each of these print?

```python
name = 'ana'
name.upper()
print(name)

nums = [3, 1, 2]
nums.sort()
print(nums)

nums = [3, 1, 2]
nums = nums.sort()
print(nums)
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
ana
[1, 2, 3]
None
```

The first one returned `'ANA'`, but nobody kept it. The third one kept the return value, which was `None`.

</details>

---

## 6. `sum`, `max` and `min`

Python has built-in functions for three of the Unit 3 loop patterns. Like `len`, they are not methods: there is no dot, and the list goes inside the parentheses. They **return** a value.

<details class="code-example" markdown="1">
<summary>Live code — the built-ins</summary>

```python
>>> nums = [7, 4, 19, 12, 1]
>>> sum(nums)
43
>>> max(nums)
19
>>> min(nums)
1
>>> sum(nums) / len(nums)
8.6
```

</details>

`sum` is the summing loop. `max` and `min` are the largest and smallest loops. Python has already written them for you.

Here is `above.py` from Lecture 09 again. The summing loop is gone, and we get the highest and lowest for free:

<details class="code-example" markdown="1">
<summary>Live code — <code>above.py</code> with the built-ins</summary>

```python
# above.py -- CSCI 131, Wednesday Oct 14

scores = []
line = input('Score (or done): ')

while line != 'done':
    scores.append(float(line))
    line = input('Score (or done): ')

if len(scores) > 0:
    average = sum(scores) / len(scores)
    print('Average:', average)
    print('Highest:', max(scores))
    print('Lowest:', min(scores))
    print('Above average:')
    for score in scores:
        if score > average:
            print(score)
else:
    print('No scores entered.')
```

```
Score (or done): 70
Score (or done): 92
Score (or done): 85
Score (or done): 64
Score (or done): 79
Score (or done): done
Average: 78.0
Highest: 92.0
Lowest: 64.0
Above average:
92.0
85.0
79.0
```

</details>

The `if len(scores) > 0` guard is still needed. An empty list has no largest item:

<details class="code-example" markdown="1">
<summary>Live code — <code>max</code> of an empty list</summary>

```python
>>> max([])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    max([])
ValueError: max() iterable argument is empty
```

</details>

You may use `sum`, `max` and `min` on assignments and tests unless a problem says otherwise. They don't replace the loop patterns, though: there is no built-in that counts the scores over 90, adds up only the positive numbers, or tells you *where* the largest one is. The last loop in `above.py` is still a loop.

---

## 7. Conclusion

| | string | list |
| - | - | - |
| change one item: `x[0] = ...` | `TypeError`; build a new string instead | works |
| methods | return a new string; **assign** the result | change the list; return `None`; **don't assign** |

```python
nums[i] = value                 # put value at position i (lists only)
word = 'J' + word[1:]           # "change" a string by building a new one

for i in range(len(nums)):      # change every item in a list
    nums[i] = nums[i] + 5

name = name.strip()             # string methods: assign the result
line = line.strip().lower()     # clean up input
word.replace(old, new)          # returns a new string
word.find(text)                 # returns a position, or -1

nums.append(x)                  # list methods: don't assign
nums.sort()

total = sum(nums)               # built-ins: return a value
highest = max(nums)
lowest = min(nums)
```

- A list is **mutable** and a string is **immutable**.
- `for item in x: item = ...` does **not** change the list. Loop over positions and assign to `x[i]`.
- A call is replaced by the value it **returns**. Functions with nothing to return give back `None`.
- String methods return a new string. If you don't assign it, it's lost.
- List methods change the list and return `None`. If you assign it, the list is lost.
- `sum`, `max` and `min` are the Unit 3 patterns, already written. `max` and `min` of an empty list are an error.


---
