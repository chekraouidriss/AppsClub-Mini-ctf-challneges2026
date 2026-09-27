import random
import string

# Generate random key (0x00 → 0xFF)
key = random.randint(0, 255)

# Generate random flag
random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
flag = f"CTF{{xor_{random_part}}}"

# Encrypt
encrypted = [format(ord(c) ^ key, "02x") for c in flag]

# Save challenge (what players see)
with open("/app/challenge.txt", "w") as f:
    f.write("Encrypted (hex):\n")
    f.write(" ".join(encrypted))
    f.write("\n\n")

    # OPTION A (easy)
    f.write(f"Key: 0x{key:02x}\n")

    # OPTION B (medium)
    # f.write("Hint: single-byte XOR\n")

# Save real flag
with open("/app/flag.txt", "w") as f:
    f.write(flag)

# Debug (you see this in docker logs)
print("[+] Key:", hex(key))
print("[+] Flag:", flag)