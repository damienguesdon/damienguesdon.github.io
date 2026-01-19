# 🚀 Damien Guesdon - CV Factory

Ce dépôt contient le moteur de génération de mon CV professionnel. Il s'agit d'une solution personnalisée permettant de générer un profil dynamique, bilingue (FR/EN) et responsive à partir de sources de données structurées.

## 🛠️ Stack Technique

- **Moteur de Rendu** : Python 3.11
- **Templating** : [Jinja2](https://palletsprojects.com/p/jinja/)
- **Source de Données** : YAML (Séparation stricte contenu/forme)
- **Front-end** : HTML5 & CSS3 (Variables CSS pour le support Dark/Light mode)
- **Automation CI/CD** : GitHub Actions
- **Qualité Code** : Ruff (Linting) & Black (Formatage)
- **Hébergement** : GitHub Pages

## ✨ Fonctionnalités

- **Bilingue (FR/EN)** : Bascule dynamique de la langue via l'interface.
- **Support Dark/Light Mode** : Détection automatique du thème système et bascule manuelle.
- **Génération Ciblée** : Support de fichiers d'overrides pour adapter le CV à des opportunités spécifiques (adaptation dynamique du résumé ou des compétences mises en avant).
- **Calcul Automatique** : Les années d'expérience globale sont recalculées dynamiquement à chaque génération.
- **Design Print-Ready** : Styles CSS optimisés pour l'impression et l'export PDF.

## 📂 Structure du Projet

```text
├── data/
│   ├── cv.yaml           # Données sources (Expériences, Compétences, etc.)
│   └── cv_custom.yaml    # Overrides pour une version spécifique (optionnel)
├── scripts/
│   └── generate_cv.py    # Script Python de génération du fichier HTML
├── src/
│   └── templates/
│       └── cv_template.html # Template Jinja2 maître
├── index.html            # CV généré (déployé automatiquement)
└── .github/workflows/    # Workflows d'automatisation (CI/CD)
```

## 🚀 Utilisation

### Installation
Le projet nécessite Python 3.11 et les dépendances Jinja2 et PyYAML.
```bash
pip install jinja2 pyyaml
```

### Génération locale
Pour générer la version standard :
```bash
python scripts/generate_cv.py
```

Pour générer une version spécifique (utilisant un fichier d'override correspondant dans `data/`) :
```bash
python scripts/generate_cv.py --target custom
```

## ⚙️ Automatisation

Le déploiement est entièrement automatisé via GitHub Actions :
1. Chaque modification de code ou de données est validée par **Ruff** (linting) et **Black** (formatage).
2. Après validation, le CV est régénéré et déployé sur **GitHub Pages**.
3. La gestion des versions est assurée par un tag de versioning injecté dynamiquement dans le code source du CV.

---
*Damien Guesdon*
