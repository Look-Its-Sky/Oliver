import socket

HOSTNAME = "127.0.0.1"
PORT = 6500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOSTNAME, PORT))
    s.listen()

    conn, addr = s.accept()

    with conn:
        print(f"Connected to from {addr}")

        while True:
            data = conn.revc(1024)

            if not data:
                break

            conn.sendall(data)