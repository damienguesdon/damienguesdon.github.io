# Damien Guesdon - CV

Site du CV de Damien Guesdon, publié sur GitHub Pages : une page d'accueil et des CV ciblés par poste, bilingues (FR/EN), avec thème clair ou sombre et styles d'impression.

## Où se fait le travail

- La source est dans une forge privée. Ce dépôt GitHub en est le **miroir** : il ne se modifie pas directement (une poussée faite ici fait échouer le miroir).
- Chaque page HTML est **écrite à la main** et autonome : ses styles et son script sont dans le fichier.

## Pages publiées

| Fichier | Poste visé |
|---|---|
| `index.html` | CTO Infrastructure & IA (page d'accueil) |
| `cto_infra_ia.html` | redirige vers la page d'accueil |
| `responsable_ingenierie_infrastructure.html` | Responsable de l'ingénierie infrastructure (langue imposée par l'ancre `#fr` ou `#en` du lien) |
| `directeur_infrastructure_securite.html` | Directeur Infrastructure, Production & Sécurité |
| `directeur_operations_techniques.html` | Directeur des Opérations Techniques |
| `directeur_de_site.html` | Directeur de Site |
| `DSI_banque.html` | DSI / CIO / CTO |
| `Fractionnal_CTO.html` | DSI / CIO |
| `IT_manager.html` | Responsable Infrastructure |
| `Responsable_IA.html` | Directeur Technique & Responsable IA |
| `AI_Platform.html` | Directeur Data & IA |
| `AI_architect.html` | Expert IA & Architecte de Solutions |
| `ia_architect.html` | Architecte & Référent Technique IA |
| `ai_strategy.html` | Expert Conseil IA, Stratégie et Transformation |
| `SRE.html` | Senior Site Reliability Engineer & MLOps Architect |

`CV_Damien_Guesdon_FR.pdf` et `Resume_Damien_Guesdon_EN.pdf` sont les PDF proposés en téléchargement par la page d'accueil.

## Publication

Le workflow `.github/workflows/ci.yml` tourne à chaque poussée reçue par le miroir :

1. `validate` : Ruff et Black sur le code Python du dépôt.
2. `deploy` (branche `main` seulement) : publie **tout le dépôt**, tel quel, sur GitHub Pages. Rien n'est généré : ce qui est versionné est ce qui est servi.

## Ancien générateur (ne sert plus)

`scripts/generate_cv.py`, `src/templates/cv_template.html`, `data/cv.yaml` et `pixi.toml` sont l'ancienne chaîne de génération (YAML + Jinja2). Les données datent de février 2026 et les pages sont modifiées à la main depuis : **ne pas lancer le script**, il écraserait `index.html` (sortie par défaut) avec un contenu périmé. Leur retrait reste à décider.
