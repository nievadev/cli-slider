import subprocess, os, termios, sys, cursor
from blessings import Terminal
from Getch import Getch

CONTENT = "content"
TERM = Terminal()
H = TERM.height
W = TERM.width
FD = sys.stdin.fileno()
SETTINGS = termios.tcgetattr(FD)

def just_exit():
    termios.tcsetattr(FD, termios.TCSADRAIN, SETTINGS)
    cursor.show()
    exit()

def main():
    ch = None
    
    files = subprocess.check_output(["ls"]).decode("utf-8").split("\n")
    files.pop()
    index = 0

    while True:
        max_num = 0

        with open(files[index], "r") as f:
            os.system("clear")
            
            lines = f.readlines()

        for i in range(len(lines)):
            if len(lines[i]) > max_num:
                max_num = len(lines[i])

        print("\n" * (H - 5))

        for i, line in enumerate(lines):
            with TERM.location(W // 2 - max_num // 2, H // 2 + i - len(lines) // 2):
                print(line, end = "")

        try:
            ch = Getch(1)

        except KeyboardInterrupt:
            just_exit()
         
        else:
            if ch() == "d" and index != len(files) - 1:
                index += 1

            elif ch() == "a" and index != 0:
                index -= 1

            elif ch() == "o":
                just_exit()

try:
    os.chdir("./" + CONTENT)
except FileNotFoundError:
    subprocess.call(["mkdir", CONTENT])
    os.chdir("./" + CONTENT)
    subprocess.call(["touch", "1"])
    
    with open("1", "r+") as f:
        f.write("Hello! This was automatically created by the script!\n")

finally:
    main()
