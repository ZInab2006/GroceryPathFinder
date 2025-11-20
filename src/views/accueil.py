from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

from src.core.paths import image_path

class AccueilVue(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__controleur = None  # Sera défini par le contrôleur
        
        self.setWindowTitle("Page d'accueil")
        self.setFixedSize(500, 500)
        
        # Création de l'interface
        self.__init_ui()
        
    def __init_ui(self):
        # Widget central et layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        # Texte principal
        self.main_text = QLabel("Fini les balades inutiles en magasin ! En un clic, trouvez le chemin le plus rapide ", self)
        self.main_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Logo
        self.logo_label = QLabel(self)
        logo_pixmap = QPixmap(str(image_path("logo.jpg")))
        logo_pixmap = logo_pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.logo_label.setPixmap(logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Texte de bienvenue
        self.welcome_label = QLabel("Bienvenue dans l'application QuickCart!", self)
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_font = QFont()
        welcome_font.setPointSize(18)
        welcome_font.setBold(True)
        self.welcome_label.setFont(welcome_font)
        
        # Bouton
        self.button = QPushButton("C'est parti !", self)
        self.button.setFixedWidth(300)
        self.button.setFixedHeight(40)
        self.button.clicked.connect(self.__on_button_clicked)
        
        # Widget pour la partie basse
        bottom_widget = QWidget()
        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(self.welcome_label)
        bottom_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_widget.setLayout(bottom_layout)
        
        # Ajout des widgets au layout principal
        layout.addStretch(1)
        layout.addWidget(self.main_text)
        layout.addStretch(2)
        layout.addWidget(self.logo_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(2)
        layout.addWidget(bottom_widget)
        layout.addStretch(1)
        
        # Configuration du widget central
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def set_controleur(self, controleur):
        """Définit le contrôleur associé à cette vue"""
        self.__controleur = controleur
    
    def __on_button_clicked(self):
        """Gère le clic sur le bouton"""
        if self.__controleur:
            self.__controleur.on_button_clicked()
    
    def show(self):
        """Affiche la fenêtre"""
        super().show() 