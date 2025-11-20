import sys
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.core.paths import image_path, style_path  # noqa: E402

# --- class Acceuil qui heritent de QMainwindow ---#
class Acceuil(QMainWindow):
    def __init__(self):
        '''Constructeur de la classe'''
        
        # appel au constructeur de la classe mère
        super().__init__()
        
        self.setWindowTitle("Page d'accueil")
        # Désactive le redimensionnement de la fenêtre
        self.setFixedSize(500, 500)
        
        # Création d'un widget central et d'un layout vertical
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        # Création du texte principal
        main_text = QLabel("Fini les balades inutiles en magasin ! En un clic, trouvez le chemin le plus rapide ", self)
        main_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Création du logo
        logo_label = QLabel(self)
        logo_pixmap = QPixmap(str(image_path("logo.jpg")))
        logo_pixmap = logo_pixmap.scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Création du label de bienvenue
        welcome_label = QLabel("Bienvenue dans l'application QuickCart!", self)
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_font = QFont()
        welcome_font.setPointSize(16)  # Taille plus grande
        welcome_font.setBold(True)     # Texte en gras
        welcome_label.setFont(welcome_font)
        
        # Création du bouton
        button = QPushButton("C'est parti !", self)
        button.setFixedWidth(200)
        button.setFixedHeight(40)
        
        # Création d'un widget pour la partie basse
        bottom_widget = QWidget()
        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(welcome_label)
        bottom_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_widget.setLayout(bottom_layout)
        
        # Ajout des widgets au layout principal
        layout.addStretch(1)
        layout.addWidget(main_text)
        layout.addStretch(2)
        layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(2)
        layout.addWidget(bottom_widget)
        layout.addStretch(1)
        
        # Configuration du widget central
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.show()
       
      
       
       
       
# --- main ----#
if __name__ == "__main__":
    
    #creation d'une QApplication
    app = QApplication(sys.argv)
    
     # ouverture d'un fichier de style 
    qss = style_path("accueil.qss").read_text(encoding="utf-8")
    app.setStyleSheet(qss)
  
    
    
    fenetre = Acceuil()

    # lancement de l'application
    sys.exit(app.exec())