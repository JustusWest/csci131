---
title: "08 — for Loops, Strings, and Lists"
published: true
---

**Wednesday, September 30**

**Reading:** *Python for Everybody*, §5.5, §6.3, §8.1 and §8.3

---

## 1. Review

Last time we wrote loops with `while`.

<details class="code-example" markdown="1">
<summary>Live code — <code>countdown.py</code></summary>

```python
n = int(input('Count down from: '))

while n > 0:
    print(n)
    n = n - 1

print('Done.')
```

```
Count down from: 3
3
2
1
Done.
```

</details>

Every `while` loop we saw had three pieces:

1. give the iterator a value **before** the loop
2. check it in the condition
3. change it in the body

A `for` takes care of all three for us, but we need something for it to loop over.

---

## 2. Lists

A **list** is a sequence of values. You make one by putting values inside square brackets, separated by commas. The values in a list are called **items**.

<details class="code-example" markdown="1">
<summary>Live code — lists at the prompt</summary>

```python
>>> moves = ['rock', 'paper', 'scissors']
>>> moves
['rock', 'paper', 'scissors']
>>> type(moves)
<class 'list'>
>>> nums = [4, 10, 7]
>>> print(nums)
[4, 10, 7]
>>> mixed = ['Widener', 3.5, 42, True]
>>> empty = []
>>> print(empty)
[]
```

</details>

- `list` is a new type, alongside `int`, `float`, `str` and `bool`.
- The items can be any type, and they don't all have to be the same type.
- `[]` is the **empty list**. It has no items at all.
- `print` shows the whole list, brackets and all.

`len` tells you how many items are in a list:

<details class="code-example" markdown="1">
<summary>Live code — <code>len</code></summary>

```python
>>> len(moves)
3
>>> len(mixed)
4
>>> len(empty)
0
```

</details>

There is a lot more that can be done with `lists`, but we will leave that for later. For now, we just create a list and loop over it.

---

## 3. `for` — once for each item

<details class="code-example" markdown="1">
<summary>Live code — <code>friends.py</code></summary>

```python

friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
    print('Happy New Year:', friend)

print('Done!')
```

```
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!
```

</details>

There are two keywords to set up a `for` loop, `for` and `in`. After that, it is the standard colon and indent to indicate the body of the loop.

The basic structure is `for` item `in` list.

Here is how Python runs a `for`:

1. Take the **first** item in the list and point `friend` at it.
2. Run the body.
3. Move to the **next** item, point `friend` at it, and run the body again.
4. When there are no items left, carry on with the line after the loop.

*for each friend in the list `friends`, print Happy New Year and their name.*

`friend` is the iterator, like `n` was in a `while` loop. The difference is that you never write `friend = ...` yourself. The `for` does it for you at the start of every iteration.

| Iteration | `friend` | Prints |
| --------- | -------- | ------ |
| 1st | `'Joseph'` | `Happy New Year: Joseph` |
| 2nd | `'Glenn'` | `Happy New Year: Glenn` |
| 3rd | `'Sally'` | `Happy New Year: Sally` |

Three items, three iterations. The loop stops when it runs out of items.

> **Ask:** what does this print?

```python
for friend in []:
    print('Happy New Year:', friend)

print('Done!')
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
Done!
```

The list is empty, so the body runs zero times. A `for` can run zero times, the same as a `while`.

</details>

The name of the iterator is up to you; `for x in friends:` works just as well. Python doesn't know that `friend` is the singular of `friends`. That is for the person reading the code, so pick names that make the line read like a sentence.

---

## 4. Adding up a list

`total.py` added up numbers the user typed until they entered `done`. If you already have the numbers in a list, use `for`:

<details class="code-example" markdown="1">
<summary>Live code — <code>sum_list.py</code></summary>

```python
# sum_list.py -- CSCI 131, Wednesday Sept 30

nums = [4, 10, 7]
total = 0

for num in nums:
    total = total + num

print('Total:', total)
print('Average:', total / len(nums))
```

```
Total: 21
Average: 7.0
```

</details>

---

## 5. `range` — do something n times

What if you don't have a list, and you just want something to happen 5 times?

<details class="code-example" markdown="1">
<summary>Live code — looping over a number</summary>

```python
for i in 5:
    print('Hello')
```

```
Traceback (most recent call last):
  File "hello.py", line 1, in <module>
    for i in 5:
TypeError: 'int' object is not iterable
```

</details>

`5` is a single number, not a sequence, so there is nothing to step through. *Not iterable* means Python can't loop over it. Lists and strings are iterable; numbers are not.

`range` turns a number into a sequence of numbers.

<details class="code-example" markdown="1">
<summary>Live code — <code>range(n)</code></summary>

