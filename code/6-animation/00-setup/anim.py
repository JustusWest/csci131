"""
anim.py -- simple animations for CSCI 131

Save this file in the SAME FOLDER as your program, then start your
program with:

    from anim import Window

A tiny example:

    from anim import Window

    win = Window(600, 400)
    y = 0
    ball = win.circle(300, y, 30, 'red')

    while y < win.height:
        y = y + 5
        win.move_to(ball, 300, y)
        win.show()

    win.done()

Things you can do with a window called win
------------------------------------------
Making the window
    win = Window(600, 400)          a window 600 wide and 400 tall
    win.width, win.height           the window's size
    (0, 0) is the TOP-LEFT corner.  x grows to the right, y grows DOWN.

Making shapes (each one gives back a number that names the shape)
    ball = win.circle(x, y, radius, color)            centred at (x, y)
    box = win.rectangle(x, y, width, height, color)   top-left corner at (x, y)
    label = win.text(x, y, message, color, size)      centred at (x, y)

Changing shapes
    win.move_to(ball, x, y)              put the shape at (x, y)
    win.set_color(ball, 'blue')          colour names, or codes like '#ff8800'
    win.set_size(ball, radius)           for a circle
    win.set_size(box, width, height)     for a rectangle
    win.set_size(label, size)            for text
    win.set_text(label, message)         change what the text says
    win.remove(ball)                     delete the shape
    win.clear()                          delete every shape
    win.set_background('black')          change the background colour

Showing what you've drawn
    win.show()            draw this frame, then wait a moment (1/30 second)
    win.pause(seconds)    draw, then wait that many seconds
    win.done()            keep the window open until you close it
                          (make this the last line of your program)
    win.is_open()         True until the window is closed

Mouse
    win.wait_for_click()  stop here until the window is clicked
    win.was_clicked()     True if the window was clicked since you last asked
    win.click_x(), win.click_y()    where the last click was
    win.mouse_x(), win.mouse_y()    where the mouse pointer is right now

Keyboard
    win.key_down('Left')       True while that key is held down
    win.key_pressed('space')   True if the key was pressed since you last asked
    Key names: 'Left', 'Right', 'Up', 'Down', 'space', 'Return',
               and letters/digits like 'a' or '7'.

Step mode
    win = Window(600, 400, step=True)
    Each win.show() waits until you press the SPACE BAR (or click in the
    window), and the title bar shows the frame number.  Print your variables each frame and you can
    check your trace table one frame at a time.
"""

import time
import tkinter as tk

__all__ = ['Window']


