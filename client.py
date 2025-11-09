import socket
from encryption_utils import load_key, encrypt_message, decrypt_message

KEY = load_key()
SERVER_IP = '127.0.0.1' 
SERVER_PORT = 9999

def start_client():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print("[CLIENT] Connected to the server.")

        while True:
            message = input("[YOU] > ")
            if message.lower() == 'quit':
                break

            encrypted_message = encrypt_message(message.encode('utf-8'), KEY)
            client_socket.send(encrypted_message)

            encrypted_reply = client_socket.recv(1024)
            if not encrypted_reply:
                print("[CLIENT] Server closed the connection.")
                break
            
            decrypted_reply = decrypt_message(encrypted_reply, KEY)
            print(f"[SERVER] says: {decrypted_reply.decode('utf-8')}")

    except ConnectionRefusedError:
        print("[ERROR] Connection refused. Is the server running?")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    finally:
        client_socket.close()
        print("[CLIENT] Connection closed.")

if __name__ == "__main__":
    start_client()