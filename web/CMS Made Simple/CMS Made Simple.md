simple-ctf/
├── Dockerfile
├── docker-compose.yml
├── cms/
├── apache.conf
├── setup.sql
├── flag.txt
├── root_flag.txt
└── exploit_hint.txt (optional for testing)

Target IP: http://your-server-ip




Challenge  — User Access (Improved & More Complex)
🎯 Goal

Make players chain multiple steps instead of just logging in.

🧠 New Concept

Instead of:

login → read /var/www/html/flag.txt

We do:

exploit → dump DB → crack password → login → pivot → find hidden creds → user flag

💡 Implementation Idea
1. CMS creds are NOT enough for SSH
CMS login works ✔️
SSH login with same creds ❌

👉 This forces deeper enumeration.

2. Add a hidden backup file

Inside web root:

/var/www/html/backup.zip

Or better:

/var/www/html/.backup/.env

Content:

DB_USER=devuser
DB_PASS=Sup3rHidden!
3. Create system user
useradd devuser
echo "devuser:Sup3rHidden!" | chpasswd
4. User flag location
/home/devuser/user.txt
flag{pivoting_like_a_pro}
📝 Updated Challenge Description
Target: http://<your-server-ip>

You gained access to the web application.

Can you move deeper into the system and obtain a real user shell?

Submit the user flag.
💡 Hint (optional)
Web apps often leave sensitive files behind.
🧠 Skills Tested
Web enumeration (gobuster)
Finding hidden files
Credential reuse
Lateral movement (web → system user)