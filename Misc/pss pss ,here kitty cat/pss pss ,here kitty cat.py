import base64
import time
# ===== FLAG =====
def get_flag():
    return "flag{n3tw0rk_br34k3r}"

ENCODED_FLAG = base64.b64encode(get_flag().encode())

# ===== PASSWORD =====
FIRST_PART = "duper"
SECOND_PART = "pass"
REAL_PASSWORD = FIRST_PART + SECOND_PART

# XOR key
XOR_KEY = 0x42
SECRET = [ord(c) ^ XOR_KEY for c in FIRST_PART]


# ===== Stage 1 =====
def check_first_part(user_input):
    score = 0

    for i in range(min(len(user_input), len(FIRST_PART))):
     if (ord(user_input[i]) ^ XOR_KEY) == SECRET[i]:
        score += 1
    time.sleep(0.05)
    return score


# ===== Stage 2 =====
def generate_hint():
    real = SECOND_PART.encode()
    key = 0x37
    encoded = bytes([b ^ key for b in real])
    packet = b"PKT" + len(encoded).to_bytes(1, "big") + encoded
    return base64.b64encode(packet)


# ===== MAIN =====
def send(msg):
    print(msg, flush=True)

def recv():
    try:
        return input().strip()
    except:
        return ""


send("=== Secure Auth v5 ===")

# ===== Stage 1 =====
while True:
    send("Stage 1 - Enter first part:")
    part1 = recv()

    if not part1:
        exit()

    result = check_first_part(part1)

    if result == len(FIRST_PART):
        send("[+] First part correct!")
        break
    else:
        send(f"{result}/{len(FIRST_PART)} correct")

# ===== Stage 2 =====
hint = generate_hint()
send("\nCaptured packet:")
send(hint.decode())

send("Hint: PKT format → magic | length | data")
send("Hint: Data is XORed")

# ===== Stage 3 =====
while True:
    send("\nEnter full password:")
    full = recv()

    if not full:
        exit()

    if full == REAL_PASSWORD:
        send("Access granted!")
        send(ENCODED_FLAG.decode())
        break
    else:
        send("Wrong password")