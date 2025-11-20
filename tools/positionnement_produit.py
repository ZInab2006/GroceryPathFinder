import json
import sys
from pathlib import Path

import tkinter as tk
from PIL import Image, ImageTk

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.core.paths import data_path, image_path  # noqa: E402

# === Paramètres ===
PLAN_IMAGE = image_path("plan_main_quadrille.png")
TAILLE_CASE = 20  # en pixels 
LARGEUR_MAX = 1120  # Largeur maximale de l'image en pixels
HAUTEUR_MIN = 600   # Hauteur minimale de la fenêtre

# Dimensions de la grille
NOMBRE_CASES = 50  # Grille 50x50
LARGEUR_GRILLE = NOMBRE_CASES * TAILLE_CASE  # 1000 pixels
HAUTEUR_GRILLE = NOMBRE_CASES * TAILLE_CASE  # 1000 pixels

# Liste des produits à placer
produits = [
    "lait", "pâtes", "beurre", "papier toilette", "savon",
    "chips", "shampooing", "brosse à dents", "bananes", "brioche",
    "riz", "yaourt", "eau Minérale", "oeufs", "pommes",
    "pain d'épices", "farine", "café moulu", "petits pois", "sardine"
]

# === Variables globales ===
produit_index = 0
positions = {}
point_depart = None
point_fin = None 
mode = "depart"  

def calculer_coordonnees(event):
    """Calcule les coordonnées de la grille à partir des coordonnées de la souris"""
    # Calculer les coordonnées en fonction de la grille
    x = min(event.x // TAILLE_CASE, NOMBRE_CASES - 1)
    y = min(event.y // TAILLE_CASE, NOMBRE_CASES - 1)
    
    return x, y

def sauvegarder_positions():
    data = {
        "entree_magasin": point_depart,  
        "positions_produits": positions,
        "point_fin": point_fin # Nouveau : sauvegarder le point de fin
    }
    try:
        with data_path("positions_produits.json").open("w", encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(" Données sauvegardées avec succès dans positions_produits.json")
        
        # Vérification des données sauvegardées
        with data_path("positions_produits.json").open("r", encoding='utf-8') as f:
            data_verifiee = json.load(f)
            print("\nVérification des données sauvegardées :")
            print(f"Entrée du magasin : {data_verifiee['entree_magasin']}")
            print(f"Nombre de produits placés : {len(data_verifiee['positions_produits'])}")
            print(f"Point de fin : {data_verifiee['point_fin']}") # Nouveau : afficher le point de fin
    except Exception as e:
        print(f" Erreur lors de la sauvegarde : {str(e)}")

def clic(event):
    global produit_index, point_depart, mode, point_fin
    
    # Calculer les coordonnées de la grille
    x, y = calculer_coordonnees(event)
    print(f"Position cliquée : ({event.x}, {event.y}) -> Coordonnées grille : ({x}, {y})")

    if mode == "depart":
        point_depart = (x, y)
        canvas.create_text(x * TAILLE_CASE + 10, y * TAILLE_CASE + 10, 
                         text="Entrée", fill="green", anchor="center")
        mode = "produits"
        print("Entrée du magasin placée à :", point_depart)
        print("Maintenant, placez le produit :", produits[produit_index])
    
    elif mode == "produits":
        if produit_index < len(produits):
            nom = produits[produit_index]
            positions[nom] = (x, y)
            print(f"{nom} placé à : ({x}, {y})")
            canvas.create_text(x * TAILLE_CASE + 10, y * TAILLE_CASE + 10, 
                             text=nom, fill="blue", anchor="center")
            produit_index += 1

            if produit_index < len(produits):
                print("Maintenant, placez le produit :", produits[produit_index])
            else:
                mode = "fin" # Passer au mode de placement du point de fin
                print("Tous les produits sont placés. Placez maintenant le point de fin.")
        
    elif mode == "fin":
        point_fin = (x, y)
        canvas.create_text(x * TAILLE_CASE + 10, y * TAILLE_CASE + 10, 
                         text="Fin", fill="red", anchor="center")
        print("Point de fin placé à :", point_fin)
        # Sauvegarder et vérifier les positions
        sauvegarder_positions()
        root.quit()

# === Fenêtre Tkinter ===
root = tk.Tk()
root.title("Positionnement des produits")

# Charger et redimensionner l'image
img = Image.open(PLAN_IMAGE)
# Vérifier les dimensions de l'image
print(f"Dimensions originales de l'image : {img.width}x{img.height} pixels")
print(f"Dimensions attendues de la grille : {LARGEUR_GRILLE}x{HAUTEUR_GRILLE} pixels")

# Calculer les nouvelles dimensions en conservant les proportions
rapport = LARGEUR_MAX / img.width
nouvelle_taille = (LARGEUR_MAX, int(img.height * rapport))
img = img.resize(nouvelle_taille, Image.Resampling.LANCZOS) 
photo = ImageTk.PhotoImage(img)

print(f"Dimensions finales de l'image : {photo.width()}x{photo.height()} pixels")

# Créer le canvas avec les dimensions de l'image
canvas = tk.Canvas(root, width=photo.width(), height=photo.height())
canvas.pack()

# Afficher l'image
canvas.create_image(0, 0, anchor="nw", image=photo)

# Configurer la taille minimale de la fenêtre
root.minsize(LARGEUR_MAX, HAUTEUR_MIN)

# Lier l'événement de clic
canvas.bind("<Button-1>", clic)

print("Placez d'abord l'entrée du magasin")
root.mainloop()