```python
for i in range(5):
    print(i)
```

```
0
1
2
3
4
```

</details>

`range(5)` **starts at 0** and **stops before 5**.


To start somewhere other than `0`, give `range` two numbers:

<details class="code-example" markdown="1">
<summary>Live code — <code>range(a, b)</code></summary>

```python
for i in range(1, 6):
    print(i, 'squared is', i ** 2)
```

```
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25
```

</details>

The first number is included, the second is not. `range(1, 6)` is 1, 2, 3, 4, 5. If you want to go up to and including `b`, write `range(a, b + 1)`.

| | Gives | How many |
| - | ----- | -------- |
| `range(5)` | `0, 1, 2, 3, 4` | 5 |
| `range(1, 6)` | `1, 2, 3, 4, 5` | 5 |
| `range(3, 7)` | `3, 4, 5, 6` | 4 |
| `range(5, 1)` | nothing | 0 |

---

## 6. `for` or `while`?

Here is one program written both ways: add up every number from 1 to `n`.

<details class="code-example" markdown="1">
<summary>Live code — <code>sum_to_n.py</code> with <code>while</code></summary>

```python
# sum_to_n.py -- CSCI 131, Wednesday Sept 30

n = int(input('n: '))
total = 0
i = 1

while i <= n:
    total = total + i
    i = i + 1

print('Total:', total)
```

```
n: 10
Total: 55
```

</details>

<details class="code-example" markdown="1">
<summary>Live code — <code>sum_to_n.py</code> with <code>for</code></summary>

```python
n = int(input('n: '))
total = 0

for i in range(1, n + 1):
    total = total + i

print('Total:', total)
```

```
n: 10
Total: 55
```

```
n: 100
Total: 5050
```

</details>

Same answer. The `for` version is two lines shorter because `range(1, n + 1)` does three jobs for us: start `i` at `1`, stop after `n`, and add `1` each time. They do the same thing, but different ways:

- A `for` loop is a **definite** loop. It runs once per item, and the number of items is known before it starts.
- A `while` loop is an **indefinite** loop. It keeps going until the condition is `False`, and you may not know in advance when that will be.

**Rule of thumb:** if you have the list, the string, or the count, use `for`. If you are waiting for something to happen, use `while`.

---


## 7. Looping over a string

A string is also a sequence, a sequence of characters. So `for` works on strings too, one character at a time.

<details class="code-example" markdown="1">
<summary>Live code — <code>for</code> over a string</summary>

```python
word = 'banana'

for ch in word:
    print(ch)
```

```
b
a
n
a
n
a
```

</details>

`ch` (short for character) is the iterator. Each time through the loop it is the next single character in `word`.

`len` works on strings as well:

<details class="code-example" markdown="1">
<summary>Live code — <code>len</code> on a string</summary>

```python
>>> len('banana')
6
>>> len('Widener University')
18
>>> len('')
0
```

</details>

The space counts. It is a character, just like the letters.

### Counting a letter

Now put an `if` inside the loop.

<details class="code-example" markdown="1">
<summary>Live code — <code>count_a.py</code></summary>

```python
# count_a.py -- CSCI 131, Wednesday Sept 30

word = input('Word: ')
count = 0

for ch in word:
    if ch == 'a':
        count = count + 1

print('Number of a:', count)
```

```
Word: banana
Number of a: 3
```

```
Word: Pennsylvania
Number of a: 2
```

</details>

There are two levels of indentation, like the nested `if` from last week. The `if` is inside the `for`, and `count = count + 1` is inside the `if`. The loop looks at every character; the `if` decides which ones get counted.

`count` is the same kind of running variable as in `total.py`: set to `0` **before** the loop and add `1` inside it.

> **Ask:** try `Alabama`. Why does it say `3` and not `4`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
Word: Alabama
Number of a: 3
```

The first letter is a capital `'A'`, and `'A' == 'a'` is `False`.
To count both we can use `or`:

```python
    if ch == 'a' or ch == 'A':
        count = count + 1
```

```
Word: Alabama
Number of a: 4
```

</details>

---

## 8. Conclusion

```python
for item in a_list:            # once for each item
    ...

for ch in a_string:            # once for each character
    ...

for i in range(n):             # 0, 1, ..., n-1  (n times)
    ...

for i in range(a, b):          # a, a+1, ..., b-1
    ...
```

- A **list** is values inside square brackets, separated by commas. `len` gives the number of items. `len` works on strings too.
- A `for` loop runs its body once for each item, pointing the iterator at each one in turn. There is no condition and no update to write, so it can't run forever.
- `range(a, b)` includes `a` and stops **before** `b`.
- Use `for` when you have the collection or the count, and `while` when you are waiting for something to happen.

---

