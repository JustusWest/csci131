---
title: "15 — Return Values"
published: true
---

**Monday, November 2**

**Reading:** *Python for Everybody*, §4.10–4.11

---

## 1. From last time

Last time you wrote `count_letter`. Here is one version of it:

<details class="code-example" markdown="1">
<summary>Live code — <code>letters.py</code>, from PA9</summary>

```python
# letters.py -- CSCI 131, Monday Nov 2

def count_letter(word, letter):
    count = 0
    for ch in word:
        if ch == letter:
            count = count + 1
    print(letter, 'appears', count, 'times in', word)

count_letter('banana', 'a')
```

```
a appears 3 times in banana
```

</details>

It works. Now suppose the program needs the **count** itself, not a sentence about it, so it can add to it or compare it to something. A call evaluates to it's return value, so store the value:

> **Ask:** what does this print?

```python
n = count_letter('banana', 'a')
print(n)
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
a appears 3 times in banana
None
```

The first line is the `print` inside the function, which runs as part of the call. The second line is `n`, and `n` is `None`.

</details>

Try to use it as a number and it fails:

<details class="code-example" markdown="1">
<summary>Live code — using the "count"</summary>

```python
>>> n + 1
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    n + 1
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

</details>

`count_letter` worked out the `3` and then **printed** it. When the function finishes, the call is replaced by `None`.


---

## 2. `return`

`return` ends the function and hands a value back to the line that called it. Here is the book's first example:

<details class="code-example" markdown="1">
<summary>Live code — <code>addtwo</code></summary>

```python
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)
```

```
8
```

</details>

`addtwo(3, 5)` starts with `a = 3` and `b = 5`, works out `added = 8`, and returns `8`. The call is replaced by `8`, so `x = 8`.

Now one that is handed a list:

<details class="code-example" markdown="1">
<summary>Live code — <code>average.py</code></summary>

```python
# average.py -- CSCI 131, Monday Nov 2

def average(nums):
    return sum(nums) / len(nums)

scores = [88, 92, 75]
avg = average(scores)
print(avg)
```

```
85.0
```

</details>

`return` can be followed by any expression, so there is no need to make a variable first. Python works out `sum(nums) / len(nums)`, which is `255 / 3`, and returns `85.0`.

> A function call evaluates to the value it **returns**. If the function has no `return`, that value is `None`.

```python
avg = average([88, 92, 75])
avg = 85.0                     # average returned 85.0
```

### Using the returned value

Because the function call becomes a value, you can put it anywhere you could have typed a value (like `85.0`):

<details class="code-example" markdown="1">
<summary>Live code — <code>average.py</code>, using the value</summary>

```python
# average.py -- CSCI 131, Monday Nov 2

def average(nums):
    return sum(nums) / len(nums)

scores = [88, 92, 75]
print('Average:', average(scores))
print('With a 5 point curve:', average(scores) + 5)

if average(scores) > 80:
    print('Honor roll')
```

```
Average: 85.0
With a 5 point curve: 90.0
Honor roll
```

</details>

---

## 3. Two kinds of function

The book calls a function that returns a value **fruitful**, and one that doesn't **void**.

| | **fruitful** | **void** |
| - | - | - |
| examples | `len`, `max`, `input`, `average` | `print`, `banner`, `show_list`, Friday's `count_letter` |
| what it does | works out a value and **returns** it | does a job, like printing |
| returns | the value | `None` |
| how you call it | store it, print it, or use it in an expression | on a line by itself |

Every function we wrote last week was void, and that was fine: their job was printing. But a function that returns is more useful, because the program decides what to do with the answer. It can print it, compare it, add to it, or hand it to another function. A function that prints has already decided.

A good rule of thumb: **functions should return; the main program prints.**

### A function that returns a string

`return` can hand back any kind of value. This one builds a string, using indexing and `upper` from Unit 4:

<details class="code-example" markdown="1">
<summary>Live code — <code>initials</code></summary>

```python
def initials(first, last):
    return first[0].upper() + '.' + last[0].upper() + '.'

print(initials('michael', 'west'))
print(initials('Ada', 'lovelace'))
```

```
M.W.
A.L.
```
</details>
---

## 4. `return` ends the function

As soon as Python reaches a `return`, the function is over. Python goes back to the call with the value, and the rest of the body is skipped.

That makes `return` a good fit for an `if`/`elif` chain from Unit 2:

<details class="code-example" markdown="1">
<summary>Live code — <code>grade.py</code></summary>

```python
# grade.py -- CSCI 131, Monday Nov 2

def letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(letter_grade(95))
print(letter_grade(72))
print(letter_grade(59))
```

```
A
C
F
```

</details>

`letter_grade(72)` checks `72 >= 90`, then `72 >= 80`, then `72 >= 70`, which is `True`, so it returns `'C'`. Every branch has its own `return`, and only one of them runs.

### Code after a `return` never runs

> **Ask:** what does this print?

```python
def average(nums):
    return sum(nums) / len(nums)
    print('Done averaging')

print(average([88, 92, 75]))
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
85.0
```

`Done averaging` is never printed. The function ended at the `return`, so the line under it never runs. There is no error, either: Python doesn't warn you. If a line you wrote never seems to run, check for a `return` above it.

</details>

---

## 5. Variables inside a function

Here is `average` again, this time with a variable inside it:

<details class="code-example" markdown="1">
<summary>Live code — <code>average.py</code>, with <code>total</code></summary>

```python
# average.py -- CSCI 131, Monday Nov 2

def average(nums):
    total = sum(nums)
    return total / len(nums)

avg = average([88, 92, 75])
print(avg)
print(total)
```

```
85.0
Traceback (most recent call last):
  File "average.py", line 9, in <module>
    print(total)
NameError: name 'total' is not defined
```

</details>

`total` was made inside `average`. Variables made inside a function, **including its parameters**, are **local**: they exist only while the function is running. When the function returns, they are gone.


So there is one way into a function and one way out:

> **In through parameters, out through `return`.**

(A function *can* read a variable from the main program, but don't rely on it. In this course, everything a function uses comes in through its parameters.)

---

## 6. Conclusion

| word | meaning | example |
| - | - | - |
| **`return`** | ends the function and hands a value back to the call | `return sum(nums) / len(nums)` |
| **return value** | the value a call is replaced by | `85.0`, from `average([88, 92, 75])` |
| **fruitful function** | returns a value | `len`, `average`, `initials` |
| **void function** | does a job and returns `None` | `print`, `banner`, `show_list` |
| **`None`** | *no value*: what a function with no `return` gives back | `x = print('hi')` |
| **local variable** | made inside a function; gone when it returns | `total` in `average` |

```python
def average(nums):                  # returns a number
    return sum(nums) / len(nums)

def initials(first, last):          # returns a string
    return first[0].upper() + '.' + last[0].upper() + '.'

def letter_grade(score):            # a return in each branch
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    else:
        return 'C'

avg = average([88, 92, 75])         # avg = 85.0
print('Average:', avg)              # the main program prints
if average([88, 92, 75]) > 80:      # a call can go anywhere a value can
    print('Honor roll')
```

- `print` shows a value to a person. `return` hands it back to the program.
- A call is replaced by the value it returns. If the function has no `return`, that value is `None`.
- If a function only prints, `x = f(...)` makes `x` equal to `None`. It is the same bug as `nums = nums.sort()`.
- `return` ends the function. Code after it never runs.
- Variables made inside a function, parameters included, are gone when it returns. **In through parameters, out through `return`.**
- Functions return; the main program prints.

---

## 7. Exercise — `letters.py`

Work on this on your own for the rest of the period. It isn't submitted.

Change `count_letter(word, letter)` so that it **returns** the count instead of printing a sentence. The sentence moves to the main program. Under the function, test it with these lines:

```python
print(count_letter('banana', 'a'))
print(count_letter('Mississippi', 's'))
print(count_letter('Banana', 'b'))

n = count_letter('banana', 'n')
print('n appears', n, 'times in banana')
print(n + 1)
```

```
3
4
0
n appears 2 times in banana
3
```

If you see a sentence followed by `None`, your function is still printing.

**If you finish:** change the program so it asks for a word and a letter, then prints the sentence. When the count is `1`, say `time`, not `times`. The function doesn't change at all; only the main program does.

```
Word: Widener
Letter: W
W appears 1 time in Widener
```

```
Word: banana
Letter: a
a appears 3 times in banana
```

<details class="code-example" markdown="1">
<summary>Solution</summary>

```python
# letters.py -- CSCI 131, Monday Nov 2

def count_letter(word, letter):
    count = 0
    for ch in word:
        if ch == letter:
            count = count + 1
    return count

print(count_letter('banana', 'a'))
print(count_letter('Mississippi', 's'))
print(count_letter('Banana', 'b'))

n = count_letter('banana', 'n')
print('n appears', n, 'times in banana')
print(n + 1)

word = input('Word: ')
letter = input('Letter: ')
n = count_letter(word, letter)

if n == 1:
    print(letter, 'appears', n, 'time in', word)
else:
    print(letter, 'appears', n, 'times in', word)
```

Only the last line of the function changed: `print(...)` became `return count`. Make sure it lines up with the `for`. Indented under the `for`, it returns after the first letter, so `count_letter('banana', 'a')` gives `0`.


</details>
