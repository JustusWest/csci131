---
title: "17 — Conditional Animation - Collisions"
published: true
---

**Wednesday, November 11**

---

## 1. From last time

Make sure `anim.py` is in the same folder as today's programs.


<details class="code-example" markdown="1">
<summary>Live code — <code>bounce.py</code></summary>

```python
# bounce.py -- CSCI 131, Wednesday Nov 11

from anim import Window

win = Window(600, 400)

x = 300
y = 50
size = 40
speed = 20

ball = win.circle(x, y, size, 'red')

while win.is_open():
    y = y + speed
    win.move_to(ball, x, y)
    win.show()

win.done()
```

</details>

`win.is_open()` is `True` until you close the window, so this loop runs **until you close it**. From now on, almost every animation loop starts this way.

> **Ask:** the ball disappears after about a second. Is the program still running? What is happening to `y`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

Yes. The loop still runs 30 times a second, and `y` keeps growing, far below the window where we can't see the ball. Add `print(y)` inside the loop to watch it.

</details>

---

## 2. Bouncing off the floor

The ball should turn around when it reaches the floor. The **bottom** of the ball is at `y + size` (the centre plus the radius), and the floor is at `win.height`:

```
          ●  ← centre at y
          │
          ▼  ← bottom at y + size
──────────────────── floor: y = win.height (400)
```

"Turn around" means the ball now moves **up**, so `speed` becomes negative:

<details class="code-example" markdown="1">
<summary>Live code — <code>bounce.py</code>, bouncing off the floor</summary>

```python
# bounce.py -- CSCI 131, Wednesday Nov 11

from anim import Window

win = Window(600, 400)

x = 300
y = 50
size = 40
speed = 20
frame = 0

ball = win.circle(x, y, size, 'red')
info = win.text(win.width / 2, 15, '', 'black', 14)

while win.is_open():
    frame = frame + 1
    y = y + speed
    if y + size > win.height:
        speed = -speed
    win.move_to(ball, x, y)
    win.set_text(info, 'frame ' + str(frame) + '    y = ' + str(y) + '    speed = ' + str(speed))
    win.show()

win.done()
```

</details>

`speed = -speed` flips the sign: `20` becomes `-20`, and `-20` would become `20`. From the next frame on, `y = y + speed` makes `y` **smaller**, and the ball goes up.

### A status line

`info` is a piece of **text** in the window. `win.text(x, y, message, color, size)` makes it, centred at `(x, y)`, and it starts out empty (`''`). Each frame, `win.set_text(info, ...)` changes what it says to the current values of `frame`, `y` and `speed`. The `+` joins strings, as in Unit 1, and `str(y)` turns the number into a string so it can be joined.

Now the variables are shown **next to the ball they control**. At 30 frames a second they change too fast to read, so slow the program down. There are two ways:

- `win = Window(600, 400, fps=5)` runs at 5 frames a second instead of 30.
- `win = Window(600, 400, step=True)` waits for the **space bar** before each frame.


### Sinking into the floor

Run the program in step mode and go to the frame where the ball reaches the floor, frame 16. The status line says `y = 370`, so the bottom of the ball is at `410`, which is **10 pixels below the floor**. That frame is drawn with part of the ball under the floor. At full speed you can barely see it, but in step mode the ball is cut off.

The fix: when the ball hits the floor, put it **on** the floor before turning it around:

```python
    if y + size > win.height:
        y = win.height - size
        speed = -speed
```

If the bottom is at `win.height`, the centre is at `win.height - size`, which is `360`. Run it again in step mode: now the status line says `y = 360` in frame 16, and the ball sits exactly on the floor before it goes back up.

> **Ask:** does that one frame really matter? Try it with gravity and a bounce that loses some energy, the way a real ball does:

```python
    speed = speed + 1
    y = y + speed
    if y + size > win.height:
        speed = -speed * 0.7
```

<details class="code-example" markdown="1">
<summary>Answer</summary>

Without the fix, the ball gets **stuck in the floor** on its second bounce and slowly sinks through it. The slower, weaker bounce doesn't lift the ball back above the floor in one frame. So on the next frame the `if` is true *again*, the speed flips back to downwards, and the ball goes deeper.

