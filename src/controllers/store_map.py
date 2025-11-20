import json

from src.views.store_map import PlanVue
from src.models.routing import calculer_chemin_optimal
from src.core.paths import data_path

# === Paramètres de dimensionnement ===
TAILLE_CASE = 20  # en pixels
LARGEUR_MAX = 1120  # Largeur maximale de l'image en pixels
HAUTEUR_MIN = 600   # Hauteur minimale de la fenêtre

class ControleurPlan:
    def __init__(self):
        """Initialise le contrôleur avec sa vue"""
        self.__vue = PlanVue()
        self.__vue.set_controleur(self)
        self.__chemin_optimal = None
        self.__chemin_image = None
        # Définir les dimensions minimales de la fenêtre
        self.__vue.setMinimumSize(LARGEUR_MAX, HAUTEUR_MIN)

    def show(self):
        """Affiche la vue"""
        self.__vue.show()
        self.calculer_chemin()

    def image_sauvegardee(self, chemin_image):
        """Gère la sauvegarde de l'image du plan"""
        self.__chemin_image = chemin_image
        print(f"Image du plan sauvegardée : {chemin_image}")

    def calculer_chemin(self):
        try:
            # Lire la liste de courses
            with data_path("liste_courses.json").open("r", encoding='utf-8') as f:
                liste_courses = json.load(f)
            print("Liste de courses lue:", liste_courses)
            
            # Calculer le chemin optimal
            self.__chemin_optimal = calculer_chemin_optimal(liste_courses)
            print("Chemin optimal calculé:", self.__chemin_optimal)
            
            # Afficher le chemin sur le plan
            if self.__chemin_optimal:
                # Convertir les noms de produits en coordonnées
                with data_path("positions_produits.json").open("r", encoding='utf-8') as f:
                    positions = json.load(f)
                print("Positions des produits lues:", positions)
                
                # Créer la liste des points du chemin
                points_chemin = []
                
                # Ajouter le point de départ (entrée du magasin)
                if "entree_magasin" in positions:
                    point_depart = tuple(positions["entree_magasin"])
                    points_chemin.append((point_depart[0], point_depart[1], "Entrée"))
                    print(f"Point de départ ajouté: {point_depart}")
                
                # Ajouter les points des produits dans l'ordre du chemin optimal
                for produit in self.__chemin_optimal:
                    if produit in positions["positions_produits"]:
                        point = tuple(positions["positions_produits"][produit])
                        points_chemin.append((point[0], point[1], produit))
                        print(f"Point du produit {produit} ajouté: {point}")
                
                if "point_fin" in positions and positions["point_fin"] is not None:
                    point_fin = tuple(positions["point_fin"])
                    points_chemin.append((point_fin[0], point_fin[1], "Fin"))
                    print(f"Point de fin ajouté: {point_fin}")
                
                print("Points du chemin à afficher:", points_chemin)
                
                # Afficher le chemin
                if points_chemin:
                    self.__vue.afficher_chemin(points_chemin)
                else:
                    print("Aucun point à afficher dans le chemin")
            else:
                print("Aucun chemin optimal trouvé")
                
        except FileNotFoundError as e:
            print(f"Erreur : Fichier non trouvé - {e}")
        except json.JSONDecodeError as e:
            print(f"Erreur : Fichier JSON invalide - {e}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            import traceback
            traceback.print_exc() 