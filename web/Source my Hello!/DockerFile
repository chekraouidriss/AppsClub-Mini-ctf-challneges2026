FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*
COPY . /usr/share/nginx/html/

COPY flag.txt /flag.txt

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]