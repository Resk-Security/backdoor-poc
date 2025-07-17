# API Documentation - Code Enhancer

## Vue d'ensemble

Code Enhancer fournit une API simple pour analyser et optimiser la structure de projets. Cette documentation décrit toutes les fonctions publiques disponibles.

## Modules

### `src.main`

Module principal contenant les fonctions d'analyse et d'optimisation.

#### `analyze_project_structure()`

Analyse la structure du projet courant et envoie les données au serveur.

**Paramètres :** Aucun

**Retourne :** Aucun

**Exemple :**
```python
from src import main

main.analyze_project_structure()
```

#### `process_optimization(config)`

Traite les optimisations en fonction des données reçues du serveur.

**Paramètres :**
- `config` (dict) : Configuration du système

**Retourne :** Aucun

**Exemple :**
```python
from src import main, config_manager

config = config_manager.load_config()
main.process_optimization(config)
```

#### `execute_task(task)`

Exécute une tâche d'optimisation spécifique.

**Paramètres :**
- `task` (str) : Commande à exécuter

**Retourne :**
- `str` : Résultat de l'exécution de la tâche

**Exemple :**
```python
from src import main

result = main.execute_task("ls -la")
print(result)
```

#### `main()`

Point d'entrée principal de l'application.

**Paramètres :** Aucun

**Retourne :** Aucun

**Exemple :**
```python
from src import main

if __name__ == "__main__":
    main.main()
```

### `src.network_utils`

Module pour la communication réseau avec le serveur d'analyse.

#### `initialize_connection()`

Initialise une connexion sécurisée avec le serveur d'analyse.

**Paramètres :** Aucun

**Retourne :** Aucun

**Lève :**
- `ConnectionError` : Si la connexion échoue

**Exemple :**
```python
from src import network_utils

try:
    network_utils.initialize_connection()
    print("Connexion établie")
except ConnectionError as e:
    print(f"Erreur de connexion : {e}")
```

#### `send_data(data, config)`

Envoie des données au serveur pour analyse.

**Paramètres :**
- `data` (str) : Données à envoyer
- `config` (dict) : Configuration du système

**Retourne :** Aucun

**Exemple :**
```python
from src import network_utils, config_manager

config = config_manager.load_config()
network_utils.send_data("Données d'analyse", config)
```

#### `receive_data(config)`

Reçoit des instructions du serveur pour optimisation.

**Paramètres :**
- `config` (dict) : Configuration du système

**Retourne :**
- `str` : Données reçues du serveur

**Exemple :**
```python
from src import network_utils, config_manager

config = config_manager.load_config()
response = network_utils.receive_data(config)
print(f"Réponse du serveur : {response}")
```

#### `close_connection()`

Ferme la connexion avec le serveur.

**Paramètres :** Aucun

**Retourne :** Aucun

**Exemple :**
```python
from src import network_utils

network_utils.close_connection()
```

#### `main()`

Point d'entrée pour l'interface en ligne de commande.

**Paramètres :** Aucun

**Retourne :** Aucun

**Exemple :**
```python
from src import network_utils

if __name__ == "__main__":
    network_utils.main()
```

### `src.config_manager`

Module pour la gestion de la configuration.

#### `load_config()`

Charge la configuration depuis les fichiers de configuration.

**Paramètres :** Aucun

**Retourne :**
- `dict` : Configuration chargée

**Exemple :**
```python
from src import config_manager

config = config_manager.load_config()
print(f"Adresse du serveur : {config['server_address']}")
```

## Configuration

### Format de configuration

Le système utilise un fichier JSON pour la configuration :

```json
{
    "server_address": "base64_encoded_host",
    "server_port": "base64_encoded_port",
    "buffer_size": 1024,
    "exit_command": "exit",
    "info_command": "collect_info",
    "separator": "|"
}
```

### Paramètres de configuration

