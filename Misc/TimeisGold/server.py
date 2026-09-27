import time
import sys

FLAG = "flag{tim1ng_1s_k3y}"

def check_flag(user_input):
    for i in range(min(len(user_input), len(FLAG))):
        if user_input[i] != FLAG[i]:
            return False
        time.sleep(0.15)
    return user_input == FLAG

print("Enter the flag:", flush=True)

try:
    user_input = input().strip()
except:
    sys.exit()

if check_flag(user_input):
    print("Correct!")
else:
    print("Wrong!")