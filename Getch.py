import termios, sys, tty, os, cursor

FD = sys.stdin.fileno()
SETTINGS = termios.tcgetattr(FD)

class Getch:
    def __init__(self, chars = 1, raw = False):
        if raw:
            tty.setraw(FD)
        else:
            tty.setcbreak(FD)

        cursor.hide()

        self.ch = sys.stdin.read(chars)

        termios.tcsetattr(FD, termios.TCSADRAIN, SETTINGS)

        cursor.show()

    def __call__(self):
        return self.ch

    def __str__(self):
        return self.ch
