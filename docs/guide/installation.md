# Installation

## Prérequis

- Python 3.10 ou supérieur
- Git installé et configuré

## Étapes

1. Cloner le dépôt :

```bash
git clone https://github.com/Alia-1to1code/git_learning.git
cd git_learning
``` 

2. Créer un environnement virtuel (recommandé) :

```bash
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate       # Windows
``` 

3. Installer les dépendances de développement :

```bash
pip install -r requirements-dev.txt
``` 

4. Vérifier l'installation :

```bash
pytest tests/ -v
``` 

!!! success "Succès"
    Si tous les tests passent, l'installation est correcte.