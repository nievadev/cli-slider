import sys, termios, tty, subprocess, os
from blessings import Terminal

CONTENT = "content"
TERM = Terminal()

def main():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    ch = None
    
    files = subprocess.check_output(["ls"]).decode("utf-8").split("\n")
    files.pop()
    index = 0

    while True:
        with open(files[index], "r") as f:
            os.system("clear")
            
            lines = f.readlines()

        lines.append("\n" * (TERM.height - 10))

        for i, line in enumerate(lines):
            max_num = len(line) if len(line) > len(lines[i - 1]) else len(lines[i - 1])

            print(line, end = "")

        print(max_num)

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
