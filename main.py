import sys, termios, tty, subprocess, os
from blessings import Terminal

CONTENT = "content"
TERM = Terminal()
H = TERM.height
W = TERM.width

def main():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    ch = None
    
    files = subprocess.check_output(["ls"]).decode("utf-8").split("\n")
    files.pop()
    index = 0

    while True:
        lens = list()
        max_num = 0

        with open(files[index], "r") as f:
            os.system("clear")
            
            lines = f.readlines()

        for i, line in enumerate(lines):
            lens.append(len(line))

        print("\n" * (H - 5))

        lens.sort()
        
        max_num = lens[-1]

        for i, line in enumerate(lines):
            with TERM.location(W // 2 - max_num // 2, H // 2 + i):
                print(line, end = "")

        tty.setcbreak(fd)

        ch = sys.stdin.read(1)
         
        if ch == "d" and index != len(files) - 1:
            index += 1

        elif ch == "a" and index != 0:
            index -= 1

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
