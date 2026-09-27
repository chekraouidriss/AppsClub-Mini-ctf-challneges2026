import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.io.wavfile import write

text = 'Flag{Th3_real_H3aring_A1d}'

try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 80)
except:
    font = ImageFont.load_default()

# Measure text size
dummy_img = Image.new("L", (1, 1))
dummy_draw = ImageDraw.Draw(dummy_img)
bbox = dummy_draw.textbbox((0, 0), text, font=font)

text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# Add padding (IMPORTANT)
padding_x = 100
padding_y = 50

width = text_w + padding_x * 2
height = text_h + padding_y * 2

# Create final image
img = Image.new("L", (width, height), color=0)
draw = ImageDraw.Draw(img)

# Center text with padding
position = (padding_x, padding_y)

draw.text(position, text, fill=255, font=font)

img.save("flag.png")
print("[+] flag.png created (no cropping)")


img = np.array(img)
img = np.flipud(img)  # flip for spectrogram

img = img / 255.0

height, width = img.shape

sample_rate = 44100
duration_per_column = 0.02
samples_per_column = int(sample_rate * duration_per_column)

audio = []

for x in range(width):
    column = img[:, x]
    t = np.linspace(0, duration_per_column, samples_per_column)

    signal = np.zeros(samples_per_column)

    for y in range(height):
        if column[y] > 0:  # skip black pixels for speed
            freq = 300 + (y / height) * 5000
            signal += column[y] * np.sin(2 * np.pi * freq * t)

    audio.append(signal)

audio = np.concatenate(audio)

# =========================
# STEP 3: NORMALIZE
# =========================
max_val = np.max(np.abs(audio))
if max_val > 0:
    audio = audio / max_val

write("hidden_message.wav", sample_rate, audio.astype(np.float32))

print("[+] hidden_message.wav generated")
print("[✓] Done! Open in Audacity → Spectrogram → Ctrl+3")