from PIL import Image

# flag in hex
hex_data = "466c61677b427233616b6f75745f316e5f436f6c30727d"

# split into RGB triplets
colors = []
for i in range(0, len(hex_data), 6):
    chunk = hex_data[i:i+6]
    if len(chunk) < 6:
        chunk = chunk.ljust(6, '0')
    r = int(chunk[0:2], 16)
    g = int(chunk[2:4], 16)
    b = int(chunk[4:6], 16)
    colors.append((r, g, b))

# create image
width = len(colors)
height = 1

img = Image.new("RGB", (width, height))
img.putdata(colors)

img.save("chall.png")
print("[+] chall.png created")