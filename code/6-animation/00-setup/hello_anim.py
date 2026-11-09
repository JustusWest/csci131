# hello_anim.py -- CSCI 131
# Run this first. If a window opens with a red ball in the middle,
# anim.py is in the right place and you're ready to go.

from anim import Window

win = Window(600, 400)
ball = win.circle(300, 200, 40, 'red')
win.done()
