FROM python:3.10-slim

RUN apt update && apt install -y socat gcc

# Create player
RUN useradd -m player

WORKDIR /home/player

COPY shell.py .
COPY enable.secret .
COPY readflag.c .

# Compile SUID binary
RUN gcc readflag.c -o readflag

# 🔥 CRITICAL: set ownership BEFORE dropping permissions
RUN chown root:root readflag && \
    chmod 4755 readflag

# Protect secret
RUN chmod 600 enable.secret

# Flag (root only)
COPY flag.txt /flag.txt
RUN chown root:root /flag.txt && chmod 400 /flag.txt

# Give player ownership of working dir
RUN chown -R player:player /home/player

USER player

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"timeout 60 python3 shell.py",pty,stderr