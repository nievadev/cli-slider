import sys, termios, tty, subprocess, os

content = "content"

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

cursor.hide()

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

            content = f.readlines()

            for i, line in enumerate(content):
                max_num = len(line) if len(line) > len(content[i - 1]) else len(content[i - 1])

                print(line, end = "")

            # print(max_num)

            tty.setraw(fd)
            ch = sys.stdin.read(1)
            while ch != "d":
                ch = sys.stdin.read(1)

            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
