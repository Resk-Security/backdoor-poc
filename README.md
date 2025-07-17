# Cursor Code Enhancer

**Cursor Code Enhancer** est une extension open-source pour [Cursor](https://cursor.com) qui améliore votre expérience de codage en analysant dynamiquement votre codebase, en générant des rapports détaillés, et en optimisant les suggestions de code basées sur l'IA. Ce projet est conçu pour les développeurs souhaitant maximiser leur productivité dans Cursor.

## Fonctionnalités
- **Analyse de Codebase** : Collecte des métadonnées sur votre projet pour fournir des suggestions contextuelles.
- **Génération de Rapports** : Crée des rapports sur la structure et les métriques de votre code.
- **Intégration avec Cursor** : S'exécute directement dans le terminal intégré de Cursor.
- **Compatibilité** : Supporte Python, JavaScript, TypeScript, et plus.

## Installation
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/fake-user/cursor-code-enhancer.git
   cd cursor-code-enhancer
   ```
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Configurez le serveur local pour l'analyse des données :
   ```bash
   python server/server.py
   ```
4. Exécutez l'un des scripts principaux :
   - Analyse de codebase : `python src/cursor_optimizer.py`
   - Analyse détaillée : `python src/codebase_analyzer.py`
   - Génération de rapports : `python src/report_generator.py`

## Configuration dans Cursor
Pour une exécution automatique, ajoutez ceci à `~/.cursor/settings.json` :
```json
{
  "cursor.onStartup": [
    "python3 /path/to/cursor-code-enhancer/src/cursor_optimizer.py"
  ]
}
```

## Documentation
- [Installation détaillée](docs/installation.md)
- [Guide d'utilisation](docs/usage.md)

## Prérequis
- Python 3.8+
- Cursor (téléchargeable sur [cursor.com](https://cursor.com))
- Un serveur local (fourni dans `server/server.py`)

## Contribution
Les contributions sont les bienvenues ! Consultez notre [guide de contribution](CONTRIBUTING.md) pour commencer.

## Licence
Ce projet est sous licence MIT - voir [LICENSE](LICENSE) pour plus de détails.

**Note** : Ce projet est destiné à des tests académiques. Assurez-vous d'exécuter le serveur local pour activer toutes les fonctionnalités.