# ===== JWT Madness (Flask challenge) =====

FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask pyjwt

# ta t injecter flag a ismail flag

EXPOSE 5000

# IMPORTANT: bind to 0.0.0.0
CMD ["python3", "script.py"]