import json

from PyQt6.QtWidgets import QApplication

from src.views.shopping_list import VueListeCourses
from src.controllers.store_map import ControleurPlan
from src.core.paths import data_path

class ControleurListeCourses:
    def __init__(self):
        """Initialise le contrôleur et crée la vue"""
        self.__vue = VueListeCourses()
        self.__vue.set_controleur(self)
        self.__controleur_plan = None
        print("Contrôleur de la liste de courses initialisé")

    def show(self):
        """Affiche la vue"""
        print("Affichage de la vue liste de courses")
        # S'assurer que la vue est visible
        self.__vue.setVisible(True)
        self.__vue.show()
        # Forcer le traitement des événements
        QApplication.processEvents()
        print("Vue liste de courses affichée")

    def valider_liste(self, articles_selectionnes):
        """Gère la validation de la liste de courses"""
        try:
            print("Validation de la liste de courses")
            # Sauvegarde dans le fichier JSON
            with data_path("liste_courses.json").open("w", encoding="utf-8") as fichier:
                json.dump(articles_selectionnes, fichier, ensure_ascii=False, indent=4)
            print("Liste sauvegardée dans liste_courses.json")

            # Créer et afficher le contrôleur du plan
            print("Création du contrôleur du plan")
            self.__controleur_plan = ControleurPlan()
            print("Affichage du plan")
            self.__controleur_plan.show()
            
            # Fermer la fenêtre de liste de courses
            print("Fermeture de la vue liste de courses")
            self.__vue.close()
            
        except Exception as e:
            print(f"Erreur lors de la validation : {str(e)}")
            self.__vue.afficher_message(f"Erreur lors de la sauvegarde : {str(e)}") 