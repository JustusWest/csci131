---
title: "07 — while Loops"
published: True
---

**Monday, September 28**

**Reading:** *Python for Everybody*, §5.1–5.3


---

## 1. Review
 `if` lets a block of code run sometimes, and when it does run it runs only once.

<details class="code-example" markdown="1">
<summary>Live code — an <code>if</code> runs its block once</summary>

```python
n = 3

if n > 0:
    print(n)
    n = n - 1

print('Done.')
```

```
3
Done.
```

</details>

Python checks `n > 0`, finds it `True`, runs the block, and moves on. After the block runs, `n` is `2` and `n > 0` is **still** `True`.

> **Ask:** what if we wanted to print `3`, `2`, `1`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

With what we've done so far, the only way is to copy and paste the `if` three times. This might work for `3` but it would be unreasonable for `1,000` and won't work at all if the user gets to pick the number.

</details>

We want is an `if` which, after running its block, **goes back and checks the condition again**.

---

## 2. `while` — an `if` that repeats


<details class="code-example" markdown="1">
<summary>Live code — the same program with <code>while</code></summary>

```python
n = 3

while n > 0:
    print(n)
    n = n - 1

print('Done.')
```

```
3
2
1
Done.
```

</details>

All we did was change `if` to `while`. The rest is the same; we have a condition to check, a colon, and an indented block. The difference is what happens after that block. An `if` keeps going to the next line. A `while` goes back up to the condition and checks again.

Here is how Python runs a `while`:

1. Check the condition.
2. If it is `False`, skip the block and carry on with the line after it.
3. If it is `True`, run the block, then **go back to step 1**.

A conditional checks once and runs once. A loop keeps checking and running until the condition becomes `False`.

Some key terms:

- the indented block is the **body** of the loop
- one pass through the body is an **iteration**
- a variable which changes in the body and decides when the loop stops, like `n`, is the **iterator**

---

### `countdown.py`

Let's try it with user input instead of a fixed number.

<details class="code-example" markdown="1">
<summary>Live code — <code>countdown.py</code></summary>

```python
# countdown.py -- CSCI 131, Monday Sept 28

n = int(input('Count down from: '))

while n > 0:
    print(n)
    n = n - 1

print('Done.')
```

```
Count down from: 5
5
4
3
2
1
Done.
```

</details>

*while `n` is more than zero, print `n` and then make it one smaller. When it reaches zero skip.*

Notice `n = n - 1`. That is reassignment: work out the right-hand side using the value `n` has right now, then point the name at the result.

---

## 3. Tracing a loop

When a loop does something you did not expect, the fix is almost always to slow down and trace it by hand. Write down each variable, and each time through, write down its value and whether the condition is `True`.

Here is `countdown.py` on an input of `3`:

| Check | `n` | `n > 0` | What happens |
| ----- | --- | ------- | ------------ |
| 1st | `3` | `True` | print `3`, `n` becomes `2` |
| 2nd | `2` | `True` | print `2`, `n` becomes `1` |
| 3rd | `1` | `True` | print `1`, `n` becomes `0` |
| 4th | `0` | `False` | leave the loop, print `Done` |

Three iterations, but **four** checks. The condition is always checked one more time than the body runs, because the last check is the one which says stop.

> **Ask:** how many times does the body run on an input of `10`? How many times is the condition checked?

<details class="code-example" markdown="1">
<summary>Answer</summary>

The body runs 10 times. The condition is checked 11 times: ten `True`s and then one `False`.

</details>

---

## 4. Three ways a loop goes wrong

### It never runs

<details class="code-example" markdown="1">
<summary>Live code — <code>countdown.py</code> on <code>0</code></summary>

```
Count down from: 0
Done.
```

</details>

The condition is `False` on the very first check, so the body is skipped entirely. This is not an error. A `while` can run zero times, the same way an `if` can.

### It never stops

Remove the line `n = n - 1` and run it.

<details class="code-example" markdown="1">
<summary>Live code — the infinite loop</summary>

```python
n = int(input('Count down from: '))

while n > 0:
    print(n)

print('Blastoff!')
```

