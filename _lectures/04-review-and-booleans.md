---
title: "04 — Test 1 Review and Booleans"
published: true
---

**Monday, September 14**

**Reading:** *Python for Everybody*, §3.1–3.4

---

## Part I — Test 1


### R1. Types


>`17 / 2` — what does Python display, and what type is it?

<details class="code-example" markdown="1">
<summary>Answer</summary>

```python
>>> 17 / 2
8.5
>>> type(17 / 2)
<class 'float'>
```

</details>

> `10 / 5`

<details class="code-example" markdown="1">
<summary>Answer</summary>

```python
>>> 10 / 5
2.0
>>> type(10 / 5)
<class 'float'>
```

</details>

> How do I get just `2` out of `10` and `5`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

```python
>>> 10 // 5
2
>>> type(10 // 5)
<class 'int'>
```

</details>


<details class="code-example" markdown="1">
<summary>Live code</summary>

```python
>>> width = 17
>>> height = 12.0
>>> width % 2
1
>>> width / 2
8.5
>>> height / 3
4.0
>>> 1 + 2 * 5
11
```
</details>


---

### R2. `input`

> The user types `35` at the prompt. What is in `hours`, and what type is it?

```python
hours = input('Enter Hours: ')
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```python
>>> hours = input('Enter Hours: ')
Enter Hours: 35
>>> hours
'35'
>>> type(hours)
<class 'str'>
```

</details>

> **Ask:** So what does `print(hours * 2)` display?

<details class="code-example" markdown="1">
<summary>Answer</summary>

```python
>>> print(hours * 2)
3535
```
</details>

---

### R3. Bug finding


```python
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = hours * rate
print('Pay:', pay)
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```python
>>> hours = '35'
>>> rate = '2.75'
>>> pay = hours * rate
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```
</details>

> Fix it - two lines change 

<details class="code-example" markdown="1">
<summary>Answer</summary>

```python
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
pay = hours * rate
print('Pay:', pay)
```

```
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
```



```python
hours_str = input('Enter Hours: ')
hours = float(hours_str)
```

</details>

### R4. The hours program

> Ask the user for a whole number of minutes, print whole hours and leftover minutes. `145` should give 2 hours and 25 minutes.

<details class="code-example" markdown="1">
<summary>Example</summary>

```python
total = int(input('Enter minutes: '))

hours = total // 60
total = total % 60

print('Hours:', hours)
print('Minutes:', total)
```

```
Enter minutes: 145
Hours: 2
Minutes: 25
```

</details>

**The shape, again:**

```
big_unit = amount // size
amount   = amount % size
```
---

## Part II — Booleans

---

### 1. A new type

We have `int`, `float` and `str`. Here is `bool`.

<details class="code-example" markdown="1">
<summary>Live code</summary>

```python
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

`int`, `float` and `str` have infinitely many values. `bool` has exactly two: `True` and `False`.

Capital letter, no quotes `True` is a value; `'True'` is a string, and `true` is nothing at all:

```python
>>> type('True')
<class 'str'>
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
```

</details>

---

### 2. Comparison, the thief of joy

Most of the time, you produce booleans by **making a comparison between two values**.

<details class="code-example" markdown="1">
<summary>Live code — comparison operators</summary>

```python
>>> 5 > 3
True
>>> 5 < 3
False
>>> 5 >= 5
True
>>> 5 != 3
True
>>> 5 == 3
False
>>> type(5 > 3)
<class 'bool'>
```
</details>

There are six comparison operators:

| Operator | Question it asks |
| -------- | ---------------- |
| `==`     | are these equal? |
| `!=`     | are these different? |
| `<`      | is the left one smaller? |
| `>`      | is the left one bigger? |
| `<=`     | smaller or equal? |
| `>=`     | bigger or equal? |

Each one takes two values and produces a `bool`.


#### `=` and `==` are different operators


<details class="code-example" markdown="1">
<summary>Live code — assignment vs comparison</summary>

```python
>>> x = 5          # instruction: put 5 in x
>>> x == 5         # question: is x equal to 5?
True
>>> x == 6
False
```

- `=` **does** something. It changes what `x` means. It produces no value.
- `==` **asks** something. It changes nothing. It produces `True` or `False`.

</details>

---

### 3. `if` only, `if` only...

<details class="code-example" markdown="1">
<summary>Live code </summary>

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

1. The word `if`, then a **boolean expression** — anything that produces `True` or `False`.
2. A **colon** at the end of the line
3. The next line is **indented** — four spaces or a tab. The indentation place the code **inside** the `if`
4. `print('Done.')` is *not* indented, so it is not part of the `if`. It runs either way.

</details>
