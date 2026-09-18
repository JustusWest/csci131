---
title: "06 — Nested Conditions and Logical Operators"
published: true
---

**Monday, September 21**

**Reading:** *Python for Everybody*, §3.2 and §3.6

---

## 1. Review

So far conditionals have asked **one** question. `if num > 0`.  `if day == 'Tuesday'`.

> How would you print `Teenager` for an age between 13 and 19?

<details class="code-example" markdown="1">
<summary>Answer</summary>

That is two questions, not one. `age >= 13` is a comparison and produces a `bool`. `age <= 19` is a comparison and produces a `bool`. You need **both** to be `True` to answer this question.

</details>
---

## 2. Nested conditionals

We can put an `if` inside and `if`

<details class="code-example" markdown="1">
<summary>Live code — <code>teen.py</code></summary>

```python
age = int(input('Age: '))

if age >= 13:
    if age <= 19:
        print('Teenager')

print('Done.')
```

```
Age: 15
Teenager
Done.
```

```
Age: 8
Done.
```

</details>

This is called a **nested** `if`. It handles the conditionals from top to bottom:

1. Check `age >= 13`. If that is `False`, everything indented under it is skipped including the second `if`.
2. If it was `True`, we are inside the outer block, and the next thing in there is another conditional: `if age <= 19`.
3. `print('Teenager')` is indented **eight** spaces, because it sits inside two blocks.

This is all marked by the indentation. The body of the first `if` is indented 4 spaces, the body of the second `if` eight spaces.

Each level can have its own `else`:

<details class="code-example" markdown="1">
<summary>Live code — an <code>else</code> at each level</summary>

```python
age = int(input('Age: '))

if age >= 13:
    if age <= 19:
        print('Teenager')
    else:
        print('Adult')
else:
    print('Child')
```

```
Age: 40
Adult
```

```
Age: 8
Child
```

</details>

Indentation is also what tells you which `if` an `else` belongs to. The first `else` is indented four spaces, so it lines up with `if age <= 19`. The second is not indented at all, so it lines up with `if age >= 13`.

---

## 3. `and`
In that example, the nested `if` is used to check if **both** conditions are `True`. Python has a keyword which checks this: `and`
<details class="code-example" markdown="1">
<summary>Live code — the same program with <code>and</code></summary>

```python
age = int(input('Age: '))

if age >= 13 and age <= 19:
    print('Teenager')

print('Done.')
```

```
Age: 15
Teenager
Done.
```

</details>
`and` takes a `bool` on the left and a `bool` on the right and produces one `bool`:

| Left | Right | `left and right` |
| ---- | ----- | ---------------- |
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

One row out of four. `and` is a demanding operator. These are the same program:

```python
if A:                          if A and B:
    if B:                          ...
        ...
```


---

## 4. `or`

<details class="code-example" markdown="1">
<summary>Live code — nesting</summary>

```python
day = input('Day: ')

if day == 'Saturday':
    print('Weekend')
else:
    if day == 'Sunday':
        print('Weekend')
```

```
Day: Sunday
Weekend
```

</details>

It works, but like the previous example it's a little complicated, using a nested conditional.

<details class="code-example" markdown="1">
<summary>Live code — the same program with <code>or</code></summary>

```python
day = input('Day: ')

if day == 'Saturday' or day == 'Sunday':
    print('Weekend')
```

```
Day: Saturday
Weekend
```

</details>

| Left | Right | `left or right` |
| ---- | ----- | --------------- |
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

Three rows out of four. Note the first one: Python's `or` includes **both**, so any combination that is `True` on an `and` will also be `True` for an `or`
```python
if A:                          if A or B:
    ...                            ...
else:
    if B:
        ...
```

---

## 5. `not`

`not` is the odd one. It takes **one** boolean and flips it.

<details class="code-example" markdown="1">
<summary>Live code — <code>not</code></summary>

```python
>>> not True
False
>>> age = 40
>>> age >= 13
True
>>> not age >= 13
False
```

</details>

Most of the time you do not need it because you can just write the opposite comparison: `age < 13` rather than `not age >= 13`, and `x != 5` rather than `not x == 5`. `not` is most useful for flipping another combination, as in `not (age >= 13 and age <= 19)`.

---

## 6. Order of operations, one more time

Just like arithmetic, the logical operators have an order too: **`not` first, then `and`, then `or`.**

<details class="code-example" markdown="1">
<summary>Live code — logical order</summary>

```python
age = 70
day = 'Friday'

if age >= 65 or age <= 12 and day == 'Tuesday':
    print('Discount')
```

```
Discount
```

`and` binds tighter, it reads as `age >= 65 or (age <= 12 and day == 'Tuesday')`. If what you meant was *seniors and children, but only on Tuesdays*, we have to use `()` to enforce it:

```python
if (age >= 65 or age <= 12) and day == 'Tuesday':
    print('Discount')
```

</details>

 **Use parentheses whenever you mix `and` and `or`** for clarity.

---

## 7. Putting it together — `ride.py`
Imagine an amusement park: you may ride if you are at least 48 inches tall, **and** you are either at least 8 years old **or** with an adult.

<details class="code-example" markdown="1">
<summary>Live code — <code>ride.py</code></summary>

```python

height = int(input('Height in inches: '))
age = int(input('Age: '))
adult = input('With an adult (yes/no)? ')

if height >= 48 and (age >= 8 or adult == 'yes'):
    print('You may ride.')
else:
    print('Sorry, not this time.')
```

```
Height in inches: 52
Age: 10
With an adult (yes/no)? no
You may ride.
```

```
Height in inches: 50
Age: 6
With an adult (yes/no)? yes
You may ride.
```

```
Height in inches: 44
Age: 30
With an adult (yes/no)? yes
Sorry, not this time.
```

</details>

Two of those inputs are counts, so `int`; the third is a word, so it stays a `str` and gets compared with `==`.

---

## 8. Nesting anyway

`and` is shorter, but it collapses every reason for saying no into one message. To tell the rider *why*, you need separate branches, and separate branches mean nesting.

<details class="code-example" markdown="1">
<summary>Live code — <code>ride.py</code>, nested for better messages</summary>

```python
if height >= 48:
    if age >= 8 or adult == 'yes':
        print('You may ride.')
    else:
        print('Riders under 8 must be with an adult.')
else:
    print('You must be 48 inches tall to ride.')
```

```
Height in inches: 50
Age: 6
With an adult (yes/no)? no
Riders under 8 must be with an adult.
```

</details>

Same way to check the conditions, but with different use cases.
---

## 9. Conclusion

```python
if A and B:        # both
if A or B:         # at least one, possibly both
if not A:          # the opposite

if A:              # nested -- an `and` with room for an
    if B:          # else at each level
        ...
    else:
        ...
else:
    ...
```

- `and` and `or` join two **booleans**. Each side must be a complete comparison.
- `not` takes one. Prefer flipping the comparison when you can.
- **The order of operations** is `not`, then `and`, then `or`. 

---

Next class is a **graded programming assignment**, in class.

Friday is **Test 2**, covering Chapter 3 — booleans and comparisons, `if`, `else`, `elif`, nesting, `and`, `or` and `not`.
