import base64

enc = base64.b64decode("VlxRV2tkeHljTyFjT3gjfHxPfSR+bQ==")

for key in range(256):
    flag = bytes([c ^ key for c in enc])
    
    if b"FLAG" in flag:
        print("Key:", key)
        print("Flag:", flag)