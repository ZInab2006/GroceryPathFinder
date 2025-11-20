# QuickCart – Smart in-store guidance

QuickCart is a PyQt6 application built for the SAÉ C12 project (Graphs & UI). It navigates a supermarket for you by computing the optimal path to collect every item in your shopping list.

> 🇫🇷 Besoin d’une version française ? Consultez [`README.fr.md`](README.fr.md).

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py
```

## Project layout

```
.
├── assets/
│   ├── images/                # Logos and store maps
│   └── styles/                # QSS stylesheets
├── data/                      # JSON datasets (product positions, saved lists…)
├── docs/                      # Reports, user notice
├── src/
│   ├── controllers/           # Controller layer (orchestration logic)
│   ├── core/paths.py          # Shared path helpers
│   ├── models/                # Model layer (algorithms, computations)
│   └── views/                 # View layer (PyQt6 UIs)
├── tools/                     # Utility scripts (data generation, prototyping)
├── main.py                    # Application entry point
└── requirements.txt
```

This layout makes the MVC pattern explicit:
- `src/models/` hosts the pathfinding logic (Dijkstra variant).
- `src/views/` groups all PyQt6 windows (home, store selection, list, map).
- `src/controllers/` connects the UI to the domain logic.

## Data & assets

All required JSON files (`liste_courses.json`, `positions_produits*.json`) live in `data/`. Helper scripts under `tools/` reuse the same centralized path helpers (`src.core.paths`) to redraw grids or reposition products, so assets stay in sync between tooling and the main app.
