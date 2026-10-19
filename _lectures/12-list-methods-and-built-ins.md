---
title: "12 — List Methods, Built-ins, split and join"
published: true
---

**Wednesday, October 21**

**Reading:** *Python for Everybody*, `sort` in §8.6, §8.8, §8.9, and the first item of §8.14

---

## 1. Where we left off

Last Wednesday: strings are **immutable**, so a string method can't change the string. It returns a **new** string, and if you want to keep it, you have to assign it.

> **Ask:** what does this print?

```python
word = 'banana'
word.upper()
print(word)
word = word.replace('a', 'o')
print(word)
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
banana
bonono
```

`word.upper()` returned `'BANANA'`, and nobody kept it. The `replace` line kept its result.

</details>

Today is the other column of the table: lists are **mutable**, and that changes how their methods behave. Then we finish with two methods that get you from one column to the other.

---

## 2. List methods change the list

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

Neither line shows anything at the prompt, because there is no value to show: both return `None`, the same *no value* that `print` returns. So what happens if you assign the result, the way you have to with a string method?

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

## 3. `sum`, `max` and `min`

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

`sum` is the summing loop. `max` and `min` are the largest and smallest loops. Python has already written them for you. On Friday's `curve.py` you needed the highest score: `max(scores)` is that loop in one call.

Here is `above.py` from Lecture 09 again. The summing loop is gone, and we get the highest and lowest for free:

<details class="code-example" markdown="1">
<summary>Live code — <code>above.py</code> with the built-ins</summary>

```python
# above.py -- CSCI 131, Wednesday Oct 21

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

## 4. `split`: from a string to a list

So far we have kept the two columns of the table apart. The last two tools go **between** them. `split` is a string method that breaks a string into pieces and returns them as a **list**.

<details class="code-example" markdown="1">
<summary>Live code — splitting a sentence into words</summary>

```python
>>> sentence = 'the quick brown fox'
>>> words = sentence.split()
>>> words
['the', 'quick', 'brown', 'fox']
>>> len(words)
4
>>> words[0]
'the'
>>> words[-1]
'fox'
```

</details>

- With nothing in the parentheses, `split` breaks the string wherever there are spaces, and the spaces are thrown away.
- The result is a list, so everything from Lecture 10 works on it: `len(words)` is a word count, and `words[0]` and `words[-1]` are the first and last words.
- `split` is a string method, so `sentence` is unchanged. It returns a new value (a list this time), and we **assign** it.

Extra spaces don't make empty words:

```python
>>> '  lots   of    space  '.split()
['lots', 'of', 'space']
```

### Splitting on something else

Put a string in the parentheses and `split` breaks the string there instead. This is how you take apart a line of data with commas in it:

<details class="code-example" markdown="1">
<summary>Live code — splitting on commas</summary>

```python
>>> line = '88,92,75'
>>> parts = line.split(',')
>>> parts
['88', '92', '75']
>>> parts[0] + parts[1]
'8892'
```

</details>

Look at the quotes: the pieces are **strings**, not numbers. `split` always gives you strings, so `+` joins them instead of adding them. To do arithmetic, convert each piece with `int` (or `float`), the same as you do with `input`.

<details class="code-example" markdown="1">
<summary>Live code — <code>total.py</code></summary>

```python
# total.py -- CSCI 131, Wednesday Oct 21

line = input('Scores, with commas: ')
parts = line.split(',')

scores = []
for part in parts:
    scores.append(int(part))

print(scores)
print('Average:', sum(scores) / len(scores))
```

```
Scores, with commas: 88,92,75
[88, 92, 75]
Average: 85.0
```

```
Scores, with commas: 70,92,85,64,79
[70, 92, 85, 64, 79]
Average: 78.0
```

</details>

Every piece is used here: `split` from today, a list built with `append` from Unit 3, `int` from Unit 1, and `sum` and `len` from earlier this lecture. Unlike `above.py`, the user types all the scores on one line.

> **Ask:** what happens if the user types a comma at the end, `88,92,75,`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
Scores, with commas: 88,92,75,
Traceback (most recent call last):
  File "total.py", line 8, in <module>
    scores.append(int(part))
ValueError: invalid literal for int() with base 10: ''
```

```python
>>> '88,92,75,'.split(',')
['88', '92', '75', '']
```

There is nothing after the last comma, so the last piece is the **empty string** `''`. `int('')` can't make a number out of nothing.

</details>

---

## 5. `join`: from a list to a string

`join` goes the other way: it takes a list of strings and glues them together into **one string**. It looks backwards, because you call it on the **glue**, and the list goes in the parentheses:

<details class="code-example" markdown="1">
<summary>Live code — <code>join</code></summary>

```python
>>> words = ['the', 'quick', 'brown', 'fox']
>>> ' '.join(words)
'the quick brown fox'
>>> '-'.join(words)
'the-quick-brown-fox'
>>> ', '.join(['Ana', 'Ben', 'Carla'])
'Ana, Ben, Carla'
>>> ''.join(['c', 'a', 't'])
'cat'
```

</details>

- Read `', '.join(names)` as *join the names, with `', '` between each pair*.
- The glue goes **between** the items, not after the last one.
- `''` as the glue means nothing between them, so the items are stuck straight together.
- `join` is a string method (it belongs to the glue), so it **returns a new string**. Assign it if you want to keep it.

Every item in the list has to be a string:

<details class="code-example" markdown="1">
<summary>Live code — joining numbers</summary>

```python
>>> ' '.join([88, 92, 75])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ' '.join([88, 92, 75])
TypeError: sequence item 0: expected str instance, int found
```

</details>

Used together, `split` and `join` swap one separator for another:

```python
>>> '-'.join('610 555 0123'.split())
'610-555-0123'
```

`'610 555 0123'.split()` returns `['610', '555', '0123']`, and `'-'.join(...)` glues those back together with dashes.

> **Ask:** what does each line print?

```python
words = 'red green blue'.split()
print(len(words))
print(words[1])
print('+'.join(words))

nums = '3,1,2'.split(',')
print(nums[0] + nums[1])
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
3
green
red+green+blue
31
```

The last one is `'3' + '1'`: the pieces from `split` are strings, so `+` sticks them together.

</details>

---

## 6. Conclusion

| | string | list |
| - | - | - |
| change one item: `x[0] = ...` | `TypeError`; build a new string instead | works |
| methods | return a new string; **assign** the result | change the list; return `None`; **don't assign** |
| convert | `x.split()` gives a list of strings | `glue.join(x)` gives a string |

```python
name = name.strip()             # string methods: assign the result
word = word.replace(old, new)

nums.append(x)                  # list methods: don't assign
nums.sort()

total = sum(nums)               # built-ins: return a value
highest = max(nums)
lowest = min(nums)
average = sum(nums) / len(nums)

words = sentence.split()        # string -> list, split on spaces
parts = line.split(',')         # split on commas; the pieces are strings
line = ', '.join(names)         # list of strings -> string, glue between
```

- List methods change the list and return `None`. If you assign it, the list is lost.
- String methods are the opposite: they return a new string. If you don't assign it, it's lost.
- `sum`, `max` and `min` are the Unit 3 patterns, already written. `max` and `min` of an empty list are an error.
- `split` turns a string into a list of **strings**. Convert the pieces with `int` or `float` before doing arithmetic.
- `join` is called on the glue: `', '.join(names)`. Every item has to be a string.
