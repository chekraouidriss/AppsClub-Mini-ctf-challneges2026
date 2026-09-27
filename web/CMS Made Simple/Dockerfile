# ===== CMS Made Simple (Web + PrivEsc Challenge) =====

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    apache2 \
    mysql-server \
    php \
    php-mysql \
    openssh-server \
    sudo \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Enable Apache modules
RUN a2enmod rewrite

# Setup SSH
RUN mkdir /var/run/sshd
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# 🔥 FIX: Ensure MySQL works over TCP
RUN sed -i 's/^skip-networking/#skip-networking/' /etc/mysql/mysql.conf.d/mysqld.cnf || true
RUN sed -i 's/^bind-address.*/bind-address = 127.0.0.1/' /etc/mysql/mysql.conf.d/mysqld.cnf

# Remove default page
RUN rm -f /var/www/html/index.html

# Copy CMS
COPY cms/ /var/www/html/
COPY apache.conf /etc/apache2/sites-available/000-default.conf

# Copy DB setup
COPY setup.sql /setup.sql

# Flags
COPY flaginitial.txt /var/www/html/flag.txt
COPY rootflag.txt /root/root.txt

# Hidden vuln
RUN mkdir -p /var/www/html/.backup
COPY hidden/.env /var/www/html/.backup/.env

# Create user
RUN useradd -m devuser && \
    echo "devuser:password123" | chpasswd

# Encrypted user flag
RUN echo "0209170c1e09584403100c180c3a155859563b04291b17494c" > /home/devuser/flag.enc && \
    chown devuser:devuser /home/devuser/flag.enc && \
    chmod 600 /home/devuser/flag.enc

# Permissions
RUN chown -R www-data:www-data /var/www/html

# Expose ports
EXPOSE 80
EXPOSE 22

# 🚀 FIXED STARTUP
CMD ["/bin/bash", "-c", "\
mysqld_safe & \
sleep 5 && \
mysql < /setup.sql && \
service ssh start && \
apachectl -D FOREGROUND \
"]