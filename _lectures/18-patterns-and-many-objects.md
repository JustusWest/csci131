---
title: "18 — Loops: Drawing Patterns"
published: true
---

**Monday, November 16**

---

## 1. From last time

On Friday you had **one** ball and **one** paddle, and a variable for every number about them. Today we draw **many** shapes at once, in patterns: rows, grids, targets, staircases and spirals. Placing 45 circles by hand would take 45 lines that are almost the same. A loop can **compute** where each one goes instead.

A quick reminder of what a `for` loop with `range` does:

```python
>>> for i in range(4):
...     print(i, i * 60)
...
0 0
1 60
2 120
3 180
```

`i` takes the values `0, 1, 2, 3`, one per trip through the loop, and anything we compute from `i` changes with it. Today `i * 60` is going to be a **position**.

---

## 2. A loop that draws

<details class="code-example" markdown="1">
<summary>Live code — <code>row.py</code></summary>

```python
# row.py -- CSCI 131, Monday Nov 16

from anim import Window

win = Window(600, 400)

for i in range(9):
    x = 60 + i * 60
    win.circle(x, 200, 25, 'blue')
    win.pause(0.3)

win.done()
```

</details>

The `win.pause(0.3)` is only there so you can **watch the loop run**: one circle appears each time through. Take it out and the whole row appears at once.


`60` is where the first circle goes, and `60` is the gap between circles. Change the gap to `30` and the circles overlap; change the start to `0` and the first circle is cut in half by the left edge.

> **Ask:** what is the **last** value of `x`? Is the last circle inside the window?

<details class="code-example" markdown="1">
<summary>Answer</summary>

`range(9)` stops at `8`, so the last `x` is `60 + 8 * 60 = 540`. Its right edge is `540 + 25 = 565`, which is inside the 600-wide window. With `range(10)` the tenth circle would be centred at `600`, half off the screen.

</details>

### Colours from a list

Every circle is blue. To give them different colours, keep the colours in a **list** and pick one by position:

```python
colors = ['red', 'orange', 'gold', 'green', 'blue']

for i in range(9):
    x = 60 + i * 60
    win.circle(x, 200, 25, colors[i % len(colors)])
```

There are 9 circles and only 5 colours, so `colors[i]` would crash at `i = 5` with `IndexError`. `i % len(colors)` is the **remainder** after dividing by 5 (Unit 1): it goes `0, 1, 2, 3, 4, 0, 1, 2, 3`, so the colours start over after blue.

---

## 3. A grid: a loop inside a loop

A grid is a row of rows. The **outer** loop picks the row, and for each row the **inner** loop draws every circle in it:

<details class="code-example" markdown="1">
<summary>Live code — <code>grid.py</code></summary>

```python
# grid.py -- CSCI 131, Monday Nov 16

from anim import Window

win = Window(600, 400)

colors = ['red', 'orange', 'gold', 'green', 'blue']

for row in range(5):
    for col in range(9):
        x = 60 + col * 60
        y = 60 + row * 70
        win.circle(x, y, 25, colors[col % len(colors)])
        win.pause(0.05)

win.done()
```

</details>

Watch the order the circles appear in: the whole first row, left to right, then the second row. While `row` is `0`, `col` goes all the way from `0` to `8`; only then does `row` become `1`.

`col` decides `x` and `row` decides `y`, using the same "start plus step" pattern as the row: `60 + col * 60` across, `60 + row * 70` down.

> **Ask:** how many circles does this draw? And what happens if you change the colour to `colors[(row + col) % len(colors)]`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

5 rows × 9 columns = **45** circles: the inner loop's body runs 9 times for **each** of the 5 trips through the outer loop.

With `row + col`, each row starts one colour later than the row above it, so the colours make **diagonal stripes**. Try `row` alone, too: each row is one colour.

</details>

---

## 4. Around a circle, and a spiral

To put shapes **around a circle**, Python's `math` module has two functions that do the hard part. For an angle, `math.cos(angle)` says how far **across** and `math.sin(angle)` how far **down** a point on a circle of radius `1` is. Multiply both by the distance you want, add the centre, and you have an `x` and a `y`. You don't need to know any trigonometry to use them.

They measure angles in **radians**, not degrees, so `math.radians(degrees)` converts first.

<details class="code-example" markdown="1">
<summary>Live code — <code>ring.py</code></summary>

```python
# ring.py -- CSCI 131, Monday Nov 16

from anim import Window
import math

win = Window(600, 400)

for i in range(12):
    angle = math.radians(i * 30)
    x = 300 + 150 * math.cos(angle)
    y = 200 + 150 * math.sin(angle)
    win.circle(x, y, 15, 'blue')
    win.pause(0.2)

win.done()
```

</details>

12 circles, 30 degrees apart, make a full turn (`12 × 30 = 360`). The first one is straight to the right of the centre. Because `y` grows **downward**, they go around **clockwise**, like a clock.

To make a **spiral**, change one thing: the distance from the centre grows with `i`, instead of always being `150`.

