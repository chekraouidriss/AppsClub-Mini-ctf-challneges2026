FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y socat

WORKDIR /app

COPY app.py .

RUN useradd -m ctfuser
USER ctfuser

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 /app/app.py",pty,stderr