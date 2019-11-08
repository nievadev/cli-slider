import sys, termios, tty, subprocess, os

content = "content"

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    os.chdir("./" + content)
except FileNotFoundError:
    subprocess.call(["mkdir", content])
    os.chdir("./" + content)
    subprocess.call(["touch", "1"])
    
    with open("1", "r+") as f:
        f.write("Hello! This was automatically created by the script!\n")
else:
    files = subprocess.check_output(["ls"]).decode("utf-8").split("\n")
    files.pop()

    for file_name in files:
        with open(file_name, "r") as f:
            os.system("clear")

            content = f.read()

            print(content)

            tty.setraw(fd)

            ch = sys.stdin.read(1)

termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
