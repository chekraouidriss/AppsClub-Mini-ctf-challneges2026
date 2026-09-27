# ===== hidden_exchange (NC challenge) =====

FROM python:3.10-slim

RUN apt update && apt install -y socat

WORKDIR /app

COPY server.py .

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 server.py",pty,stderr