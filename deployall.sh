#!/bin/bash

BASE_DIR="/root/challenges"

WEB_PORT=10001
NC_PORT=11001
SSH_PORT=12001

echo "[+] Deploying challenges..."

docker rm -f $(docker ps -aq) 2>/dev/null

for category in "$BASE_DIR"/*; do
    [ -d "$category" ] || continue

    cat_name=$(basename "$category")

    for chall in "$category"/*; do
        [ -d "$chall" ] || continue

        name=$(basename "$chall")
        full_name="${cat_name}_${name}"

        echo "[+] Processing $full_name..."

        case "$cat_name" in
            web)
                PORT=$WEB_PORT
                MAP="$PORT:80"
                MEM="128m"
                CPU="0.3"
                ((WEB_PORT++))
                ;;

            pwn|nc|misc)
                PORT=$NC_PORT
                MAP="$PORT:1337"
                MEM="128m"
                CPU="0.3"
                ((NC_PORT++))
                ;;

            ssh)
                PORT=$SSH_PORT
                MAP="$PORT:22"
                MEM="256m"
                CPU="0.5"
                ((SSH_PORT++))
                ;;

            *)
                echo "[-] Unknown category $cat_name, skipping..."
                continue
                ;;
        esac

        echo "    → Port: $PORT"

        docker build -t "$full_name" "$chall"

        docker run -d \
            --name "$full_name" \
            -p "$MAP" \
            --memory="$MEM" \
            --cpus="$CPU" \
            --pids-limit=100 \
            --restart=always \
            "$full_name"

    done
done

echo "[+] Deployment complete!"
docker ps