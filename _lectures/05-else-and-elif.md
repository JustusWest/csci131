---
title: "05 — else and elif"
published: true
---

**Wednesday, September 16**

**Reading:** *Python for Everybody*, §3.3–3.5

---

## 1. `if` statements

Last time we introduced a fourth data type, `bool`, which is either `True` or `False`. 

We also looked at the six comparison operators, which evaluate to a `bool`:

| Operator | Question it asks |
| -------- | ---------------- |
| `==`     | are these equal? |
| `!=`     | are these different? |
| `<`      | is the left one smaller? |
| `>`      | is the left one bigger? |
| `<=`     | smaller or equal? |
| `>=`     | bigger or equal? |

<details class="code-example" markdown="1">
<summary>Live code — basic <code>if</code></summary>

```python
num = int(input('Num: '))

if num >= 10:
    print('Double digit')

print('Done.')
```

```
Num: 15
Double digit
Done.
```

```
Num: 8
Done.
```

</details>

`if` gives us a piece of code which **sometimes runs**. 

---

## 2. `else`

`else` let's us run some code only when the first block doesn't run

1. `else` has **no condition**. It is not `else num < 10:`. There is nothing to ask — `else` means *every case the `if` did not take*.
2. `else` still gets a **colon**, and its body is still **indented**.
3. `else` must sit at the same indentation as its `if`, and there must be an `if` above it.

The important property is that **exactly one of the two branches runs.**


<details class="code-example" markdown="1">
<summary>Live code — <code>digits.py</code></summary>

```python
# digits.py -- CSCI 131, Wednesday Sept 16

num = int(input('Num: '))

if num >= 10:
    print('Double digit')
else:
    print('Single digit')

print('Done.')
```

```
Num: 15
Double digit
Done.
```

```
Num: 8
Single digit
Done.
```

</details>




---

### Even or odd

Recall the `%` operator - it give the remainder of dividing the two numbers.

Using `num % 2` we can test if a number is even or odd.

<details class="code-example" markdown="1">
<summary>Live code — <code>evenodd.py</code></summary>

```python
# evenodd.py

num = int(input('Enter a number: '))

if num % 2 == 0:
    print(num, 'is even')
else:
    print(num, 'is odd')
```

```
Enter a number: 18
18 is even
```

```
Enter a number: 7
7 is odd
```

</details>

the expression `num % 2 == 0` has two parts:

- `num % 2` is arithmetic. It produces a number — `0` or `1`.
- `== 0` is a comparison. It takes that number and produces a `bool`.

`%` happens first, and then `==` compares the result. So on `18`: `18 % 2` is `0`, then `0 == 0` is `True`, so the `if` branch runs.


---

## 3. Indentation

Python has no `begin` and `end` and no curly braces. Indentation is meaningful in python. Here are some common errors:

<details class="code-example" markdown="1">
<summary>Live code — error 1: the missing colon</summary>

```python
if 5 > 3
    print('yes')
```

```
  File "prices.py", line 1
    if 5 > 3
            ^
SyntaxError: expected ':'
```


</details>

<details class="code-example" markdown="1">
<summary>Live code — error 2: the body is not indented</summary>

```python
if 5 > 3:
print('yes')
```

```
  File "prices.py", line 2
    print('yes')
    ^
IndentationError: expected an indented block after 'if' statement on line 1
```

</details>

<details class="code-example" markdown="1">
<summary>Live code — error 3: inconsistent indentation</summary>

```python
score = 95
if score >= 90:
    print('A')
  print('B')
```

```
  File "prices.py", line 4
    print('B')
              ^
IndentationError: unindent does not match any outer indentation level
```

Four spaces, then two. You must be consistent, **pick four spaces and use four spaces everywhere.** In IDLE, the Tab key gives you four spaces.


## 5. `elif`

</details>
---

<details class="code-example" markdown="1">
<summary>Live code — three outcomes</summary>

Print whether a number is positive, negative, or zero.

```python
num = int(input('Num: '))

if num > 0:
    print('Positive')
else:
    print('Negative')
```

```
Num: 0
Negative
```

</details>

We can't handle this problem with only two options, so we need a way to have multiple branches.


<details class="code-example" markdown="1">
<summary>Live code — <code>sign.py</code></summary>

```python
# sign.py

num = int(input('Num: '))

if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')
```

```
Num: 7
Positive
```

```
Num: -4
Negative
```

```
Num: 0
Zero
```

</details>

`elif` is short for *else if*, and it is one word — not `else if`, not `elseif`. Python will not accept either of those.

Here is how Python runs a chain like this:

1. Check the `if` condition. If it is `True`, run that block and **skip the entire rest of the chain**.
2. Otherwise, check the first `elif`. If it is `True`, run that block and skip the rest.
3. Keep going down the chain.
4. If nothing matched and there is an `else`, run it.

**Exactly one branch runs.**

A chain can have as many `elif` branches as you need:

<details class="code-example" markdown="1">
<summary>Live code — <code>weekday.py</code></summary>

```python
# weekday.py

day = int(input('Day number (1-5): '))

if day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
else:
    print('Not a weekday')
```

```
Day number (1-5): 4
Thursday
```

```
Day number (1-5): 9
Not a weekday
```

</details>

- `elif` may only appear **after** an `if` (or after another `elif`). It cannot stand on its own.
- The `else` at the end is **optional**. If you leave it off and nothing matches, nothing happens.
