FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# generate the stego image
RUN python script.py

EXPOSE 8000

CMD ["python", "-m", "http.server", "8000"]