from Crypto.Util.number import *

flag = bytes_to_long(b"FLAG{sm4ll_attck}")

e = 3
n = getPrime(512) * getPrime(512)

c = pow(flag, e, n)

print("n =", n)
print("e =", e)
print("c =", c)