---
title: "09 — Loop Patterns and Building a List"
published: true
---

**Monday, October 5**

**Reading:** *Python for Everybody*, §5.3 (`break`), §5.6, and `append` in §8.6

---

## 1. Loop Structures

There are two common loop structures that we have already worked with in class:

- **counting** loops increment some count each time a condition is met by the value in the sequence
- **summing** loops increment a total by the value in the sequence

Here's an example that uses both.
<details class="code-example" markdown="1">
<summary>Live code — <code>steps.py</code></summary>

```python
# steps.py -- CSCI 131, Monday Oct 5

steps = [8200, 4500, 10300, 6100, 12000, 9800, 3000]

count = 0
for s in steps:
    if s >= 10000:
        count = count + 1

total = 0
for s in steps:
    total = total + s

print('Days over 10,000:', count)
print('Total steps:', total)
print('Average:', total / len(steps))
```

```
Days over 10,000: 2
Total steps: 53900
Average: 7700.0
```

</details>

**Counting** adds `1` each time. **Summing** adds the item itself. 

---

## 2. Searching Loops

Another loop structure is the **searching** loop. Here we check each value against a condition, looking for a single value which satisifies it. In this case, we are looking for the largest number in a list:

<details class="code-example" markdown="1">
<summary>Live code — <code>minmax.py</code>, first try</summary>

```python
# minmax.py -- CSCI 131, Monday Oct 5


nums = [7, 4, 19, 12, 1]
largest = 0
smallest = 0

for num in nums:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print('Largest:', largest)
print('Smallest:', smallest)
```

```
Largest: 19
Smallest: 0
```

</details>

`largest` is right. `smallest` is not because `smallest` starts at `0`, and none of the numbers in the list are less than `0` so it is never replaced.


```python
# minmax.py -- CSCI 131, Monday Oct 5

nums = [1, 4, 19, 12, 3]
largest = nums[0]
smallest = nums[0]

for num in nums:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print('Largest:', largest)
print('Smallest:', smallest)
```

```
Largest: 19
Smallest: 0
```

The fix is to initialize `largest` and `smallest` to the first value in the list, rather than `0`. We have not seend this syntax before, it's called *indexing* a list; `nums[0]` means *the value at index 0 in the list nums*. 

Don't worry too much about it for now, we will pick it up again when we treat `list` more fully.

---

## 4. Searching

Sometimes the question is just *is there one?*

Here is a list of changes to a bank balance: deposits are positive, withdrawals are negative. Was there any withdrawal?

<details class="code-example" markdown="1">
<summary>Live code — <code>search.py</code></summary>

```python
# search.py -- CSCI 131, Monday Oct 5

changes = [120, -40, 75, -15, 200]

found = False
for c in changes:
    print('Checking', c)
    if c < 0:
        found = True

if found:
    print('There was a withdrawal.')
else:
    print('No withdrawals.')
```

```
Checking 120
Checking -40
Checking 75
Checking -15
Checking 200
There was a withdrawal.
```

</details>

`found` is a **flag**: a `bool` that starts `False` and gets flipped to `True` the moment we see what we are looking for. Nothing ever flips it back. After the loop, an `if` reads the flag and reports.

---

## 5. Building a list

Here is a problem none of our patterns can solve:

> Read scores until `done`. Print the average, then **every score above the average**.

Start with an empty list, and use `append` to add an item to the end:

<details class="code-example" markdown="1">
<summary>Live code — <code>append</code> at the prompt</summary>

```python
>>> moves = []
>>> moves
[]
>>> moves.append('rock')
>>> moves
['rock']
>>> moves.append('paper')
>>> moves
['rock', 'paper']
>>> len(moves)
2
```

</details>

The dot is new. `moves.append('rock')` means *append `'rock'` to `moves`*. `append` is a function that belongs to the list, so you write the list's name, a dot, then the function. It changes the list itself, so there is no `moves = ...` on that line.

<details class="code-example" markdown="1">
<summary>Live code — <code>above.py</code></summary>

```python
# above.py -- CSCI 131, Monday Oct 5

scores = []
line = input('Score (or done): ')

while line != 'done':
    scores.append(float(line))
    line = input('Score (or done): ')

total = 0
for score in scores:
    total = total + score

if len(scores) > 0:
    average = total / len(scores)
    print('Average:', average)
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
Above average:
92.0
85.0
79.0
```

```
Score (or done): done
No scores entered.
```

</details>

Three loops, each doing one job:

1. a `while`, because we are waiting for `done`: **build** the list
2. a `for` over the list: **sum** it
3. a `for` over the list again, with an `if`: print the ones above the average

The second pass over the data is the whole reason for the list. Without it, there is nothing to go back to.

---

## 6. Conclusion

```python
count = 0                      # count
for item in a_list:
    if test:
        count = count + 1

total = 0                      # sum
for item in a_list:
    total = total + item

largest = first_value          # largest (or smallest, with <)
for item in the_rest:
    if item > largest:
        largest = item

found = False                  # search
for item in a_list:
    if test:
        found = True

new_list = []                  # build a list
while ...:
    new_list.append(value)
```

- Every pattern has three parts: set up **before** the loop, update **inside**, use **after**.
- The starting value matters. `0` is right for a count or a sum, but wrong for largest or smallest: start those at the first real value.
- A flag starts `False` and is only ever flipped to `True` inside the loop.
- `my_list.append(x)` adds `x` to the end of a list. Build a list when you need to go over the data more than once.

---
