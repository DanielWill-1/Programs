import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}...")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from client: {data.decode()}")
            conn.sendall(b"Message received by server!")
