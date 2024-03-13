import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print("Connected to server")
    except Exception as e:
        print("Error connecting to server:", e)
    else:
        message = "Hello from client"
        client_socket.send(message.encode())
        print("Message sent to server:", message)

        response = client_socket.recv(1024).decode()
        print("Server response:", response)

        client_socket.close()

if __name__ == "__main__":
    main()