```
Count down from: 3
3
3
3
3
3
...
```

</details>

Nothing in the body changes `n`, so `n > 0` is `True` now and will be `True` forever. This is an **infinite loop**.

**To stop a runaway program in IDLE, click in the shell window and press Ctrl+C.** Python stops wherever it is and reports it:

```
Traceback (most recent call last):
  File "countdown.py", line 4, in <module>
    print(n)
KeyboardInterrupt
```


> **Ask:** what happens if the last line of the body is `n = n + 1` instead?

<details class="code-example" markdown="1">
<summary>Answer</summary>

Also an infinite loop. `n` does change, but it moves the wrong way. It gets bigger every time, so `n > 0` never becomes `False`.

The body has to change something the condition looks at, **and** it has to move it toward making the condition `False`.

</details>

### It runs once too many (or too few)

<details class="code-example" markdown="1">
<summary>Live code — <code>&gt;=</code> instead of <code>&gt;</code></summary>

```python
n = int(input('Count down from: '))

while n >= 0:
    print(n)
    n = n - 1

print('Done')
```

```
Count down from: 3
3
2
1
0
Blastoff!
```

</details>

This is not necessarily an error, but depending on the application it might be.

---

## 5. Loops that wait for the user


<details class="code-example" markdown="1">
<summary>Live code — <code>password.py</code></summary>

```python
# password.py

password = input('Password: ')

while password != 'swordfish':
    print('Wrong, try again.')
    password = input('Password: ')

print('Welcome!')
```

```
Password: hello
Wrong, try again.
Password: Swordfish
Wrong, try again.
Password: swordfish
Welcome!
```

```
Password: swordfish
Welcome!
```

</details>

Compare this to `login.py` from last Wednesday. There, one wrong answer ended the program. Here, the program keeps asking for as long as it needs to. It could be one try or fifty.

Look at where `input` appears. It appears **twice**, and both are needed:

- The one **before** the loop gives the condition something to check the first time.
- The one **at the bottom of the body** is the update. It changes what the condition looks at each time.

> **Ask:** what happens if you delete the `input` inside the loop? What if you delete the one before it?

<details class="code-example" markdown="1">
<summary>Answer</summary>

Delete the one inside: if the first password is wrong, nothing ever changes `password`, and it prints `Wrong, try again.` forever.

Delete the one before: the very first check is `password != 'swordfish'`, but `password` has not been given a value yet, so Python stops with a `NameError`. A loop's condition needs its variables to exist **before** the loop starts.

</details>

The same shape checks that input makes sense. This one uses `or` from last Monday:

<details class="code-example" markdown="1">
<summary>Live code — <code>age.py</code></summary>

```python
age = int(input('Age: '))

while age < 0 or age > 120:
    print('That is not a real age.')
    age = int(input('Age: '))

print('Thank you.')
```

```
Age: 200
That is not a real age.
Age: -3
That is not a real age.
Age: 19
Thank you.
```

</details>

When the loop finishes, you **know** the condition is `False`. So every line after the loop can rely on `age` being between 0 and 120.

---

## 6. Putting it together — `total.py`

The user types in a number or types `done` when finished. The program prints the total.

<details class="code-example" markdown="1">
<summary>Live code — stage 1: read until <code>done</code></summary>

Start with the loop alone, and have it just repeat back what it was given.

```python
# total.py -- CSCI 131, Monday Sept 28

line = input('Number (or done): ')

while line != 'done':
    print('You typed', line)
    line = input('Number (or done): ')

print('Finished.')
```

```
Number (or done): 4
You typed 4
Number (or done): 10
You typed 10
Number (or done): 7
You typed 7
Number (or done): done
Finished.
```

</details>

Same shape as `password.py`: take input once before the loop, and again inside the body of the loop. Run this on it's own first to make sure it stops.

Why is there no `float` on the `input`? Try it.

<details class="code-example" markdown="1">
<summary>Live code — converting too early</summary>

```python
num = float(input('Number (or done): '))
```

