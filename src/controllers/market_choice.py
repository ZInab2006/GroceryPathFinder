from src.views.market_choice import SupermarcheVue
from src.controllers.shopping_list import ControleurListeCourses

class SupermarcheControleur:
    """
    Contrôleur pour la sélection du supermarché.
    Fait le lien entre la vue de sélection du supermarché et la liste de courses.
    """
    
    def __init__(self):
        """
        Initialise le contrôleur :
        - Crée la vue de sélection du supermarché
        - Configure le lien entre la vue et ce contrôleur
        - Initialise le contrôleur de liste de courses à None
        """
        self.__vue = SupermarcheVue()  # Création de la vue
        self.__vue.set_controleur(self)  # Configuration du lien vue-contrôleur
        self.__controleur_liste_courses = None  # Contrôleur de liste de courses (créé plus tard)

    def show(self):
        """
        Affiche la vue de sélection du supermarché.
        Méthode appelée pour démarrer l'interface de sélection.
        """
        self.__vue.show()

    def supermarche_choisi(self, nom_supermarche):
        """
        Gère l'événement de sélection d'un supermarché.
        
        Args:
            nom_supermarche (str): Le nom du supermarché sélectionné
            
        Actions:
        1. Affiche le supermarché choisi dans la console
        2. Crée le contrôleur de liste de courses s'il n'existe pas
        3. Affiche l'interface de liste de courses
        4. Ferme la vue de sélection du supermarché
        """
        print(f"Supermarche choisi : {nom_supermarche}")
        if not self.__controleur_liste_courses:
            self.__controleur_liste_courses = ControleurListeCourses()
        self.__controleur_liste_courses.show()
        self.__vue.close() 