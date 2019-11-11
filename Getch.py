import termios, sys, tty, cursor, os

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

        self.turn_normal()

    def __call__(self):
        return self.ch

    def __str__(self):
        return self.ch

    @staticmethod
    def turn_normal(flush = True):
        if flush:
            os.system("clear")

        termios.tcsetattr(FD, termios.TCSADRAIN, SETTINGS)
        cursor.show()
