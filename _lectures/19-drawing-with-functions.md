---
title: "19 — Functions: Drawing with Functions"
published: true
---

**Wednesday, November 18**

---

## 1. One flower

On Monday we put circles **around a circle** with `math.cos` and `math.sin`. Put a ring of petals around a gold centre, and you have a flower:

<details class="code-example" markdown="1">
<summary>Live code — <code>flower.py</code></summary>

```python
# flower.py -- CSCI 131, Wednesday Nov 18

from anim import Window
import math

win = Window(600, 400)

for i in range(8):
    angle = math.radians(i * 45)
    px = 300 + 40 * math.cos(angle)
    py = 200 + 40 * math.sin(angle)
    win.circle(px, py, 20, 'pink')
win.circle(300, 200, 30, 'gold')

win.done()
```

</details>

8 petals, 45 degrees apart, 40 pixels from the centre. The gold circle is drawn **after** the loop, so it goes on top of the petals.

Now we want a **second** flower, at `(150, 250)`. We could copy the six lines and change `300` and `200`... in **three** places each. A garden of ten flowers would be sixty lines, and changing the petal colour would mean changing it ten times.

This is what functions are for (Unit 5): write the steps **once**, give them a name, and **call** the name every time you need them.

---

## 2. A function that draws a flower

<details class="code-example" markdown="1">
<summary>Live code — <code>flower.py</code>, with a function</summary>

```python
# flower.py -- CSCI 131, Wednesday Nov 18

from anim import Window
import math



def flower(win, x, y):
    for i in range(8):
        angle = math.radians(i * 45)
        px = x + 40 * math.cos(angle)
        py = y + 40 * math.sin(angle)
        win.circle(px, py, 20, 'pink')
    win.circle(x, y, 30, 'gold')

win = Window(600, 400)


flower(win, 300, 200)
flower(win, 150, 250)
flower(win, 450, 120)

win.done()
```

</details>

The body is the same code as before, with `300` replaced by the parameter `x` and `200` by `y`. Each **call** starts by assigning the arguments to the parameters, then runs the body:

| call | `x` | `y` | first petal at |
| - | - | - | - |
| `flower(win, 300, 200)` | 300 | 200 | `(340, 200)` |
| `flower(win, 150, 250)` | 150 | 250 | `(190, 250)` |
| `flower(win, 450, 120)` | 450 | 120 | |

Remember the Unit 5 rules:

- The `def` goes at the **top**, and it only **stores** the function. Nothing is drawn until the calls at the bottom.
- The function gets what it needs **through its parameters**. It needs the window to draw in, so `win` is passed in too.
- `px`, `py` and `angle` are **local** variables: they exist only while the function runs.
- `flower` doesn't `return` anything. It does a job, like `print` or Unit 5's `banner`: it draws.

> **Ask:** fill in the last row of the table. Then: what would `flower(win, 0, 0)` draw?

<details class="code-example" markdown="1">
<summary>Answer</summary>

`(490, 120)`: the first petal is always 40 pixels to the **right** of the centre (`angle` is `0`, so `cos` is `1` and `sin` is `0`).

`flower(win, 0, 0)` puts the centre at the **top-left corner**, so only a quarter of the flower shows: the gold centre's bottom-right quarter and the petals below and to the right of it. Python doesn't complain; the shapes are just mostly outside the window.

</details>

---

## 3. More parameters

Every flower is the same size and colour. Anything that should be different from one flower to the next becomes a **parameter**. Let's add `size` (how far the petals are from the centre) and `color` (the petals' colour), and give the flower a stem:

<details class="code-example" markdown="1">
<summary>Live code — <code>flower.py</code>, five parameters</summary>

```python
# flower.py -- CSCI 131, Wednesday Nov 18

from anim import Window
import math

def flower(win, x, y, size, color):
    win.rectangle(x - 3, y, 6, win.height - y, 'green')     # stem
    for i in range(8):
        angle = math.radians(i * 45)
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        win.circle(px, py, size / 2, color)
    win.circle(x, y, (size / 2) + 5, 'gold')

win = Window(600, 400)

flower(win, 300, 200, 40, 'pink')
flower(win, 120, 280, 20, 'purple')
flower(win, 470, 130, 60, 'red')

win.done()
```

</details>

Every number that used to be `40` is now `size`, and every `20` is now `size / 2`, so the petals and the centre grow and shrink together. The stem is a rectangle from the flower's centre down to the bottom of the window: its height is `win.height - y`. It's drawn **first**, so the petals cover the top of it.


---

## 4. Flowers in a loop

A call can go inside a loop, like any other line. Monday's row pattern, with a function call in the body, draws a row of flowers that get bigger:

```python
colors = ['red', 'orange', 'purple', 'pink', 'blue']

for i in range(5):
    flower(win, 80 + i * 110, 220, 15 + i * 8, colors[i])
```

Each trip through the loop computes **new arguments** from `i`, and `flower` draws one whole flower with them. There's a loop **inside** `flower` too (the petals), so this is a nested loop, split between the main program and the function: `5 × 8 = 40` petals.

> **Ask:** what are the arguments in the call when `i` is `3`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

`flower(win, 410, 220, 39, 'pink')`: `x` is `80 + 3 × 110 = 410`, `size` is `15 + 3 × 8 = 39`, and `colors[3]` is `'pink'`.

