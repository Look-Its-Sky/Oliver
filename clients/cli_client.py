import socket

usr_input = input("Input the host and port (eg: 127.0.0.1:6500)")
HOSTNAME, PORT = usr_input.split(":")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    s.connect((HOSTNAME, PORT))
    s.sendall(b"message")
    
    data = s.recv(1024)

print(f"Recieved: {data!r}")