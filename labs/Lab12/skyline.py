## Name:

# skyline.py -- CSCI 131, Lab 12
# A city at night, drawn with functions.

from anim import Window
import random

# TODO 3 - Write a window_color() function that randomly chooses yellow or black.
# Use it to choose the color of the windows in building()

def building(win, x, width, floors):
    height = floors * 40
    top = win.height - height
    win.rectangle(x, top, width, height, 'dimgray')
    #TODO 1 - Add windows to the building


win = Window(600, 400, background='midnightblue')

win.circle(500, 70, 35, 'lightyellow')      # the moon

# three buildings to test your function with
building(win, 40, 120, 5)
building(win, 220, 90, 8)
building(win, 380, 150, 3)

#TODO 2 - Write a loop to draw six randomly sized buildings.

win.done()
