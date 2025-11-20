import json
import math
from typing import Dict, List, Tuple

from src.core.paths import data_path

def calculer_distance(point1, point2):
    """
    Calcule la distance entre deux points.
    point1 et point2 sont des listes de deux nombres [x, y]
    """
    # On récupère les coordonnées x et y des deux points
    x1 = point1[0]  # x du premier point
    y1 = point1[1]  # y du premier point
    x2 = point2[0]  # x du deuxième point
    y2 = point2[1]  # y du deuxième point
    
    # On calcule la différence des x et des y
    diff_x = x2 - x1
    diff_y = y2 - y1
    
    # On calcule la distance avec le théorème de Pythagore
    distance = math.sqrt(diff_x * diff_x + diff_y * diff_y)
    return distance


def dijkstra(depart: Tuple[int, int], produits: Dict[str, Tuple[int, int]], produits_a_visiter: List[str]) -> List[str]:
    """
    Trouve le chemin optimal pour visiter les produits sélectionnés en partant du point de départ.
    
    Args:
        depart: Coordonnées du point de départ (entrée du magasin)
        produits: Dictionnaire des positions de tous les produits
        produits_a_visiter: Liste des noms des produits à visiter
    
    Returns:
        Liste ordonnée des produits à visiter pour le chemin optimal
    """
    # Initialisation
    non_visites = set(produits_a_visiter)  #La liste des produits à visiter
    chemin = []  #Le chemin optimal
    position_actuelle = depart  #La position du depart
    
    # Tant qu'il reste des produits à visiter
    while non_visites:
        # Trouver le produit le plus proche
        produit_plus_proche = None
        distance_min = float('inf')
        
        for produit in non_visites:   #On parcourt la liste des produits non visiter
            dist = calculer_distance(position_actuelle, produits[produit])
            if dist < distance_min:     #Si la distance est plus petite que la distance minimale 
                distance_min = dist     #on met à jour la distance minimale et le produit le plus proche
                produit_plus_proche = produit
        
        # Ajouter ce produit au chemin 
        chemin.append(produit_plus_proche)
        #Ce deplacer vers ce produit
        position_actuelle = produits[produit_plus_proche]
        #Enlever ce produit de la liste des produits non visiter
        non_visites.remove(produit_plus_proche)
    
    return chemin

def calculer_chemin_optimal(produits_selectionnes: List[str]) -> List[str]:
    """
    Cette fonction prend en entrée une liste de produits qu'on veut acheter 
    
    Args:
        produits_selectionnes: Liste des noms des produits à visiter
    
    Returns:
        Liste ordonnée des produits à visiter pour le chemin optimal
    """
    try:
        # Charger les positions depuis le fichier JSON
        with data_path("positions_produits_essai.json").open("r", encoding='utf-8') as f:
            data = json.load(f)
        
        # On récupère les position 
        entree = tuple(data["entree_magasin"])
        positions_produits = {k: tuple(v) for k, v in data["positions_produits"].items()}
        
        # Vérifier que tous les produits sélectionnés existent
        for produit in produits_selectionnes:
            if produit not in positions_produits:
                raise ValueError(f"Le produit '{produit}' n'existe pas dans la liste des produits")
        
        # Calculer le chemin optimal
        chemin = dijkstra(entree, positions_produits, produits_selectionnes)
        
        # Afficher le chemin
        print("\nChemin optimal :")
        print(f"1. Départ : Entrée du magasin ({entree})")
        for i, produit in enumerate(chemin, 2):
            print(f"{i}. {produit} : {positions_produits[produit]}")
        
        return chemin
        
    except FileNotFoundError:
        print("Erreur : Le fichier positions_produits_essai.json n'existe pas")
        return []
    except json.JSONDecodeError:
        print("Erreur : Le fichier positions_produits_essaie.json est mal formaté")
        return []
    except Exception as e:
        print(f"Erreur : {str(e)}")
        return []