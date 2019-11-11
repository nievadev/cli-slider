import subprocess, os
from blessings import Terminal
from Getch import Getch

CONTENT = "content"
TERM = Terminal()
H = TERM.height
W = TERM.width

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

        for i, line in enumerate(lines):
            max_num = len(line) if len(line) > len(lines[i - 1]) else len(lines[i - 1])

        print("\n" * (H - 5))

        for i, line in enumerate(lines):
            with TERM.location(W // 2 - max_num // 2, H // 2 + i):
                print(line, end = "")

        try:
            ch = Getch(1)

        except KeyboardInterrupt:
            os.system("clear")
            Getch.turn_normal()
            exit()
         
        else:
            if ch() == "d" and index != len(files) - 1:
                index += 1

            elif ch() == "a" and index != 0:
                index -= 1

            elif ch() == "o":
                os.system("clear")
                Getch.turn_normal()
                exit()

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
