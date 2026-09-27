# ===== digging-for-soup (DNS challenge) =====
# flag chiffrer west db.soup.com
FROM ubuntu:22.04

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y bind9 dnsutils && \
    apt clean

COPY named.conf /etc/bind/named.conf
COPY named.conf.local /etc/bind/named.conf.local
COPY named.conf.options /etc/bind/named.conf.options
COPY db.soup.com /etc/bind/db.soup.com

EXPOSE 53/tcp
EXPOSE 53/udp

CMD ["named", "-g", "-c", "/etc/bind/named.conf"]