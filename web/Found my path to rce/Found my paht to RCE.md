Title: Apache Gone Wrong

Description:
Our admin misconfigured Apache after a recent update.
Can you find the hidden flag?


I tried accessing /cgi-bin/ directly but it didn’t work.
Someone said Apache had issues with encoded paths like 
Not sure what that means...

Hint:
Strange URL encoding might help...



cheat sheet
    - use gobuster to Run directory scan:
        >> gobuster dir -u url -w commonwords.txt
    