---
title: "11 — Changing Sequences: Methods and Return Values"
published: true
---

**Wednesday, October 14**

**Reading:** *Python for Everybody*, §6.5, §6.9 and §8.2

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

`print` does its job (putting `hi` on the screen), then returns `None`. Keep `None` in mind; it comes back next lecture, with list methods.

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

## 5. Capitalizing the vowels

> **Problem:** ask for a word and replace every vowel with its capital letter, so `banana` becomes `bAnAnA`.

`replace` does the changing, and because it returns a new string, we have to assign the result. The question is how to decide what to replace. Here are two ways.

### Way 1: loop over the word

<details class="code-example" markdown="1">
<summary>Live code — <code>capvowels.py</code>, looping over the word</summary>

```python
# capvowels.py -- CSCI 131, Wednesday Oct 14

word = input('Word: ')

for letter in word:
    if letter in 'aeiou':
        word = word.replace(letter, letter.upper())

print(word)
```

```
Word: banana
bAnAnA
```

</details>

Go through the word one letter at a time. If the letter is a vowel (`in` from Monday), replace every copy of it with its capital. `word = ` keeps the result. Without it, this is `answer.py` again and nothing changes.

If anyone asks how the loop can keep going when `word` changes inside it: the `for` goes through the string `word` named when the loop **started**. `word = ...` points the name at a new string, but the original string was never changed (it can't be), so the loop carries on through its letters.

### Way 2: loop over the vowels

<details class="code-example" markdown="1">
<summary>Live code — <code>capvowels.py</code>, looping over the vowels</summary>

```python
word = input('Word: ')

for vowel in 'aeiou':
    word = word.replace(vowel, vowel.upper())

print(word)
```

```
Word: banana
bAnAnA
```

</details>

Same answer, and no `if`. When a vowel isn't in the word, `replace` finds nothing to replace and returns the same string, so there is nothing to check.

### How many times does each loop run?

Add a counter, the Unit 3 counting pattern: start at `0` before the loop and add `1` every time the loop body runs.

<details class="code-example" markdown="1">
<summary>Live code — Way 1 with a counter</summary>

```python
word = input('Word: ')
count = 0

for letter in word:
    count = count + 1
    if letter in 'aeiou':
        word = word.replace(letter, letter.upper())

print(word)
print('Loop ran', count, 'times')
```

```
Word: banana
bAnAnA
Loop ran 6 times
```

```
Word: supercalifragilisticexpialidocious
sUpErcAlIfrAgIlIstIcExpIAlIdOcIOUs
Loop ran 34 times
```

</details>

<details class="code-example" markdown="1">
<summary>Live code — Way 2 with a counter</summary>

```python
word = input('Word: ')
count = 0

for vowel in 'aeiou':
    count = count + 1
    word = word.replace(vowel, vowel.upper())

print(word)
print('Loop ran', count, 'times')
```

```
Word: banana
bAnAnA
Loop ran 5 times
```

```
Word: supercalifragilisticexpialidocious
sUpErcAlIfrAgIlIstIcExpIAlIdOcIOUs
Loop ran 5 times
```

</details>

| word | letters | Way 1 loops | Way 2 loops |
| - | - | - | - |
| `banana` | 6 | 6 | 5 |
| `education` | 9 | 9 | 5 |
| `supercalifragilisticexpialidocious` | 34 | 34 | 5 |

- Way 1 runs **once per letter**, so the longer the word, the more times it runs.
- Way 2 runs **once per vowel**: always 5 times, however long the word is.

Both programs are correct. They do different amounts of work to get there. When you write a loop, it is worth asking: *what decides how many times this runs?*

---

## 6. Conclusion

| | string | list |
| - | - | - |
| change one item: `x[0] = ...` | `TypeError`; build a new string instead | works |
| methods | return a new string; **assign** the result | next lecture |

```python
nums[i] = value                 # put value at position i (lists only)
word = 'J' + word[1:]           # "change" a string by building a new one

for i in range(len(nums)):      # change every item in a list
    nums[i] = nums[i] + 5

name = name.strip()             # string methods: assign the result
line = line.strip().lower()     # clean up input
word.replace(old, new)          # returns a new string
word.find(text)                 # returns a position, or -1

for vowel in 'aeiou':           # runs 5 times, whatever the word
    word = word.replace(vowel, vowel.upper())
```

- A list is **mutable** and a string is **immutable**.
- `for item in x: item = ...` does **not** change the list. Loop over positions and assign to `x[i]`.
- A call is replaced by the value it **returns**. Functions with nothing to return give back `None`.
- String methods return a new string. If you don't assign it, it's lost.
- Two loops can give the same answer and run a different number of times. Looping over the word runs once per letter; looping over `'aeiou'` always runs 5 times.
