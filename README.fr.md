# QuickCart – Guidage intelligent en magasin

QuickCart est une application PyQt6 réalisée dans le cadre de la SAÉ C12 (Graphes & IHM). Elle guide l'utilisateur à travers un supermarché en calculant l'itinéraire optimal pour récupérer tous les articles de sa liste de courses.

## Configuration rapide

```bash
python -m venv .venv
source .venv/bin/activate  # Ou .venv\Scripts\activate sous Windows
pip install -r requirements.txt
python main.py
```

## Organisation du projet

```
.
├── assets/
│   ├── images/                # Logos et plans du magasin
│   └── styles/                # Feuilles de style QSS
├── data/                      # Jeux de données (positions, listes…)
├── docs/                      # Compte-rendu, notice utilisateur
├── src/
│   ├── controllers/           # Couche Contrôleur (logique d'orchestration)
│   ├── core/paths.py          # Utilitaires communs pour les chemins
│   ├── models/                # Couche Modèle (algorithmes, calculs)
│   └── views/                 # Couche Vue (interfaces PyQt6)
├── tools/                     # Scripts annexes (génération de données, maquettes)
├── main.py                    # Point d'entrée de l'application
└── requirements.txt
```

Cette structure explicite l'implémentation du motif MVC :
- `src/models/` contient l'algorithme de calcul d'itinéraire (Dijkstra).
- `src/views/` regroupe les fenêtres PyQt6 (accueil, choix du magasin, liste, plan).
- `src/controllers/` fait le lien entre la vue et le modèle.

## Données et ressources

Les fichiers JSON nécessaires (`liste_courses.json`, `positions_produits*.json`) se trouvent dans `data/`. Les scripts du dossier `tools/` permettent de recalculer les plans quadrillés ou de repositionner graphiquement les produits ; ils utilisent les mêmes chemins centralisés via `src.core.paths`.

