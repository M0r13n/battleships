CSI = '\x1b['


class Ansi(object):
    FULL_RESET = 0

    def __init__(self):
        for name in dir(self):
            if not name.startswith('__'):
                setattr(self, name, CSI + str(getattr(self, name)) + 'm')


class Text(Ansi):
    DEFAULT = 39
    [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE] = range(30, 38)


class Background(Ansi):
    DEFAULT = 49
    [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE] = range(40, 48)


class Cursor(Ansi):
    BLINK = 5


Text = Text()
Background = Background()
Cursor = Cursor()
