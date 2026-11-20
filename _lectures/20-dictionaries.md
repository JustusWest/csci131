---
title: "20 — Dictionaries: Many Moving Objects"
published: true
---

**Monday, November 23**

Reading: *Python for Everybody*, Chapter 9, §9.1–9.2.

---

## 1. Dictionaries

A list keeps values in **positions**: `0`, `1`, `2`, … A **dictionary** keeps values under **names**, called **keys**. Try these in the shell:

```python
>>> ball = {'x': 300, 'y': 200, 'dx': 7, 'dy': 4}
>>> ball
{'x': 300, 'y': 200, 'dx': 7, 'dy': 4}
>>> ball['x']
300
>>> ball['dy']
4
```

A dictionary is written with **curly braces**. Each item is a **key**, a colon, and its **value**, with commas in between. The key is a string, so it needs quotes. To get a value back, use square brackets with the key, as with a list, but with a **name** in the brackets instead of a position.

| | list | dictionary |
| - | - | - |
| made with | `[300, 200, 7, 4]` | `{'x': 300, 'y': 200, 'dx': 7, 'dy': 4}` |
| look up by | position: `pos[0]` | key: `ball['x']` |
| you have to remember | that position 0 is `x` | nothing: the key says what it is |

### Changing and adding

Assigning to a key **changes** its value. Assigning to a key that isn't there yet **adds** it:

```python
>>> ball['x'] = ball['x'] + ball['dx']
>>> ball['x']
307
>>> ball['size'] = 30
>>> ball
{'x': 307, 'y': 200, 'dx': 7, 'dy': 4, 'size': 30}
```

`ball['x'] = ball['x'] + ball['dx']` is the same idea as `x = x + dx`: the right side uses the **old** value, and the answer is stored back under the same key. It's longer to type, but `print(ball)` now shows the ball's **whole** state at once.

---

## 2. One ball as a dictionary

Here is `walls.py` again, with the five variables replaced by one dictionary. The shape's number goes into the dictionary too, under the key `'shape'`:

<details class="code-example" markdown="1">
<summary>Live code — <code>walls_dict.py</code></summary>

```python
# walls_dict.py -- CSCI 131, Monday Nov 23

from anim import Window

win = Window(600, 400)

ball = {'x': 300, 'y': 200, 'dx': 7, 'dy': 4, 'size': 30}
ball['shape'] = win.circle(ball['x'], ball['y'], ball['size'], 'red')

info = win.text(win.width / 2, 15, '', 'black', 14)

while win.is_open():
    ball['x'] = ball['x'] + ball['dx']
    ball['y'] = ball['y'] + ball['dy']

    if ball['x'] - ball['size'] < 0:                # left wall
        ball['x'] = ball['size']
        ball['dx'] = -ball['dx']
    if ball['x'] + ball['size'] > win.width:        # right wall
        ball['x'] = win.width - ball['size']
        ball['dx'] = -ball['dx']
    if ball['y'] - ball['size'] < 0:                # ceiling
        ball['y'] = ball['size']
        ball['dy'] = -ball['dy']
    if ball['y'] + ball['size'] > win.height:       # floor
        ball['y'] = win.height - ball['size']
        ball['dy'] = -ball['dy']

    win.move_to(ball['shape'], ball['x'], ball['y'])
    win.set_text(info, str(ball))
    win.show()

win.done()
```

</details>

Compare it line by line with `walls.py`: every `x` became `ball['x']`, every `dx` became `ball['dx']`, and so on. The program does **exactly** the same thing.

The circle is made on the second line, **after** the dictionary, because `win.circle` needs the `x`, `y` and size. Its number is then **added** to the dictionary under `'shape'`.

The status line is now one call: `str(ball)` turns the whole dictionary into a string, so every value about the ball is on the screen next to it. No more building `'x = ' + str(x) + ...` by hand.

For **one** ball, this is just a longer way to write the same program. The payoff comes when there are many.

---

## 3. Multiple balls: a list of dictionaries

Making a ball takes two lines: build the dictionary, then make its circle. We'll need to make balls in two places today, so those lines go in a **function**:

```python
def make_ball(win, x, y):
    ball = {'x': x, 'y': y, 'dx': random.randint(2, 7), 'dy': random.randint(2, 7), 'size': 20}
    ball['shape'] = win.circle(x, y, ball['size'], random_color())
    return ball
```

Each call makes a **new** dictionary, with its own random speeds and its own circle. The main program keeps them all in a list:

<details class="code-example" markdown="1">
<summary>Live code — <code>balls.py</code></summary>

```python
# balls.py -- CSCI 131, Monday Nov 23

from anim import Window
import random

def random_color():
    colors = ['red', 'orange', 'gold', 'green', 'blue', 'purple']
    return colors[random.randint(0, len(colors) - 1)]

def make_ball(win, x, y):
    ball = {'x': x, 'y': y, 'dx': random.randint(2, 7), 'dy': random.randint(2, 7), 'size': 20}
    ball['shape'] = win.circle(x, y, ball['size'], random_color())
    return ball

win = Window(600, 400)

balls = []
for i in range(10):
    balls.append(make_ball(win, random.randint(50, 550), random.randint(50, 350)))

while win.is_open():
    for ball in balls:
        ball['x'] = ball['x'] + ball['dx']
        ball['y'] = ball['y'] + ball['dy']

        if ball['x'] - ball['size'] < 0:
            ball['x'] = ball['size']
            ball['dx'] = -ball['dx']
        if ball['x'] + ball['size'] > win.width:
            ball['x'] = win.width - ball['size']
            ball['dx'] = -ball['dx']
        if ball['y'] - ball['size'] < 0:
            ball['y'] = ball['size']
            ball['dy'] = -ball['dy']
        if ball['y'] + ball['size'] > win.height:
            ball['y'] = win.height - ball['size']
            ball['dy'] = -ball['dy']

        win.move_to(ball['shape'], ball['x'], ball['y'])
    win.show()

win.done()
```