class Window:
    """A window to draw and animate shapes in.  See the top of anim.py."""

    def __init__(self, width=600, height=400, title='CSCI 131',
                 background='white', step=False, fps=30):
        _check_number(width, 'the window width')
        _check_number(height, 'the window height')
        _check_number(fps, 'fps')
        if width <= 0 or height <= 0:
            raise ValueError('The window width and height must be bigger than 0.')
        if fps <= 0:
            raise ValueError('fps (frames per second) must be bigger than 0.')

        self.width = width
        self.height = height
        self._title = str(title)
        self._step = bool(step)
        self._frame_time = 1.0 / fps
        self._last_frame = time.perf_counter()
        self._frame = 0
        self._open = True

        # what each shape is, plus what we need to redraw it
        self._shapes = {}

        # input state
        self._clicked = False
        self._click_x = 0
        self._click_y = 0
        self._mouse_x = 0
        self._mouse_y = 0
        self._keys_down = set()
        self._keys_pressed = set()
        self._space_for_step = False
        self._waiting_for_step = False
        self._step_hint_shown = False

        self._root = tk.Tk()
        self._root.title(self._title)
        self._root.resizable(False, False)
        self._root.protocol('WM_DELETE_WINDOW', self._on_close)
        self._background = self._check_color(background)
        self._canvas = tk.Canvas(self._root, width=width, height=height,
                                 background=self._background,
                                 highlightthickness=0)
        self._canvas.pack()

        self._canvas.bind('<Button-1>', self._on_click)
        self._canvas.bind('<Motion>', self._on_motion)
        self._root.bind('<KeyPress>', self._on_key_press)
        self._root.bind('<KeyRelease>', self._on_key_release)

        # bring the window to the front and give it the keyboard
        self._root.lift()
        self._root.attributes('-topmost', True)
        self._root.after_idle(self._root.attributes, '-topmost', False)
        self._root.focus_force()
        self._canvas.focus_set()
        self._pump()

    # ----------------------------------------------------------- shapes

    def circle(self, x, y, radius, color='black'):
        """Make a circle centred at (x, y).  Gives back its number."""
        self._check_open()
        _check_number(x, 'x')
        _check_number(y, 'y')
        _check_number(radius, 'the radius')
        color = self._check_color(color)
        shape = self._canvas.create_oval(x - radius, y - radius,
                                         x + radius, y + radius,
                                         fill=color, outline='')
        self._shapes[shape] = {'kind': 'circle', 'x': x, 'y': y,
                               'radius': radius}
        return shape

    def rectangle(self, x, y, width, height, color='black'):
        """Make a rectangle whose top-left corner is at (x, y)."""
        self._check_open()
        _check_number(x, 'x')
        _check_number(y, 'y')
        _check_number(width, 'the width')
        _check_number(height, 'the height')
        color = self._check_color(color)
        shape = self._canvas.create_rectangle(x, y, x + width, y + height,
                                              fill=color, outline='')
        self._shapes[shape] = {'kind': 'rectangle', 'x': x, 'y': y,
                               'width': width, 'height': height}
        return shape

    def text(self, x, y, message, color='black', size=20):
        """Write text centred at (x, y).  The message can be a number."""
        self._check_open()
        _check_number(x, 'x')
        _check_number(y, 'y')
        _check_number(size, 'the text size')
        color = self._check_color(color)
        shape = self._canvas.create_text(x, y, text=str(message), fill=color,
                                         font=('Arial', _font_size(size)))
        self._shapes[shape] = {'kind': 'text', 'x': x, 'y': y, 'size': size}
        return shape

    # ------------------------------------------------- changing shapes

    def move_to(self, shape, x, y):
        """Put a shape at (x, y): a circle's or text's centre, a rectangle's top-left corner."""
        self._check_open()
        info = self._check_shape(shape)
        _check_number(x, 'x')
        _check_number(y, 'y')
        info['x'] = x
        info['y'] = y
        self._place(shape, info)

    def set_color(self, shape, color):
        """Change a shape's colour."""
        self._check_open()
        self._check_shape(shape)
        self._canvas.itemconfigure(shape, fill=self._check_color(color))

    def set_size(self, shape, size, height=None):
        """Change a shape's size.

        circle:     win.set_size(ball, radius)
        rectangle:  win.set_size(box, width, height)
        text:       win.set_size(label, size)
        """
        self._check_open()
        info = self._check_shape(shape)
        kind = info['kind']
        _check_number(size, 'the size')
        if kind == 'rectangle':
            if height is None:
                raise TypeError('A rectangle needs a width AND a height: '
                                'win.set_size(box, width, height)')
            _check_number(height, 'the height')
            info['width'] = size
            info['height'] = height
        else:
            if height is not None:
                raise TypeError('A ' + kind + ' has only one size: '
                                'win.set_size(shape, size)')
            if kind == 'circle':
                info['radius'] = size
            else:
                info['size'] = size
                self._canvas.itemconfigure(shape, font=('Arial', _font_size(size)))
        self._place(shape, info)

    def set_text(self, shape, message):
        """Change what a piece of text says.  The message can be a number."""
        self._check_open()
        info = self._check_shape(shape)
        if info['kind'] != 'text':
            raise TypeError('set_text only works on text made with win.text(...); '
                            'shape ' + str(shape) + ' is a ' + info['kind'] + '.')
        self._canvas.itemconfigure(shape, text=str(message))

    def remove(self, shape):
        """Delete a shape from the window."""
        self._check_open()
        self._check_shape(shape)
        self._canvas.delete(shape)
        del self._shapes[shape]

    def clear(self):
        """Delete every shape in the window."""
        self._check_open()
        self._canvas.delete('all')
        self._shapes.clear()

    def set_background(self, color):
        """Change the background colour."""
        self._check_open()
        self._background = self._check_color(color)
        self._canvas.configure(background=self._background)

    # --------------------------------------------------------- showing

    def show(self):
        """Draw the current frame, then wait a moment (1/30 second)."""
        if not self._open:
            return
        self._frame = self._frame + 1
        if self._step:
            self._wait_for_space()
        else:
            self._sleep_until(self._last_frame + self._frame_time)
        self._last_frame = time.perf_counter()

    def pause(self, seconds):
        """Draw what's there now, then wait that many seconds."""
        _check_number(seconds, 'seconds')
        if not self._open:
            return
        if self._step:
            self._frame = self._frame + 1
            self._wait_for_space()
        else:
            self._sleep_until(time.perf_counter() + seconds)
        self._last_frame = time.perf_counter()

    def done(self):
        """Keep the window open until it is closed.  Put this last."""
        if not self._open:
            return
        self._root.title(self._title + '  (finished, close the window to end)')
        self._root.mainloop()

    def is_open(self):
        """True until the window has been closed."""
        return self._pump()

    # ----------------------------------------------------------- mouse

    def wait_for_click(self):
        """Stop here until the window is clicked."""
        self._check_open()
        old_title = self._root.title()
        self._root.title(self._title + '  (click in the window)')
        self._clicked = False
        while self._pump() and not self._clicked:
            time.sleep(0.01)
        self._clicked = False
        if self._open:
            self._root.title(old_title)
        self._last_frame = time.perf_counter()

    def was_clicked(self):
        """True if the window was clicked since the last time you asked."""
        self._check_open()
        self._pump()
        answer = self._clicked
        self._clicked = False
        return answer

    def click_x(self):
        """The x of the last click."""
        return self._click_x

    def click_y(self):
        """The y of the last click."""
        return self._click_y

    def mouse_x(self):
        """The x of the mouse pointer right now."""
        return self._mouse_x

    def mouse_y(self):
        """The y of the mouse pointer right now."""
        return self._mouse_y

    # -------------------------------------------------------- keyboard

    def key_down(self, key):
        """True while that key is being held down, e.g. win.key_down('Left')."""
        self._check_open()
        self._pump()
        return _key_name(key) in self._keys_down

    def key_pressed(self, key):
        """True if the key was pressed since the last time you asked."""
        self._check_open()
        self._pump()
        name = _key_name(key)
        if name in self._keys_pressed:
            self._keys_pressed.discard(name)
            return True
        return False

    # -------------------------------------------------------- internal

    def __repr__(self):
        return '<Window ' + str(self.width) + ' x ' + str(self.height) + '>'

    def _place(self, shape, info):
        kind = info['kind']
        x = info['x']
        y = info['y']
        if kind == 'circle':
            r = info['radius']
            self._canvas.coords(shape, x - r, y - r, x + r, y + r)
        elif kind == 'rectangle':
            self._canvas.coords(shape, x, y, x + info['width'], y + info['height'])
        else:
            self._canvas.coords(shape, x, y)

    def _pump(self):
        if self._open:
            try:
                self._root.update()
            except tk.TclError:
                self._open = False
        return self._open

    def _sleep_until(self, deadline):
        # Sleep in short slices so the window stays responsive.
        while self._pump():
            left = deadline - time.perf_counter()
            if left <= 0:
                break
            time.sleep(min(left, 0.02))

    def _wait_for_space(self):
        if not self._step_hint_shown:
            print('[anim] Step mode: click the window, then press SPACE '
                  '(or click again) for each frame.')
            self._step_hint_shown = True
        self._root.title(self._title + '  (frame ' + str(self._frame) +
                         ': press SPACE or click for the next frame)')
        self._space_for_step = False
        self._waiting_for_step = True
        while self._pump() and not self._space_for_step:
            time.sleep(0.01)
        self._waiting_for_step = False
        self._space_for_step = False
        # a step-mode space press shouldn't also count as the program's own key press
        self._keys_pressed.discard('space')

    def _check_open(self):
        if not self._open:
            raise SystemExit

    def _check_shape(self, shape):
        if isinstance(shape, bool) or not isinstance(shape, int):
            raise TypeError('Expected a shape (the number that win.circle(...), '
                            'win.rectangle(...) or win.text(...) gave back), '
                            'but got ' + repr(shape) + '.')
        if shape not in self._shapes:
            raise ValueError('There is no shape number ' + str(shape) +
                             ' in this window. Maybe it was removed, or the '
                             'number came from somewhere else?')
        return self._shapes[shape]

    def _check_color(self, color):
        if not isinstance(color, str):
            raise TypeError('A colour should be a string like \'red\' or '
                            '\'#ff8800\', but got ' + repr(color) + '.')
        try:
            self._root.winfo_rgb(color)
        except tk.TclError:
            raise ValueError(repr(color) + ' is not a colour Python knows. '
                             'Try a name like \'red\', \'skyblue\' or '
                             '\'darkgreen\', or a code like \'#ff8800\'.') from None
        return color

    def _on_close(self):
        self._open = False
        try:
            self._root.destroy()
        except tk.TclError:
            pass

    def _on_click(self, event):
        # Clicking gives the window the keyboard (needed on macOS, where
        # a new window often isn't the active one).
        try:
            self._canvas.focus_force()
        except tk.TclError:
            pass
        if self._waiting_for_step:
            # in step mode, a click means "next frame", not a program click
            self._space_for_step = True
            return
        self._clicked = True
        self._click_x = event.x
        self._click_y = event.y

    def _on_motion(self, event):
        self._mouse_x = event.x
        self._mouse_y = event.y

    def _on_key_press(self, event):
        name = event.keysym.lower()
        if name == 'space':
            self._space_for_step = True
        if name not in self._keys_down:
            self._keys_pressed.add(name)
        self._keys_down.add(name)

    def _on_key_release(self, event):
        self._keys_down.discard(event.keysym.lower())


def _check_number(value, what):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        message = what + ' should be a number, but got ' + repr(value)
        if isinstance(value, str):
            message = message + ' (that is a string; did you forget int() or float()?)'
        raise TypeError(message + '.')


def _key_name(key):
    if not isinstance(key, str):
        raise TypeError('A key name should be a string like \'Left\' or \'a\', '
                        'but got ' + repr(key) + '.')
    return key.lower()


def _font_size(size):
    return max(1, int(round(size)))
