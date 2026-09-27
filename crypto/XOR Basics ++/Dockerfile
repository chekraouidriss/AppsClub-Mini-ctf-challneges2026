FROM python:3.9

WORKDIR /app

COPY generate.py .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 8000

CMD ["./entrypoint.sh"]