```
Number (or done): done
Traceback (most recent call last):
  File "total.py", line 1, in <module>
    num = float(input('Number (or done): '))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: 'done'
```

</details>

`'done'` is not a number, so `float` cannot convert it. `input` always gives you a string. **Compare first, convert second.**

<details class="code-example" markdown="1">
<summary>Live code — stage 2: keep a running total</summary>

```python
total = 0
line = input('Number (or done): ')

while line != 'done':
    total = total + float(line)
    line = input('Number (or done): ')

print('Total:', total)
```

```
Number (or done): 4
Number (or done): 10
Number (or done): 7
Number (or done): done
Total: 21.0
```

</details>

`total = total + float(line)` is another example of reassignment. It takes the current value, changes it, and stores it back in the variable. Each iteration adds one more number to the total. Trace it:

| After typing | `line` | `total` |
| ------------ | ------ | ------- |
| (before the loop) | `'4'` | `0` |
| `4` | `'10'` | `4.0` |
| `10` | `'7'` | `14.0` |
| `7` | `'done'` | `21.0` |

> **Ask:** what happens if `total = 0` moves inside the loop, just above `total = total + float(line)`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
Number (or done): 4
Number (or done): 10
Number (or done): 7
Number (or done): done
Total: 7.0
```

The total is reset to zero every iteration, so each number replaces the last one instead of being added to it. Only the final number is left.

A variable which collects something across the loop has to be set up **once, before** the loop starts.

</details>

<details class="code-example" markdown="1">
<summary>Live code — stage 3: count them and average</summary>

```python
total = 0
count = 0
line = input('Number (or done): ')

while line != 'done':
    total = total + float(line)
    count = count + 1
    line = input('Number (or done): ')

print('Count:', count)
print('Total:', total)
print('Average:', total / count)
```

```
Number (or done): 4
Number (or done): 10
Number (or done): 7
Number (or done): done
Count: 3
Total: 21.0
Average: 7.0
```

</details>

`count` is another running variable, but it adds `1` each time instead of the number typed in. It doesn't care what the numbers are, only how many there were.

Now test the boundary. What if the user types `done` straight away?

<details class="code-example" markdown="1">
<summary>Live code — no numbers at all</summary>

```
Number (or done): done
Count: 0
Total: 0
Traceback (most recent call last):
  File "total.py", line 12, in <module>
    print('Average:', total / count)
                      ~~~~~~^~~~~~~
ZeroDivisionError: division by zero
```

</details>

The loop ran zero times, which is fine. But after the loop, `count` is `0`, and you cannot divide by zero.

<details class="code-example" markdown="1">
<summary>Live code — <code>total.py</code>, finished</summary>

```python
# total.py -- CSCI 131, Monday Sept 28

total = 0
count = 0
line = input('Number (or done): ')

while line != 'done':
    total = total + float(line)
    count = count + 1
    line = input('Number (or done): ')

print('Count:', count)
print('Total:', total)

if count > 0:
    print('Average:', total / count)
else:
    print('No numbers entered.')
```

```
Number (or done): 4
Number (or done): 10
Number (or done): 7
Number (or done): done
Count: 3
Total: 21.0
Average: 7.0
```

```
Number (or done): done
Count: 0
Total: 0
No numbers entered.
```

</details>

A loop and a conditional working together: the loop gathers the numbers, and the `if` afterwards decides what can be said about them.

---

## 7. Three loop shapes

```python
n = 5                          # counting loop
while n > 0:
    ...
    n = n - 1                  # the update

value = input('...')           # input loop: ask once before
while value != 'done':
    ...
    value = input('...')       # and again in the body

total = 0                      # running total: set up before
while ...:
    total = total + ...        # add to it inside the body
print(total)                   
```

- `while` is an `if` that goes back and checks again. The condition is checked **before every iteration**, including the first.
- Every variable in the condition must have a value **before** the loop starts.
- The body must change something the condition looks at, in the direction of making it `False`. If it doesn't, you have an infinite loop. Use **Ctrl+C** to stop it.
- Anything that accumulates across the loop is set up **before** the loop, not inside it.