</details>

Add `print(balls[0])` after the `for i` loop to see one of the dictionaries in the shell. `balls` is a list of ten of them.

The frame loop has a loop **inside** it:

- The `while` loop is the **frames**, as always.
- In each frame, `for ball in balls:` visits every ball in turn. The body is the `walls_dict.py` code, unchanged: move **this** ball, bounce **this** ball off the walls, put **this** ball's circle where its dictionary says.
- `win.show()` comes **after** the inner loop, once per frame, when every ball has moved.

`ball` is not a copy. Each time through, it **is** one of the dictionaries in the list, so `ball['x'] = ...` changes that ball's `x` for good, and next frame it continues from there.

---

## 4. Clicks add balls

Because the frame loop works on **whatever is in the list**, adding a ball is one line: make a dictionary and append it. Add this inside the `while` loop, before the `for` loop:

```python
    if win.was_clicked():
        balls.append(make_ball(win, win.click_x(), win.click_y()))
```

Click a few times. Every new ball bounces off the walls with the others, and **nothing else in the program changed**: the `for` loop simply has one more dictionary to visit next frame.

A counter is just as short. Make a label before the loop:

```python
count = win.text(win.width / 2, 385, '', 'black', 14)
```

and update it each frame with `len(balls)`:

```python
    win.set_text(count, 'Balls: ' + str(len(balls)))
```

---


## 5. Conclusion

| code | what it does |
| - | - |
| `ball = {'x': 300, 'y': 200}` | make a dictionary with two keys |
| `ball['x']` | the value stored under the key `'x'` |
| `ball['x'] = 307` | change the value under `'x'` |
| `ball['size'] = 30` | add a new key (if `'size'` wasn't there) |
| `len(ball)`, `'x' in ball` | how many keys; is `'x'` one of them? |
| `for key in names:` | loop over a dictionary's keys |
| `balls = []`, `balls.append(ball)` | a list of dictionaries, one per object |
| `for ball in balls:` | visit every object, inside the frame loop |

- A **list** finds a value by **position**; a **dictionary** finds it by **key**, a name you choose.
- One object, one dictionary: its shape number, position, speed, size. `str(ball)` shows all of it in the status line.
- Many objects: a **list** of dictionaries. The frame loop has a `for` loop inside it that updates every object, then **one** `win.show()`.
- Adding an object is `append`; the frame loop doesn't change.
- `KeyError` means the key isn't in the dictionary: usually a misspelling.

---

## 6. Exercise — `snow.py`

Work on this on your own for the rest of the period. It isn't submitted.

Write `snow.py`: **40** snowflakes falling on a dark sky (`Window(600, 400, background='midnightblue')`).

- Write a function `make_flake(win, x, y)` that returns a dictionary with keys `'x'`, `'y'`, `'size'` (a random whole number from 2 to 6), `'speed'` (the size divided by 2, so bigger flakes fall faster) and `'shape'` (a white circle).
- Make 40 flakes at random places in the window, and keep them in a list.
- Each frame, every flake moves down by its own speed. When a flake has gone **completely** below the bottom, put it back just **above** the top (`y` equal to minus its size), at a new random `x`.

**If you finish:** give each flake a `'dx'` key, a random number from `-1` to `1`, so flakes drift sideways as they fall.

<details class="code-example" markdown="1">
<summary>Solution</summary>

```python
# snow.py -- CSCI 131, Monday Nov 23

from anim import Window
import random

def make_flake(win, x, y):
    size = random.randint(2, 6)
    flake = {'x': x, 'y': y, 'size': size, 'speed': size / 2}
    flake['shape'] = win.circle(x, y, size, 'white')
    return flake

win = Window(600, 400, background='midnightblue')

flakes = []
for i in range(40):
    flakes.append(make_flake(win, random.randint(0, win.width), random.randint(0, win.height)))

while win.is_open():
    for flake in flakes:
        flake['y'] = flake['y'] + flake['speed']
        if flake['y'] - flake['size'] > win.height:     # completely below the bottom
            flake['y'] = -flake['size']
            flake['x'] = random.randint(0, win.width)
        win.move_to(flake['shape'], flake['x'], flake['y'])
    win.show()

win.done()
```

The **top** of a flake is at `y - size`, so it's completely gone when that is past `win.height`. Putting it back at `y = -size` puts its bottom edge exactly at the top of the window, so it slides in instead of popping up.

**If you finish:** add `'dx': random.randint(-1, 1)` to the dictionary in `make_flake`, and `flake['x'] = flake['x'] + flake['dx']` in the loop. A flake with `dx` of `0` falls straight down.

</details>

{% comment %}
Exit ticket (not shown on the site).

    ball = {'x': 100, 'y': 50, 'dy': 4}
    ball['y'] = ball['y'] + ball['dy']
    ball['dy'] = -ball['dy']
    ball['size'] = 10
    print(ball)

What does the last line print?

Answer: {'x': 100, 'y': 54, 'dy': -4, 'size': 10}. y uses the old dy (4), then dy flips, and 'size' is added at the end.
{% endcomment %}
