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
