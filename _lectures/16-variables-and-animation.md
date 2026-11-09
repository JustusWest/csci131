---
title: "16 — Animation Intro"
published: true
---

**Monday, November 9**

---

## 1. A change of pace

For the rest of the semester we'll going to write some animation based programs so you can see your code executing in real time. This is a bit experimental, so please provide feedback early and often.

We'll use a small module I wrote for the course called `anim`. We will start by going back over earlier topics and applying what we've learned to create animations. We start with our first topic, **variables and expressions**.

---

## 2. Setting up


1. Download <a href="{{ '/code/6-animation/00-setup/anim.py' | relative_url }}" download><strong><code>anim.py</code></strong></a> and <a href="{{ '/code/6-animation/00-setup/hello_anim.py' | relative_url }}" download><strong><code>hello_anim.py</code></strong></a> from the course site. They are also on the [Code page]({{ '/code.html' | relative_url }}), under Unit 6. Both go into your **Downloads** folder. Put them in the folder where you save all your programs.
2. In IDLE, use **File → Open**, and open `hello_anim.py`.
3. Press **F5**. A window should open with a red ball in it.

To use the `anim` module, you must run your code file from a folder that contains the `anim.py` file.

<details class="code-example" markdown="1">
<summary>Code — <code>hello_anim.py</code></summary>

```python
# hello_anim.py -- CSCI 131
# Run this first. If a window opens with a red ball in the middle,
# anim.py is in the right place and you're ready to go.

from anim import Window

win = Window(600, 400)
ball = win.circle(300, 200, 40, 'red')
win.done()
```

</details>

`from anim import Window` looks for `anim.py` **in the same folder as your program**. Every program you must be saved in the same folder as `anim.py`.

---

## 3. The window

<details class="code-example" markdown="1">
<summary>Live code — <code>ball.py</code></summary>

```python
# ball.py -- CSCI 131, Monday Nov 9

from anim import Window

win = Window(600, 400)

win.done()
```

</details>

`Window(600, 400)` opens a window 600 pixels wide and 400 tall. `win` is a variable like any other; it holds the window, and every command for the window starts with `win.`. This is the same dot you used in `word.upper()`.

`win.done()` keeps the window open until you close it. It goes on the **last line** of every program.

### Coordinates

Every point in the window has an `x` (how far across) and a `y` (how far down):

```
(0, 0) ──────────── x grows this way ────────────▶ (600, 0)
  │
  │                    (300, 200)
  │                        ●
  y grows DOWN
  │
  ▼
(0, 400)                                          (600, 400)
```

`(0, 0)` is the **top-left** corner.

---

## 4. A ball

<details class="code-example" markdown="1">
<summary>Live code — <code>ball.py</code></summary>

```python
# ball.py -- CSCI 131, Monday Nov 9

from anim import Window

win = Window(600, 400)
ball = win.circle(300, 200, 40, 'red')
print(ball)

win.done()
```

```
1
```

</details>

`win.circle(x, y, radius, color)` draws a circle **centred** at `(x, y)`. 

Using literal values to define a ball like above makes it hard to change those values. So we will make them variables:

<details class="code-example" markdown="1">
<summary>Live code — <code>ball.py</code>, with variables</summary>

```python
# ball.py -- CSCI 131, Monday Nov 9

from anim import Window

win = Window(600, 400)

x = 300
y = 200
size = 40
color = 'red'

ball = win.circle(x, y, size, color)

win.done()
```

</details>

Same picture. But now we can use **expressions**. The ball should be in the middle of the window, and the middle is half the width and half the height:

```python
x = win.width / 2
y = win.height / 2
```

`win.width` and `win.height` hold the window's size (`600` and `400`). Change the window to `Window(800, 600)` and the ball is still in the middle, without touching anything else.

> **Ask:** where does `win.circle(0, 0, 40, 'red')` appear? How much of it can you see?

<details class="code-example" markdown="1">
<summary>Answer</summary>

Its centre is the top-left corner, so only the bottom-right quarter of the circle is inside the window. The rest is off the screen. Nothing goes wrong: shapes are allowed to be partly or completely off the window.

</details>

---

## 5. Changing the ball

> **Ask:** the ball is already drawn. What happens on the screen when this line runs?

```python
size = 80
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

**Nothing.** `size` is now `80`, but the circle on the screen doesn't change.

`win.circle(x, y, size, color)` used the **value** of `size` at the moment it ran, which was `40`. After that, the variable and the circle are separate. Changing the variable doesn't redraw anything.

</details>

To change the picture, you change the variable **and then tell the window**:

<details class="code-example" markdown="1">
<summary>Live code — <code>ball.py</code>, changing size and colour</summary>

```python
# ball.py -- CSCI 131, Monday Nov 9

from anim import Window

win = Window(600, 400)

