import random
import base64

# Small enough to brute force, but not instant
p = 104729  # prime
g = 5

a = random.randint(1000, 5000)
b = random.randint(1000, 5000)

A = pow(g, a, p)
B = pow(g, b, p)

shared = pow(B, a, p)

FLAG = b"FLAG{this_1s_h3ll_m4n}"

# XOR encryption
key = shared % 256
cipher = bytes([c ^ key for c in FLAG])

print("=== PUBLIC DATA ===")
print(f"p = {p}")
print(f"g = {g}")
print(f"A = {A}")
print(f"B = {B}")
print(f"cipher = {base64.b64encode(cipher).decode()}")