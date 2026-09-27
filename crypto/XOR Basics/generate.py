import random
import string

key = 0x42

random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
flag = f"CTF{{xor_{random_part}}}"

encrypted = [format(ord(c) ^ key, "02x") for c in flag]

with open("/app/challenge.txt", "w") as f:
    f.write("Encrypted (hex):\n")
    f.write(" ".join(encrypted))
    f.write("\n\nKey: 0x42\n")

# Save flag (for validation)
with open("/app/flag.txt", "w") as f:
    f.write(flag)

