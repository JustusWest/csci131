---
title: "14 — More Parameters, and Lists as Arguments"
published: true
---

**Wednesday, October 28**

**Reading:** *Python for Everybody*, §4.9 and §4.12

---

## 1. Where we left off

Last time, we wrote our first functions. A `def` **stores** the function under a name, and a **call** runs it. A call starts by assigning the *argument* to the *parameter*.

> **Ask:** what does this print?

```python
def banner(word):
    line = '=' * len(word)
    print(line)
    print(word)
    print(line)

print('Start')
banner('Hi')
print('End')
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
Start
==
Hi
==
End
```

The `def` prints nothing. `banner('Hi')` starts with `word = 'Hi'`, jumps into the body, and comes back to print `End`.

</details>

- the **parameter** of a function is the name you give something when you *define* the function i.e. `word` in `def banner(word)`
- the **argument** of a function is the value inside the `()` when you *call* the function i.e. `Hi` in `banner('Hi')`

Now we look in more depth at parameters, what happens when we have more than one and when the parameter is a list.

---

## 2. More than one parameter

To define a function with more than one parameter, separate the parameters with commas. When you call the function, the arguments are matched up **in order**: the first argument goes to the first parameter, the second to the second, etc.

<details class="code-example" markdown="1">
<summary>Live code — <code>banner.py</code>, adding <code>repeat</code></summary>

```python
def repeat(word, n):
    for i in range(n):
        print(word)

repeat('Go Pride!', 3)
```

```
Go Pride!
Go Pride!
Go Pride!
```

</details>

`repeat('Go Pride!', 3)` starts with `word = 'Go Pride!'` and `n = 3`, then runs the loop. Swap the arguments and it goes wrong:

<details class="code-example" markdown="1">
<summary>Live code — arguments in the wrong order</summary>

```python
>>> repeat(3, 'Go Pride!')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    repeat(3, 'Go Pride!')
  File "banner.py", line 10, in repeat
    for i in range(n):
TypeError: 'str' object cannot be interpreted as an integer
```

</details>

Now `word` is `3` and `n` is `'Go Pride!'`, and `range` can't count to a string. Notice that the traceback has **two** parts. Read it from the bottom up: the error happened on line 10, **inside** `repeat`, and the part above says which call got it there.

Give a function the wrong number of arguments and the error says so plainly:

<details class="code-example" markdown="1">
<summary>Live code — too few, too many</summary>

```python
>>> banner()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    banner()
TypeError: banner() missing 1 required positional argument: 'word'
>>> banner('Widener', 'Pride')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    banner('Widener', 'Pride')
TypeError: banner() takes 1 positional argument but 2 were given
```

</details>

---

## 3. A list as an argument

A parameter can hold any value, including a list. This one prints a numbered list using a loop

<details class="code-example" markdown="1">
<summary>Live code — <code>show_list</code></summary>

```python
def show_list(items):
    for i in range(len(items)):
        print(i + 1, items[i])

groceries = ['eggs', 'milk', 'bread']
show_list(groceries)
```

```
1 eggs
2 milk
3 bread
```

</details>

Why `i + 1`? Positions start at `0`, but people count from `1`.

> **Ask:** what does `show_list('abc')` print?

<details class="code-example" markdown="1">
<summary>Answer</summary>

```
1 a
2 b
3 c
```

A string is a sequence too. `len`, indexing and `range(len(...))` all work on it, so the function works without any changes. We wrote it thinking about lists, but nothing in it says *list*.

</details>

---

## 4. Putting it together — `roster.py`

Read names until `done`, then print them as a numbered roster under a banner. The functions go at the top, and the program goes underneath:

<details class="code-example" markdown="1">
<summary>Live code — <code>roster.py</code></summary>

```python
# roster.py -- CSCI 131, Wednesday Oct 28

def banner(word):
    line = '=' * len(word)
    print(line)
    print(word)
    print(line)

def show_list(items):
    for i in range(len(items)):
        print(i + 1, items[i])

names = []
name = input('Name (or done): ')

while name != 'done':
    names.append(name)
    name = input('Name (or done): ')

banner('Roster')
show_list(names)
```

```
Name (or done): Ana
Name (or done): Ben
Name (or done): Carla
Name (or done): done
======
Roster
======
1 Ana
2 Ben
3 Carla
```

</details>


---

## 5. Conclusion

```python
def repeat(word, n):            # two parameters
    for i in range(n):
        print(word)

def show_list(items):           # a list parameter
    for i in range(len(items)):
        print(i + 1, items[i])

repeat('Go Pride!', 3)          # starts with word = 'Go Pride!', n = 3
show_list(['eggs', 'milk'])     # starts with items = ['eggs', 'milk']
```

- When defining a function, you define the *parameters*
- When calling a fcuntion, you give it *arguments*
- Arguments are matched to parameters **in order**. Swap them and the function gets the wrong values.
- The wrong number of arguments is a `TypeError` that tells you how many the function wanted.
- Different functions can use the same parameter name. Each function's parameters are its own.
- A parameter can be a list. A function that only uses `len` and indexing works on a string too.

Every function so far **printed** something. `len` and `max` don't print anything. They hand a value back, and you decide what to do with it. Next time we write functions that do that, with `return`.

---

## 6. Exercise — `above.py`


Write a function `show_above(scores, limit)` that prints every score in the list `scores` that is greater than `limit`, one per line. Under the function, test it with these calls:

```python
show_above([72, 88, 95, 61, 84], 80)
print('---')
show_above([72, 88, 95, 61, 84], 90)
print('---')
show_above([72, 88, 95, 61, 84], 100)
```

```
88
95
84
---
95
---
```

The last call prints nothing, which is correct: no score is over 100.

**If you finish:** change the program so it reads scores until `done`, as in `roster.py`, then asks for the limit and calls `show_above`. Convert each score with `int` before you `append` it.

```
Score (or done): 70
Score (or done): 92
Score (or done): 85
Score (or done): 64
Score (or done): done
Limit: 80
92
85
```

<details class="code-example" markdown="1">
<summary>Solution</summary>

```python
# above.py -- CSCI 131, Wednesday Oct 28

def show_above(scores, limit):
    for score in scores:
        if score > limit:
            print(score)

scores = []
line = input('Score (or done): ')

while line != 'done':
    scores.append(int(line))
    line = input('Score (or done): ')

limit = int(input('Limit: '))
show_above(scores, limit)
```

The body of `show_above` is a Unit 3 loop with an `if` inside. The only new part is the header, and the header is what lets you run the same loop on any list with any limit.

</details>
