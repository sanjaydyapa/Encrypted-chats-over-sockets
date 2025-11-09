import socket
import threading
from encryption_utils import load_key, decrypt_message, encrypt_message

KEY = load_key()

def handle_client(client_socket):
    
    
    print("[SERVER] New client connected.")
    
    try:
        while True:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break 

            decrypted_message = decrypt_message(encrypted_message, KEY)
            print(f"[CLIENT] says: {decrypted_message.decode('utf-8')}")

            reply = input("[YOU] > ")
            encrypted_reply = encrypt_message(reply.encode('utf-8'), KEY)
            client_socket.send(encrypted_reply)

    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    finally:
        print("[SERVER] Client disconnected.")
        client_socket.close()


def start_server():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    print("[SERVER] Server started and listening on port 9999...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[SERVER] Accepted connection from {addr}")
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()