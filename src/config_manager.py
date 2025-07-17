import json
import base64
import os

def load_config(config_path="config/enhancer_config.json"):
    """Charge la configuration depuis un fichier JSON."""
    default_config = {
        "server_address": base64.b64encode(b"127.0.0.1").decode(),
        "server_port": base64.b64encode(b"9999").decode(),
        "buffer_size": 1024,
        "separator": "<sep>",
        "exit_command": "exit",
        "info_command": "collect_info"
    }
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
        return {**default_config, **config}
    return default_config