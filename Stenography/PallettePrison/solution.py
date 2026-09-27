from PIL import Image

img = Image.open("chall.png")
pixels = list(img.getdata())

hex_data = "".join(f"{r:02x}{g:02x}{b:02x}" for r, g, b in pixels)

print(bytes.fromhex(hex_data).decode())