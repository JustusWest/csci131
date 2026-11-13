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