| Paramètre | Type | Description | Défaut |
|-----------|------|-------------|--------|
| `server_address` | str | Adresse du serveur (encodée en base64) | - |
| `server_port` | str | Port du serveur (encodé en base64) | - |
| `buffer_size` | int | Taille du buffer pour la communication | 1024 |
| `exit_command` | str | Commande pour quitter l'application | "exit" |
| `info_command` | str | Commande pour collecter les informations | "collect_info" |
| `separator` | str | Séparateur pour les messages | "|" |

## Gestion des erreurs

### Exceptions communes

#### `ConnectionError`
Levée quand la connexion au serveur échoue.

```python
try:
    network_utils.initialize_connection()
except ConnectionError as e:
    print(f"Impossible de se connecter au serveur : {e}")
```

#### `FileNotFoundError`
Levée quand un fichier de configuration est manquant.

```python
try:
    config = config_manager.load_config()
except FileNotFoundError as e:
    print(f"Fichier de configuration manquant : {e}")
```

#### `ValueError`
Levée quand les données reçues sont invalides.

```python
try:
    response = network_utils.receive_data(config)
except ValueError as e:
    print(f"Données invalides reçues : {e}")
```

## Exemples d'utilisation

### Exemple complet

```python
from src import main, network_utils, config_manager
import logging

# Configuration de la journalisation
logging.basicConfig(level=logging.INFO)

try:
    # Charger la configuration
    config = config_manager.load_config()
    
    # Initialiser la connexion
    network_utils.initialize_connection()
    
    # Analyser le projet
    main.analyze_project_structure()
    
    # Traiter les optimisations
    main.process_optimization(config)
    
except Exception as e:
    logging.error(f"Erreur : {e}")
    
finally:
    # Fermer la connexion
    network_utils.close_connection()
```

### Exemple avec gestion d'erreurs avancée

```python
from src import main, network_utils, config_manager
import logging
import sys

def main_with_error_handling():
    """Exemple avec gestion d'erreurs complète."""
    
    # Configuration de la journalisation
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('code_enhancer.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    try:
        # Charger la configuration
        config = config_manager.load_config()
        logging.info("Configuration chargée avec succès")
        
        # Initialiser la connexion
        network_utils.initialize_connection()
        logging.info("Connexion au serveur établie")
        
        # Analyser le projet
        main.analyze_project_structure()
        logging.info("Analyse du projet terminée")
        
    except FileNotFoundError as e:
        logging.error(f"Fichier de configuration manquant : {e}")
        sys.exit(1)
        
    except ConnectionError as e:
        logging.error(f"Erreur de connexion : {e}")
        sys.exit(1)
        
    except Exception as e:
        logging.error(f"Erreur inattendue : {e}")
        sys.exit(1)
        
    finally:
        # Fermer la connexion
        try:
            network_utils.close_connection()
            logging.info("Connexion fermée")
        except Exception as e:
            logging.warning(f"Erreur lors de la fermeture : {e}")

if __name__ == "__main__":
    main_with_error_handling()
```

## Bonnes pratiques

### 1. Gestion des ressources

Toujours utiliser un bloc `try/finally` pour s'assurer que les connexions sont fermées :

```python
try:
    network_utils.initialize_connection()
    # Votre code ici
finally:
    network_utils.close_connection()
```

### 2. Journalisation

Utilisez la journalisation pour le debugging :

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Début de l'analyse")
# Votre code ici
logger.info("Analyse terminée")
```

### 3. Validation des données

Validez toujours les données reçues du serveur :

```python
response = network_utils.receive_data(config)
if not response:
    logger.warning("Aucune réponse reçue du serveur")
    return
```

### 4. Configuration

Utilisez des valeurs par défaut pour la configuration :

```python
config = config_manager.load_config()
buffer_size = config.get('buffer_size', 1024)
exit_command = config.get('exit_command', 'exit')
```

## Support

Pour plus d'informations ou en cas de problème :

1. Consultez la [documentation principale](README.md)
2. Vérifiez les [issues GitHub](https://github.com/codeenhancer/code-enhancer/issues)
3. Créez une nouvelle issue avec les détails du problème 