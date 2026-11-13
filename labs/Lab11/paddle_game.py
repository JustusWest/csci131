## Name:

# paddle_game.py -- CSCI 131, Lab 11
# The ball from walls.py and the paddle from paddle.py, in one program.

from anim import Window

win = Window(600, 400)

# the ball
x = 300
y = 200
size = 30
dx = 7
dy = 4
ball = win.circle(x, y, size, 'red')

# the paddle
px = 250            # paddle's left edge
py = 360            # paddle's top edge
pw = 100            # paddle's width
ph = 15             # paddle's height
pspeed = 8
paddle = win.rectangle(px, py, pw, ph, 'black')

info = win.text( 75, 15, '', 'black', 14) # info panel in the top left


while win.is_open():
    # move the paddle left and right
    if win.key_down('Left'):
        px = px - pspeed
    elif win.key_down('Right'):
        px = px + pspeed
    # keep the paddle on the screen
    if px < 0:
        px = 0
    if px + pw > win.width:
        px = win.width - pw

    # move the ball
    x = x + dx
    y = y + dy

    # bounce the ball off the walls
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
    # TODO: The ball falls through and stops the animation
    if y + size > win.height:           # floor
        y = win.height - size
        dy = -dy
        win.set_color(ball, 'red')

    # TODO: Make the ball bounce off the paddle

    # TODO: Add a score to the info panel and make it go up when the ball bounces off the paddle

    win.set_text(info, 'x = ' + str(x) + '  y = ' + str(y)) # displays x,y of the ball


    win.move_to(paddle, px, py)
    win.move_to(ball, x, y)
    win.show()

win.done()