</details>

---

## 5. A function that returns a value

For a garden, each flower should get a **random** colour. That's a job for a function too, but a different kind: it doesn't draw anything, it **returns** a colour (Unit 5: *in through parameters, out through `return`*):

<details class="code-example" markdown="1">
<summary>Live code — <code>garden.py</code></summary>

```python
# garden.py -- CSCI 131, Wednesday Nov 18

from anim import Window
import math
import random

def flower(win, x, y, size, color):
    win.rectangle(x - 3, y, 6, win.height - y, 'green')     # stem
    for i in range(8):
        angle = math.radians(i * 45)
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        win.circle(px, py, size / 2, color)
    win.circle(x, y, (size / 2) + 5, 'gold')

def random_color():
    colors = ['red', 'orange', 'purple', 'pink', 'blue', 'white']
    return colors[random.randint(0, len(colors) - 1)]

win = Window(600, 400, background='lightgreen')

for i in range(8):
    x = 50 + i * 70
    y = random.randint(100, 300)
    size = random.randint(15, 30)
    flower(win, x, y, size, random_color())
    win.pause(0.2)

win.done()
```

</details>

`random_color()` is an **argument** to `flower`. Python runs it **first**, and the call is **replaced by the value it returns**:

```
flower(win, x, y, size, random_color())
flower(win, 120, 214, 22, random_color())      # x, y, size replaced by their values
flower(win, 120, 214, 22, 'orange')            # random_color() replaced by what it returned
```

Then `flower` runs with `color = 'orange'`. Run the program a few times: every garden is different.

The two functions are the two kinds from Unit 5:

| function | does | returns | called like |
| - | - | - | - |
| `flower` | draws a flower | nothing (`None`) | on a line by itself |
| `random_color` | picks a colour | a colour string | anywhere a colour can go |

> **Ask:** what goes wrong if `random_color` ends with `print(colors[...])` instead of `return colors[...]`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

The colour name appears in the shell, but the function returns `None`, so the call becomes `flower(win, 120, 214, 22, None)`, and `win.rectangle` is fine but `win.circle` stops with *A colour should be a string like 'red' or '#ff8800', but got None*. **Functions return; the main program draws** (or prints).

</details>

### If there's time: a gradient function

Monday's colour gradient is a good thing to hide in a function. You don't need to understand the `f'...'` line, only what goes **in** and what comes **out**: give `shade` a number from `0` to `n` and it returns a colour from red to yellow.

```python
def shade(i, n):
    green = i * 255 // n
    return f'#ff{green:02x}00'

for i in range(8):
    flower(win, 50 + i * 70, 200, 25, shade(i, 7))
```

`shade(0, 7)` returns `'#ff0000'` (red) and `shade(7, 7)` returns `'#ffff00'` (yellow), so the row fades from red on the left to yellow on the right. The main program never sees how.

---

## 6. Exercise — `snowmen.py`

Work on this on your own for the rest of the period. It isn't submitted.

Write a function `snowman(win, x, y, size)` that draws a snowman out of three white circles. `(x, y)` is the centre of the **bottom** ball:

- the bottom ball has radius `size`
- the middle ball has radius `size * 0.7`, and sits on top of the bottom ball
- the head has radius `size * 0.5`, and sits on top of the middle ball

"Sits on top" means the two balls just touch, so the distance between their centres is the two radii added together. Work out the middle ball's `y` and the head's `y` on paper first.

Use `win = Window(600, 400, background='skyblue')` so the snow shows up. Then call `snowman` in a loop to draw a row of **four** snowmen that get bigger from left to right, all standing at `y = 340`.

**If you finish:** give each snowman two small black eyes. Where do they go, in terms of `x`, the head's `y` and `size`?

<details class="code-example" markdown="1">
<summary>Solution</summary>

```python
# snowmen.py -- CSCI 131, Wednesday Nov 18

from anim import Window

def snowman(win, x, y, size):
    win.circle(x, y, size, 'white')                 # bottom

    middle_y = y - size - size * 0.7
    win.circle(x, middle_y, size * 0.7, 'white')    # middle

    head_y = middle_y - size * 0.7 - size * 0.5
    win.circle(x, head_y, size * 0.5, 'white')      # head

    # if you finish: eyes
    win.circle(x - size * 0.2, head_y - size * 0.1, size * 0.08, 'black')
    win.circle(x + size * 0.2, head_y - size * 0.1, size * 0.08, 'black')

win = Window(600, 400, background='skyblue')

for i in range(4):
    snowman(win, 90 + i * 140, 340, 20 + i * 8)

win.done()
```

The middle ball's centre is **above** the bottom ball's, so its `y` is **smaller**: up by the bottom radius, then up by its own. The head is the same again, from the middle ball. Computing `middle_y` first and then using it for `head_y` keeps each line short.

</details>

{% comment %}
Exit ticket (not shown on the site).

    def flower(win, x, y, size, color):
        ...
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        ...

    flower(win, 100, 50, 20, 'red')

In this call, what are x, y, size and color? Where is the centre of the first petal (i = 0, so cos is 1 and sin is 0)?

Answer: x = 100, y = 50, size = 20, color = 'red'. The first petal is at (120, 50).
{% endcomment %}
