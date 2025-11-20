import sys
from pathlib import Path

from PIL import Image, ImageDraw

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.core.paths import image_path  # noqa: E402

def quadriller_image(image_path, taille_case=20):
    """
    Quadrille une image en 50x50 cases
    :param image_path: Chemin vers l'image à quadriller
    :param taille_case: Taille d'une case en pixels
    """
    # Charger l'image
    img = Image.open(image_path)
    
    # Créer une copie de l'image pour dessiner la grille
    img_quadrillee = img.copy()
    draw = ImageDraw.Draw(img_quadrillee)
    
    # Dimensions de la grille
    largeur, hauteur = img.size
    nombre_cases = 50
    
    # Couleur de la grille (rouge semi-transparent)
    couleur_grille = (255, 0, 0, 128)  # RGBA
    
    # Dessiner les lignes verticales
    for i in range(nombre_cases + 1):
        x = i * (largeur // nombre_cases)
        draw.line([(x, 0), (x, hauteur)], fill=couleur_grille, width=1)
    
    # Dessiner les lignes horizontales
    for i in range(nombre_cases + 1):
        y = i * (hauteur // nombre_cases)
        draw.line([(0, y), (largeur, y)], fill=couleur_grille, width=1)
    
    # Sauvegarder l'image quadrillée
    image_path = Path(image_path)
    chemin_sauvegarde = image_path.with_name(f"{image_path.stem}_quadrille{image_path.suffix}")
    img_quadrillee.save(chemin_sauvegarde)
    
    print(f"Image quadrillée sauvegardée sous : {chemin_sauvegarde}")
    print(f"Dimensions de l'image : {largeur}x{hauteur} pixels")
    print(f"Taille d'une case : {largeur//nombre_cases}x{hauteur//nombre_cases} pixels")

if __name__ == "__main__":
    # Chemin vers l'image du plan
    plan_source = image_path("plan_main.png")
    
    # Vérifier si l'image existe
    if not plan_source.exists():
        print(f"Erreur : L'image {plan_source} n'existe pas")
    else:
        # Quadriller l'image
        quadriller_image(plan_source)