FROM python:3.10-slim

RUN apt update && apt install -y socat

RUN useradd -m player
WORKDIR /home/player

COPY server.py .
RUN chown -R player:player /home/player

USER player

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"timeout 30 python3 server.py",pty,stderr