x = win.width / 2
y = win.height / 2
size = 40
color = 'red'

ball = win.circle(x, y, size, color)
win.pause(1)

size = size * 2
win.set_size(ball, size)
win.pause(1)

color = 'blue'
win.set_color(ball, color)
win.pause(1)

x = x + 150
win.move_to(ball, x, y)

win.done()
```

</details>

- `win.pause(1)` shows what's drawn so far and waits one second. Without the pauses, all the changes happen too fast to see.
- `win.set_size(ball, size)`, `win.set_color(ball, color)` and `win.move_to(ball, x, y)` all start with the shape's name, so the window knows which shape to change.
- Colours are strings: `'red'`, `'skyblue'`, `'darkgreen'`, `'orange'`… or codes like `'#ff8800'`.

> **Ask:** after the last `move_to`, what are `x`, `y` and `size`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

`x` is `450.0` (`300.0 + 150`), `y` is `200.0` and `size` is `80`. `x` and `y` are floats because `/` always gives a float. That makes no difference to the window.

</details>

---

## 6. Making it fall

An animation is a series of **frames**, like a flip book. In each frame we change some variables, put the shapes where the variables say, and show the result. Then we do it again, and a `while` loop does the repeating:

<details class="code-example" markdown="1">
<summary>Live code — <code>fall.py</code></summary>

```python
# fall.py -- CSCI 131, Monday Nov 9

from anim import Window

win = Window(600, 400)

x = 300
y = 50
size = 40
speed = 10

ball = win.circle(x, y, size, 'red')

while y < win.height + size:
    y = y + speed
    win.move_to(ball, x, y)
    win.show()

win.done()
```

</details>

Each time through the loop is one frame:

1. `y = y + speed` moves `y` down by `10`
2. `win.move_to(ball, x, y)` puts the ball where `y` now says
3. `win.show()` draws the frame and waits a moment (1/30 of a second)

The loop stops when `y` reaches `440` (`win.height + size`). Why add `size`? When the **centre** of the ball reaches the bottom edge at `400`, half the ball is still showing. At `440` the top of the ball has gone past the edge too.

### Trace it

> **Ask:** before running it, fill in `y` for the first frames.

| frame | `y` |
| - | - |
| start | 50 |
| 1 | |
| 2 | |
| 3 | |
| 4 | |

<details class="code-example" markdown="1">
<summary>Answer</summary>

`60`, `70`, `80`, `90`. Each frame adds `speed`, which is `10`. The loop runs until `y` is `440`, which takes 39 frames.

</details>

Now check it two ways. First, add `print(y)` as the last line inside the loop. The numbers in the shell are the same numbers the ball is following.

Second, change the window line to:

```python
win = Window(600, 400, step=True)
```

In **step mode**, every `win.show()` waits for you to press the **space bar** (or click in the window), and the title bar shows the frame number. Click on the window first so it gets the keyboard, then go one frame at a time and compare the window, the shell and your table.

> **Ask:** what happens if `speed` is `-10`? What if it's `0`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

With `-10`, `y` gets *smaller*, so the ball goes **up** and off the top. `y` never reaches `440`, so the loop never ends: close the window to stop it. With `0`, `y` never changes and the ball sits still forever. Same problem.

</details>

---

## 7. Gravity

Real things don't fall at a steady speed: they speed up. That means `speed` should change too. One more line in the loop:

<details class="code-example" markdown="1">
<summary>Live code — <code>fall.py</code>, with gravity</summary>

```python
# fall.py -- CSCI 131, Monday Nov 9

from anim import Window

win = Window(600, 400)

x = 300
y = 50
size = 40
speed = 0
gravity = 1
frame = 0

ball = win.circle(x, y, size, 'red')

while y < win.height + size:
    frame = frame + 1
    speed = speed + gravity
    y = y + speed
    win.move_to(ball, x, y)
    print(frame, speed, y)
    win.show()

win.done()
```

</details>

Now **three** variables change every frame. `frame` counts the frames, so the printout lines up with your table and with step mode.

> **Ask:** fill in the table before you run it.

| frame | `speed` | `y` |
| - | - | - |
| start | 0 | 50 |
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

<details class="code-example" markdown="1">
<summary>Answer</summary>

| frame | `speed` | `y` |
| - | - | - |
| start | 0 | 50 |
| 1 | 1 | 51 |
| 2 | 2 | 53 |
| 3 | 3 | 56 |
| 4 | 4 | 60 |
| 5 | 5 | 65 |

Each frame `speed` goes up by `1`, and then `y` goes up by the **new** `speed`. So the ball moves 1, then 2, then 3… pixels per frame, and it gets faster.

</details>

### Order matters

> **Ask:** swap the two lines, so `y = y + speed` comes before `speed = speed + gravity`. What changes in the table?

<details class="code-example" markdown="1">
<summary>Answer</summary>

In frame 1, `y = y + speed` uses the **old** `speed`, which is `0`, so `y` stays `50`. Only then does `speed` become `1`. Every row of `y` is one frame behind: `50`, `51`, `53`, `56`, `60`.

The program runs line by line, and each line uses whatever the variables hold **at that moment**. You can see the difference only because you traced it.

</details>

Try changing `gravity` to `0.5`, or to `3`, and predict what the ball will do before you run it.

---

## 8. If there's time: start where you click

<details class="code-example" markdown="1">
<summary>Live code — <code>fall.py</code>, start at a click</summary>

```python
# fall.py -- CSCI 131, Monday Nov 9

