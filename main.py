"""
Projet : QuickCart - Application de guidage en supermarché
BUT Informatique - SAÉ C12-Graphes-IHM
IUT du Littoral Côte d'Opale
2024-2025

Réalisé par :
- OUTMANI Zinab
- CUIFFA Enzo

Description :
Application permettant de trouver le chemin optimal pour faire ses courses
dans un supermarché en utilisant l'algorithme de Dijkstra.

Fonctionnalités :
- Sélection du supermarché
- Création de liste de courses
- Calcul du chemin optimal
- Affichage du chemin sur le plan du magasin
"""

import sys

from PyQt6.QtWidgets import QApplication

from src.controllers.accueil import AccueilControleur
from src.core.paths import style_path

def main():
    # Création de l'application
    app = QApplication(sys.argv)
    
    # Chargement du style commun
    common_style = style_path("common.qss").read_text(encoding="utf-8")
    app.setStyleSheet(common_style)
    
    # Création et affichage de la fenêtre d'accueil
    controleur = AccueilControleur()
    controleur.show()
    
    # Lancement de l'application
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 