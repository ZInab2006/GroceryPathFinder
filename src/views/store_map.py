from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QScrollArea,
    QSizePolicy,
)
from PyQt6.QtGui import QPainter, QPen, QColor, QImage
from PyQt6.QtCore import Qt

from src.core.paths import image_path

# Constante pour la taille de la grille (même que dans tools/positionnement_produit.py)
TAILLE_CASE = 20
# Dimensions maximales de l'image et de la fenêtre 
LARGEUR_MAX_IMAGE = 1120

class PlanWidget(QWidget):
    def __init__(self, image_file=image_path("plan_main_quadrille.png")):
        super().__init__()
        self.image_path = image_file
        self.chemin_optimal = []  # Liste des points du chemin optimal
        self.chemin_visible = False  # Nouvelle variable pour contrôler la visibilité
        
        # Charger et redimensionner l'image du plan
        self.plan_image = QImage(str(self.image_path))
        
        # Redimensionner l'image avec la largeur maximale définie
        rapport = LARGEUR_MAX_IMAGE / self.plan_image.width()
        nouvelle_taille = (LARGEUR_MAX_IMAGE, int(self.plan_image.height() * rapport))
        self.plan_image = self.plan_image.scaled(nouvelle_taille[0], nouvelle_taille[1], 
                                                Qt.AspectRatioMode.KeepAspectRatio,
                                                Qt.TransformationMode.SmoothTransformation)


    def set_chemin_visible(self, visible):
        """Définit si le chemin doit être visible"""
        print("Changement de visibilité du chemin:", visible)
        self.chemin_visible = visible
        self.update()

    def definir_chemin(self, chemin):
        """Définit le chemin optimal à afficher"""
        print("Définition du chemin:", chemin)
        # 'chemin' contient maintenant une liste de tuples (grid_x, grid_y, nom)
        # Convertir en coordonnées pixels et ignorer le nom (puisque nous ne l'affichons plus)
        self.chemin_optimal = []
        for item in chemin:
            if len(item) == 3: # Format (x, y, name)
                grid_x, grid_y, _ = item # Ignorer le nom
                pixel_x = grid_x * TAILLE_CASE
                pixel_y = grid_y * TAILLE_CASE
                self.chemin_optimal.append((pixel_x, pixel_y))
            elif len(item) == 2: # Format (x, y) si le nom n'est pas passé
                grid_x, grid_y = item
                pixel_x = grid_x * TAILLE_CASE
                pixel_y = grid_y * TAILLE_CASE
                self.chemin_optimal.append((pixel_x, pixel_y))

        self.chemin_visible = True  # Rendre le chemin visible par défaut
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        try:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            # Dessiner le plan (l'image est déjà mise à l'échelle dans __init__)
            painter.drawImage(0, 0, self.plan_image)
            
            # Dessiner le chemin optimal seulement si visible
            if self.chemin_visible and len(self.chemin_optimal) > 0: # Changer > 1 à > 0 pour dessiner au moins un point
                print("Dessin du chemin avec", len(self.chemin_optimal), "points")
                # Ligne du chemin en bleu
                painter.setPen(QPen(QColor(0, 0, 255), 4, Qt.PenStyle.SolidLine))
                
                # Dessiner les points et les lignes
                for i in range(len(self.chemin_optimal)):
                    point = self.chemin_optimal[i]
                    print(f"Point {i}:", point)
                    if isinstance(point, (list, tuple)) and len(point) == 2:
                        px, py = point
                        # Les coordonnées px, py sont déjà en pixels et origine en haut à gauche
                        screen_x = int(px)
                        screen_y = int(py)
                        print(f"Position écran: ({screen_x}, {screen_y})")
                        
                        # Dessiner un point plus grand pour chaque intersection (épaisseur 20x20)
                        painter.setBrush(QColor(0, 0, 255))  # Point en bleu
                        painter.drawEllipse(screen_x - 10, screen_y - 10, 20, 20) # Rayon de 10 pixels
                        
                        # Dessiner la ligne vers le point suivant
                        if i < len(self.chemin_optimal) - 1:
                            next_point = self.chemin_optimal[i + 1]
                            if isinstance(next_point, (list, tuple)) and len(next_point) == 2:
                                nx, ny = next_point
                                next_screen_x = int(nx)
                                next_screen_y = int(ny)
                                print(f"Ligne vers: ({next_screen_x}, {next_screen_y})")
                                painter.drawLine(screen_x, screen_y, next_screen_x, next_screen_y)
        finally:
            painter.end()

class PlanVue(QWidget):
    def __init__(self):
        super().__init__()
        self.__controleur = None
        self.setWindowTitle("Plan du magasin")
        self.__init_interface()

    def __init_interface(self):
        # Widget principal avec scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        # Widget du plan (charge plan_main_quadrille.png par défaut)
        self.plan_widget = PlanWidget()
        # Définir la taille du PlanWidget pour qu'il corresponde à l'image chargée
        self.plan_widget.setFixedSize(self.plan_widget.plan_image.size())
        scroll.setWidget(self.plan_widget)

 

        # Bouton de visualisation du chemin
        self.bouton_visualiser = QPushButton("Visualiser le chemin")
        self.bouton_visualiser.setMinimumSize(300, 50)
        self.bouton_visualiser.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.bouton_visualiser.clicked.connect(self.__on_visualiser_clicked)
        self.bouton_visualiser.setStyleSheet('''
            QPushButton {
                font-size: 16px;
                padding: 10px 30px;
                background-color: #5EB6B9;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #4aa7aa;
            }
        ''')

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(scroll)
        layout.addWidget(self.bouton_visualiser, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        self.setLayout(layout)

    def __on_visualiser_clicked(self):
        """Gère le clic sur le bouton de visualisation"""
        print("Bouton visualiser cliqué")
        # Inverser la visibilité du chemin directement via le widget du plan
        self.plan_widget.set_chemin_visible(not self.plan_widget.chemin_visible)

    def afficher_chemin(self, chemin):
        """Affiche le chemin optimal sur le plan"""
        print("Affichage du chemin:", chemin)
        self.plan_widget.definir_chemin(chemin)
        # La visibilité est gérée par definir_chemin dans PlanWidget

    def set_controleur(self, controleur):
        self.__controleur = controleur 