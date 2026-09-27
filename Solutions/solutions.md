# Stenography

## Solution :  It's Like Music to My Eyes

### Step 1: Inspect the file

We are given an audio file:
hidden_message.wav

The challenge description hints that we should "look at sound differently".

### Step 2: Use spectrogram

Open the file using Audacity.

- Import hidden_message.wav
- Click on track name
- Change view to "Spectrogram"

### Step 3: Adjust view

- Zoom out (Ctrl + 3)
- Increase spectrogram gain if needed

### Step 4: Read the message

The hidden text appears in the spectrogram

## Solution :  LSB Secret

### Step 1: Inspect the file

We are given an image:
chall.png

The challenge title suggests Least Significant Bit (LSB) steganography.

### Step 2: Extract hidden data

Use stegano library:

```bash
python3 -c "from stegano import lsb; print(lsb.reveal('chall.png'))" 
```

## Solution :  When Goats are Flying
## Step 1: Analyze the image

We are given an image: image.jpg

Nothing obvious is visible, so we try steganography tools.

## Step 2: Use steghide

```bash
steghide info hidden.jpg
steghide extract -sf hidden.jpg

```


## Solution :  Corruption is Bad

## Step 1: Analyze file

We are given an image.

Using binwalk:

binwalk final.jpg

We find a ZIP archive inside.

## Step 2: Extract

binwalk -e final.jpg

We get corrupted.zip.

## Step 3: Fix archive

zip -FF corrupted.zip --out fixed.zip

## Step 4: Extract

unzip fixed.zip

We need a password.

## Step 5: Find password

The description hints:

"WALNUT"

## Step 6: Get flag

cat flag.txt

## Solution - Palette Prison

### Step 1: Analyze the image

We are given chall.png.

The image looks like random colors.

### Step 2: Extract pixel values

Using Python and PIL, extract RGB values.

### Step 3: Convert to hex

Each pixel represents 3 bytes (RGB).

Concatenate values into a hex string.

### Step 4: Decode hex

Convert hex to ASCII:

xxd -r -p

# Forensic
## Metadata lives Matter 

run exiftool and the flag is right there

## Hiddren in plain sight 
Solve

Player:

opens → broken image
uses:
hexedit surfingsquirrel.jpg

or:

xxd | tail
fixes header → image opens → flag visible


## delted but not goone 

fls -r disk.img
icat disk.img <inode>


# Cryptography

## Hidden Exchnage 
🧠 How players solve (important for you)

They will:

1. Recover a
for i in range(1, p):
    if pow(g, i, p) == A:
        a = i
        break
2. Compute shared secret
shared = pow(B, a, p)
3. Decrypt
key = shared % 256
cipher = base64.b64decode(cipher_b64)

flag = bytes([c ^ key for c in cipher])
print(flag)


# WEB

## Admin Access

Solution Path (for you)
Get token from /login
brute-force secret (rockyou, small list)
modify payload → "admin"
re-sign → access /admin

# Reverse Engineering
## Simple Checker


## Obfuscated Logic


# dns Step 1 — Initial Recon

Start by querying the TXT records:

dig @46.101.177.219 nicebowlofsoup.com TXT

👉 Response:

status: REFUSED
🧠 Observation
Server responds → DNS is alive ✅
But query is refused ❌
Recursion is disabled

👉 This suggests:

The server is restrictive… maybe another query method works

🔥 Step 2 — Try Zone Transfer (AXFR)

Since normal queries fail, try a zone transfer:

dig @46.101.177.219 nicebowlofsoup.com AXFR
🎯 Result

You get a full zone dump including:

TXT records
Fake data
RSA key chunks
Encrypted flag
🧠 Step 3 — Identify useful data

From the dump:

🔐 Encrypted flag
flag IN TXT "s7p204bmVTCz0RvYWx0wm22WEvo..."
❌ Fake key (trap)
oldkey IN TXT "-----BEGIN RSA PRIVATE KEY ... (invalid)"

👉 Ignore this

✅ Real key (fragmented)
chunk1 → -----BEGIN RSA PRIVATE KEY-----
chunk2 → ...
chunk3 → ...
chunk4 → ...
chunk5 → ...
chunk6 → -----END RSA PRIVATE KEY-----

👉 This is the real private key

🛠 Step 4 — Reconstruct RSA key

Create a file:

nano private.pem

Paste in correct order:

-----BEGIN RSA PRIVATE KEY-----
(chunk2)
(chunk3)
(chunk4)
(chunk5)
-----END RSA PRIVATE KEY-----

Save it.

🔐 Step 5 — Decode encrypted flag
1. Save ciphertext
echo "s7p204bmVTCz0RvYWx0..." > cipher.txt
2. Decode Base64
base64 -d cipher.txt > encrypted.bin
3. Decrypt using RSA
openssl rsautl -decrypt -inkey private.pem -in encrypted.bin
🏁 Step 6 — Get the flag
Flag{I_d0nt_ev3n_like_s0up}
🧠 Key Concepts Learned
DNS enumeration
Zone transfer (AXFR) vulnerability
Identifying misleading data
RSA decryption workflow
💡 Why this works

👉 The server allows:

Zone transfer (AXFR) to anyone

👉 This leaks:

Hidden records
Private key

👉 Which breaks encryption entirely

🔐 Real-world takeaway

This is a critical misconfiguration:

allow-transfer { any; };

👉 In real systems, this should be restricted:

allow-transfer { trusted-ip; };
🧩 Challenge Flow Summary
TXT query → blocked
AXFR → full dump
Extract:
ciphertext
RSA key chunks
Rebuild key
Decrypt
Flag

one bit closer to root : How Players Solve It
Intended path:
Find a way to modify files (you can add this via LFI, upload, or shell access)
Flip ONE BIT in auth.php
Remove/invert the !
Login with:
username: admin
password: anything