<details class="code-example" markdown="1">
<summary>Live code — <code>spiral.py</code></summary>

```python
# spiral.py -- CSCI 131, Monday Nov 16

from anim import Window
import math

win = Window(600, 400)

colors = ['red', 'orange', 'gold', 'green', 'blue']

for i in range(60):
    angle = math.radians(i * 20)
    distance = 5 + i * 3
    x = 300 + distance * math.cos(angle)
    y = 200 + distance * math.sin(angle)
    win.circle(x, y, 6, colors[i % len(colors)])
    win.pause(0.05)

win.done()
```

</details>

> **Ask:** what happens if the angle step is `10` instead of `20`? What if `distance` grows by `1` instead of `3`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

With `10`, each turn takes 36 circles instead of 18, so the 60 circles only make it a little more than one and a half times around: a looser, shorter spiral. With `1`, the circles barely move outwards and pile up in the middle; the spiral is tight and small. Every number in the loop is a knob you can turn.

</details>

**If there's time:**  Use `range(200)`, `angle = math.radians(i * 137.5)` and `distance = 12 * math.sqrt(i)`, with a radius of `5`. The odd angle means no two circles ever line up, and the pattern appears on its own.

### If there's time: a colour gradient

The colours still come from a list of five. Instead, we can **compute** a colour from `i`, so the pattern fades smoothly from red in the middle to yellow at the edge.

A colour code like `'#ff8800'` is three pairs of **hexadecimal** (base 16) digits: how much **red**, **green** and **blue**, each from `00` (none) to `ff` (all of it, 255). Red is `'#ff0000'` and yellow is `'#ffff00'`, so in between, only the **green** pair changes.

<details class="code-example" markdown="1">
<summary>Live code — <code>gradient.py</code></summary>

```python
# gradient.py -- CSCI 131, Monday Nov 16

from anim import Window
import math

win = Window(600, 400)

for i in range(200):
    angle = math.radians(i * 137.5)
    distance = 12 * math.sqrt(i)
    x = 300 + distance * math.cos(angle)
    y = 200 + distance * math.sin(angle)

    green = i * 256 // 200
    color = f'#ff{green:02x}00'

    win.circle(x, y, 5, color)
    win.pause(0.02)

win.done()
```

</details>

`green` goes from `0` for the first circle to `254` for the last. The line `f'#ff{green:02x}00'` writes that number as two hexadecimal digits in the middle of the code, so `color` goes from `'#ff0000'` (red) through oranges to `'#fffe00'` (yellow). You don't need to know how that line works; add `print(i, color)` inside the loop to watch the codes change.

> **Ask:** how would you fade from **black** to **red** instead?

<details class="code-example" markdown="1">
<summary>Answer</summary>

Put the changing number in the **red** pair and keep the other two at `00`: `color = f'#{green:02x}0000'` (the variable would be better called `red` now). For the first circle that's `'#000000'`, black.

</details>

---

## 5. Additional Examples

Two more patterns to try on your own.

**Concentric circles.** The loop variable doesn't have to be a position: here every circle has the same centre, and `i` decides the **radius**. Each new circle is smaller and drawn **on top**, so a ring of the one underneath still shows.

<details class="code-example" markdown="1">
<summary>Code — <code>target.py</code></summary>

```python
# target.py -- CSCI 131, Monday Nov 16

from anim import Window

win = Window(600, 400)

colors = ['red', 'white']

for i in range(8):
    radius = 160 - i * 20
    win.circle(300, 200, radius, colors[i % 2])
    win.pause(0.3)

win.done()
```

</details>

Try `radius = 20 + i * 20` instead: the last, biggest circle is white, so it covers all the others and the window looks empty.

**A staircase.** The inner loop's `range` uses the outer loop's variable, so row `0` has 1 box, row `1` has 2, and so on: `1 + 2 + … + 8 = 36` boxes. Rectangles are placed by their **top-left corner**.

<details class="code-example" markdown="1">
<summary>Code — <code>stairs.py</code></summary>

```python
# stairs.py -- CSCI 131, Monday Nov 16

from anim import Window

win = Window(600, 400)

colors = ['red', 'orange', 'gold', 'green', 'blue']

for row in range(8):
    for col in range(row + 1):
        x = 100 + col * 50
        y = 50 + row * 40
        win.rectangle(x, y, 46, 36, colors[row % len(colors)])
        win.pause(0.05)

win.done()
```

</details>

To make it a **pyramid** centred in the window, start each row half its width to the left of the middle: `x = 300 - (row + 1) * 25 + col * 50`.

{% comment %}
Exit ticket (not shown on the site).

    for row in range(3):
        for col in range(4):
            win.circle(50 + col * 50, 50 + row * 50, 20, 'red')

How many circles are drawn? What are row and col when the last one is drawn, and where is it centred?

Answer: 3 x 4 = 12 circles. The last one is row = 2, col = 3, centred at (200, 150).
{% endcomment %}
