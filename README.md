
[![Vérification PEP8 - flake8](https://github.com/Alia-1to1code/git_learning/actions/workflows/pep8.yml/badge.svg)](https://github.com/Alia-1to1code/git_learning/actions/workflows/pep8.yml)
![Tests](https://github.com/Alia-1to1code/git_learning/actions/workflows/test.yml/badge.svg)
![Docs](https://github.com/Alia-1to1code/git_learning/actions/workflows/docs.yml/badge.svg)


# Apprentissage de Git et GitHub

📖 **[Documentation en ligne](https://Alia-1to1code.github.io/git_learning/)**

## Description

`git_learning` est un dépôt d'exemple utilisé durant les cours pour apprendre :
- les bases de Git (init, add, commit, push)
- la gestion des branches et des pull requests
- la résolution de conflits
- l'automatisation avec **GitHub Actions** (linting, tests)
- le déploiement de documentation via **GitHub Pages** (MkDocs)
- les principes CI/CD simples

<img src="https://1to1code-pictures.s3.eu-west-par.io.cloud.ovh.net/git/final.png" alt="github" style="width:80%; height:auto; display:block; margin:0 auto;" /> 

## Démarrage rapide

```bash
git clone https://github.com/Alia-1to1code/git_learning.git
cd git_learning
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
pip install -r requirements-dev.txt requirements-docs.txt
```

Exécuter les tests et le linteur :

```bash
pytest tests/
flake8 .
```

Prévisualiser la documentation locale :

```bash
mkdocs serve
# puis ouvrir http://127.0.0.1:8000
```

## Structure du dépôt

- `docs/` : sources MkDocs (documentation)
- `.github/workflows/` : workflows GitHub Actions (tests, docs, pep8)
- `src/` : code source de l'exemple (module `calculator`)
- `tests/` : tests unitaires
- `requirements-*.txt` : dépendances pour dev (tests, mkdocs, linters)

## Contribuer

Suggestions rapides : ouvrez une branche `feature/...`, faites vos changements, puis créez une Pull Request. Les workflows vérifieront automatiquement le style et les tests.

