import socket
import base64

HOST = "0.0.0.0"
PORT = 5000

# ===== GENERATED VALUES (PASTE HERE) =====
p = 104729
g = 5
A = 12345
B = 67890
cipher_b64 = "VlxRV2tkeHljTyFjT3gjfHxPfSR+bQ=="
# ========================================

cipher = base64.b64decode(cipher_b64)


def handle_client(conn):
    try:
        conn.send(b"=== Hidden Exchange ===\n\n")

        conn.send(f"p = {p}\n".encode())
        conn.send(f"g = {g}\n".encode())
        conn.send(f"A = {A}\n".encode())
        conn.send(f"B = {B}\n\n".encode())

        conn.send(b"Encrypted message:\n")
        conn.send(cipher_b64.encode() + b"\n\n")

        conn.send(b"Recover the shared secret and decrypt the message.\n")
        conn.send(b"Submit flag:\n")

        user = conn.recv(1024).strip()

        if user == b"FLAG{d1ff13_h3llm4n_m3d1um}":
            conn.send(b"Correct!\n")
        else:
            conn.send(b"Wrong!\n")

    except:
        pass

    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(50)

    print(f"[+] Running on port {PORT}")

    while True:
        conn, _ = server.accept()
        handle_client(conn)


if __name__ == "__main__":
    main()