from anim import Window

win = Window(600, 400)

win.wait_for_click()
x = win.click_x()
y = win.click_y()
size = 40
speed = 0
gravity = 1

ball = win.circle(x, y, size, 'red')

while y < win.height + size:
    speed = speed + gravity
    y = y + speed
    win.move_to(ball, x, y)
    win.show()

win.done()
```

</details>

`win.wait_for_click()` stops the program until you click in the window. After that, `win.click_x()` and `win.click_y()` give back where you clicked. They're values like any others, so they go into `x` and `y`, and everything after that is the program from before.

> **Ask:** where should you click so the ball takes the longest to fall off the screen? Where for the shortest?

---

## 9. Conclusion

| word | meaning | example |
| - | - | - |
| **module** | a file of Python code your program can use | `anim.py` |
| **coordinates** | `x` across, `y` down, from the top-left corner | `(300, 200)` |
| **frame** | one picture in an animation: one time through the loop | `y = y + speed`, `move_to`, `show` |
| **step mode** | waits for the space bar (or a click) before each frame | `Window(600, 400, step=True)` |

| call | what it does |
| - | - |
| `win = Window(600, 400)` | open a window 600 wide and 400 tall |
| `win.width`, `win.height` | the window's size |
| `ball = win.circle(x, y, radius, color)` | draw a circle centred at `(x, y)`; gives back its number |
| `win.move_to(ball, x, y)` | put the shape at `(x, y)` |
| `win.set_size(ball, radius)` | change a circle's size |
| `win.set_color(ball, color)` | change a shape's colour |
| `win.pause(seconds)` | show the window, then wait |
| `win.show()` | show one frame, then wait a moment |
| `win.wait_for_click()`, `win.click_x()`, `win.click_y()` | wait for a click; where it was |
| `win.done()` | keep the window open; the last line of every program |

- `(0, 0)` is the top-left corner. A bigger `y` is **lower** on the screen.
- A shape is drawn with the values its variables had **when the line ran**. Changing a variable afterwards does nothing until you tell the window (`move_to`, `set_size`, `set_color`).
- `y = y + speed` uses the **old** `y` on the right side and stores the answer as the new `y`.
- An animation is a `while` loop: change the variables, put the shapes where they say, `win.show()`.
- The order of lines inside the loop matters. Trace it to see how.

---

## 10. Exercise — `drop.py`

Work on this on your own for the rest of the period. It isn't submitted.

Write `drop.py`, with **two** balls of different sizes and colours, side by side near the top of the window. Each ball has its own speed (`speed1` and `speed2`, say), and they both fall **in the same loop**, so they move at the same time. Keep the loop going until **both** have left the bottom of the screen.

Before you run it, write down `y1` and `y2` for the first three frames, then check with `print`.

**If you finish:** give one ball gravity and keep the other at a steady speed. Pick the numbers so that the ball with gravity starts slower but passes the other one before the bottom. Use step mode to find the frame where it passes.

<details class="code-example" markdown="1">
<summary>Solution</summary>

```python
# drop.py -- CSCI 131, Monday Nov 9

from anim import Window

win = Window(600, 400)

x1 = 200
y1 = 50
size1 = 30
speed1 = 4

x2 = 400
y2 = 50
size2 = 50
speed2 = 0
gravity = 0.5

ball1 = win.circle(x1, y1, size1, 'orange')
ball2 = win.circle(x2, y2, size2, 'purple')

frame = 0
while y1 < win.height + size1 or y2 < win.height + size2:
    frame = frame + 1
    y1 = y1 + speed1
    speed2 = speed2 + gravity
    y2 = y2 + speed2
    win.move_to(ball1, x1, y1)
    win.move_to(ball2, x2, y2)
    print(frame, y1, y2)
    win.show()

win.done()
```

The loop keeps going while **either** ball is still on the screen, so the condition uses `or`. With `and`, it would stop as soon as the *first* ball left.

The first ball moves `4` every frame: `54`, `58`, `62`. The second starts at `0` and speeds up by `0.5`: `50.5`, `51.5`, `53.0`. Ball 2 catches up with ball 1 at frame 15 (both at `110`), and from frame 16 on it's ahead.

</details>
