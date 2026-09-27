FROM php:8.2-apache

# Install useful tools
RUN apt-get update && apt-get install -y sudo

# Enable Apache modules if needed
RUN a2enmod rewrite

# Copy only the app
COPY src/ /var/www/html/

# Create low-priv user (for future privesc)
RUN useradd -m ctfuser

# Optional: controlled privilege escalation (safer than find)
# RUN chmod u+s /bin/bash   # ⚠️ Only if you WANT easy privesc

# Flag (optional)
# COPY flag.txt /root/flag.txt
# RUN chmod 400 /root/flag.txt

# 🔥 IMPORTANT: allow write for edit.php exploit
RUN chown -R www-data:www-data /var/www/html

# Allow writing ONLY where needed (better than 777 everywhere)
RUN chmod 775 /var/www/html
RUN chmod 666 /var/www/html/auth.php

EXPOSE 80