With `y = win.height - size` added, the ball always starts its trip up from on top of the floor, and it settles there and stops, like a real ball.

</details>

---

## 3. Four walls

Now the ball goes up and off the top forever. A **ceiling** needs a second `if`. The **top** of the ball is at `y - size`, and the top of the window is `0`:

```python
    if y - size < 0:
        y = size
        speed = -speed
```

To move in every direction, the ball needs a speed **across** and a speed **down**. We'll call them `dx` and `dy` ("change in `x`", "change in `y`"). Each frame, both change the position, and there is one `if` per wall:

<details class="code-example" markdown="1">
<summary>Live code — <code>walls.py</code></summary>

```python
# walls.py -- CSCI 131, Wednesday Nov 11

from anim import Window

win = Window(600, 400)

x = 300
y = 200
size = 30
dx = 7
dy = 4

ball = win.circle(x, y, size, 'red')

while win.is_open():
    x = x + dx
    y = y + dy

    if x - size < 0:                    # left wall
        x = size
        dx = -dx
        win.set_color(ball, 'blue')
    if x + size > win.width:            # right wall
        x = win.width - size
        dx = -dx
        win.set_color(ball, 'blue')
    if y - size < 0:                    # ceiling
        y = size
        dy = -dy
        win.set_color(ball, 'red')
    if y + size > win.height:           # floor
        y = win.height - size
        dy = -dy
        win.set_color(ball, 'red')

    win.move_to(ball, x, y)
    win.show()

win.done()
```

</details>

Hitting a side wall only flips `dx`; hitting the floor or ceiling only flips `dy`. The ball turns blue after a side wall and red after the floor or ceiling, so you can see which `if` ran.

> **Ask:** could the four `if`s be `if`, `elif`, `elif`, `elif`?

<details class="code-example" markdown="1">
<summary>Answer</summary>

No. In a corner the ball can hit a side wall **and** the floor in the same frame. With `elif`, only the first one would run, and the ball would go through the floor. Left and right can never both happen at once, so `elif` between those two would be fine; the same goes for ceiling and floor.

</details>

---

## 4. The keyboard

`win.key_down('Left')` is `True` while the left arrow key is held down. That's a question we can ask every frame, so a paddle that follows the arrow keys is two `if`s:

<details class="code-example" markdown="1">
<summary>Live code — <code>paddle.py</code></summary>

```python
# paddle.py -- CSCI 131, Wednesday Nov 11

from anim import Window

win = Window(600, 400)

px = 250            # paddle's left edge
py = 360            # paddle's top edge
pw = 100            # paddle's width
ph = 15             # paddle's height
pspeed = 8

paddle = win.rectangle(px, py, pw, ph, 'black')

while win.is_open():
    if win.key_down('Left'):
        px = px - pspeed
    elif win.key_down('Right'):
        px = px + pspeed

    win.move_to(paddle, px, py)
    win.show()

win.done()
```

</details>

Click in the window first so it gets the keyboard. Remember that a **rectangle** is placed by its **top-left corner**, not its centre, so `px` is the left edge and `px + pw` is the right edge.

> **Ask:** hold the left arrow down for a few seconds. What goes wrong? Fix it with two more `if`s.

<details class="code-example" markdown="1">
<summary>Answer</summary>

The paddle slides off the screen, and `px` keeps going negative. Keep it on the screen the same way we kept the ball in, but with the rectangle's edges:

```python
    if px < 0:
        px = 0
    if px + pw > win.width:
        px = win.width - pw
```

These go **after** the arrow-key `if`s and **before** `move_to`, so the paddle is never drawn off the screen.

</details>

`win.key_down` is `True` in **every frame** while the key is held, which is right for moving. For something that should happen **once per press**, use `win.key_pressed('space')`: held for one second, `key_down` would be true about 30 times, `key_pressed` once.

Step mode uses the space bar for "next frame", so for programs that read the keyboard, slow them down with `fps=5` instead.

On Friday you'll put the ball and the paddle in the same program, and make the ball bounce off the paddle.

