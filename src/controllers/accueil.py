from src.views.accueil import AccueilVue
from src.controllers.market_choice import SupermarcheControleur

class AccueilControleur:
    def __init__(self):
        """Initialise le contrôleur avec sa vue"""
        self.__vue = AccueilVue()
        self.__vue.set_controleur(self)
        self.__controleur_supermarche = None
    
    def on_button_clicked(self):
        """Gère l'action du clic sur le bouton"""
        # Fermer la fenêtre d'accueil
        self.__vue.close()
        
        # Création et affichage de la fenêtre de choix du supermarché
        self.__controleur_supermarche = SupermarcheControleur()
        self.__controleur_supermarche.show()
    
    def show(self):
        """Affiche la vue"""
        self.__vue.show() 