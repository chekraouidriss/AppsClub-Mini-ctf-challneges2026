import os

enabled = False

def help_cmd():
    if enabled:
        print("Commands: help, ls, id, cat, enable, strings, run")
    else:
        print("Commands: help, ls, id, enable, strings")

def enable_cmd():
    global enabled
    pwd = input("Password: ")

    try:
        with open("enable.secret") as f:
            secret = f.read().strip()
    except:
        print("Error")
        return

    if pwd == secret:
        enabled = True
        print("(enabled)")
    else:
        print("Wrong password")

def run_cmd():
    if not enabled:
        print("Not allowed")
        return

    cmd = input("Run: ")

    # 🔥 restrict commands (important)
    allowed = ["./readflag", "ls", "id"]

    if cmd not in allowed:
        print("Command not allowed")
        return

    os.system(cmd)

while True:
    cmd = input("mini-shell$ ")

    if cmd == "help":
        help_cmd()

    elif cmd.startswith("strings"):
        # 🔥 restrict file access
        if "enable.secret" in cmd:
            print("Access denied")
        else:
            os.system(cmd)

    elif cmd == "ls":
        os.system("ls")

    elif cmd == "id":
        os.system("id")

    elif cmd == "enable":
        enable_cmd()

    elif cmd == "run":
        run_cmd()

    elif cmd == "exit":
        break

    else:
        print("Unknown command")