---

## 5. Conclusion

| call | what it does |
| - | - |
| `win.is_open()` | `True` until the window is closed: `while win.is_open():` |
| `win.key_down('Left')` | `True` while that key is held down, every frame |
| `win.key_pressed('space')` | `True` once for each press of the key |
| `label = win.text(x, y, message, color, size)` | write text centred at `(x, y)` |
| `win.set_text(label, message)` | change what the text says |

- A wall is an `if`: **is the shape past the edge?** If so, put it back **on** the edge (or it can get stuck), then turn it around by flipping the sign of its speed: `dy = -dy`.
- Use separate `if`s when more than one thing can happen in the same frame (a corner). Use `elif` when only one can (left key *or* right key).
- A circle's edges are its centre plus or minus the radius. A rectangle's are its corner plus its width or height.
- The program checks **exactly** what your condition says. Trace the frame where it goes wrong to find out what you actually wrote.

---

## 6. Exercise — `count.py`

Work on this on your own for the rest of the period. It isn't submitted.

Start from `walls.py`. Add a **bounce counter**: text near the top of the window that says `Bounces: 0` and goes up by one every time the ball hits any wall.

Before you run it, work out on paper the **frame** of the first bounce, and which wall it is. (Start: `x = 300`, `y = 200`, `size = 30`, `dx = 7`, `dy = 4`, in a 600 × 400 window.) Then check it: add a status line that shows `frame`, `x` and `y`, and run with `fps=5` or step mode.

**If you finish:** make the ball go a little faster after every bounce. Careful: `dx = dx + 1` is wrong when `dx` is negative. Why?

<details class="code-example" markdown="1">
<summary>Solution</summary>

```python
# count.py -- CSCI 131, Wednesday Nov 11

from anim import Window

win = Window(600, 400)

x = 300
y = 200
size = 30
dx = 7
dy = 4

ball = win.circle(x, y, size, 'red')
bounces = 0
label = win.text(win.width / 2, 45, 'Bounces: 0', 'black', 16)
info = win.text(win.width / 2, 15, '', 'black', 14)

frame = 0
while win.is_open():
    frame = frame + 1
    x = x + dx
    y = y + dy

    if x - size < 0:
        x = size
        dx = -dx
        bounces = bounces + 1
    if x + size > win.width:
        x = win.width - size
        dx = -dx
        bounces = bounces + 1
    if y - size < 0:
        y = size
        dy = -dy
        bounces = bounces + 1
    if y + size > win.height:
        y = win.height - size
        dy = -dy
        bounces = bounces + 1

    win.set_text(label, 'Bounces: ' + str(bounces))
    win.move_to(ball, x, y)
    win.set_text(info, 'frame ' + str(frame) + '    x = ' + str(x) + '    y = ' + str(y))
    win.show()

win.done()
```

The first bounce is the **right wall**, in frame **39**. The right edge of the ball is at `x + 30`, which must get past `600`, so `x` must get past `570`. `x` goes `307`, `314`, …, and `x + dx` makes it `573` in frame 39, so the `if` puts it back at `570`. That's why the status line shows `x = 570` in frame 39, not `573`. The floor would take until frame 43 (`y + 30` past `400` means `y` past `370`, and `200 + 4 × 43 = 372`).

**If you finish:** `dx = dx + 1` makes a ball moving left (`dx` is `-7`) *slower* (`-6`). Speed it up away from zero instead: `if dx > 0: dx = dx + 1` and `else: dx = dx - 1`. Or simply `dx = -dx * 1.1` instead of `dx = -dx` in the bounce.

</details>

{% comment %}
Exit ticket (not shown on the site).

    win = Window(600, 400)
    x = 560
    dx = 15
    size = 20
    ...
    while win.is_open():
        x = x + dx
        if x + size > win.width:
            x = win.width - size
            dx = -dx

What are x and dx after frames 1, 2 and 3?

Answer: frame 1: x = 575, dx = 15 (595 is not > 600). Frame 2: 590 + 20 = 610 > 600, so x = 580, dx = -15. Frame 3: x = 565, dx = -15.
{% endcomment %}
