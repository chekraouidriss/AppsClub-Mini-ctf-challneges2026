FROM ubuntu:22.04

RUN apt update && apt install -y openssh-server sudo

# Create player
RUN useradd -m player && echo "player:letmein123" | chpasswd

# SSH setup
RUN mkdir /var/run/sshd

# Copy challenge files
COPY . /home/player
RUN chown -R player:player /home/player

# Place flag
RUN mkdir -p /.hidden && echo "flag{terminal_master}" > /.hidden/flag.txt
RUN chmod 700 /.hidden
RUN chmod 600 /.hidden/flag.txt

# Optional: restrict permissions
RUN chmod -R o-rwx /root

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]