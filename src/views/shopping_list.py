from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QCheckBox, QPushButton, QLabel, QSizePolicy
from PyQt6.QtCore import Qt

class VueListeCourses(QWidget):
    def __init__(self):
        super().__init__()
        self.__controleur = None
        self.setWindowTitle("Liste de courses")
        self.setFixedSize(600, 520)
        self.__init_interface()

    def __init_interface(self):
        # Titre
        self.__titre = QLabel("Sélectionnez vos articles")
        self.__titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__titre.setStyleSheet("font-size: 30px; font-weight: bold; margin: 15px;")
        
        # Grille de cases à cocher
        self.__articles = [
            "lait", "pâtes", "beurre", "papier toilette", "savon",
            "chips", "shampooing", "brosse à dents", "bananes", "brioche",
            "riz", "yaourt", "eau Minérale", "oeufs", "pommes",
            "pain d'épices", "farine", "café moulu", "petits pois", "sardine"
        ]
        self.__cases_cocher = []
        grille = QGridLayout()
        grille.setSpacing(12)

        for i, article in enumerate(self.__articles):
            case = QCheckBox(article)
            case.setStyleSheet("font-size: 14px;")
            self.__cases_cocher.append(case)
            ligne = i // 4
            colonne = i % 4
            grille.addWidget(case, ligne, colonne)

        # Bouton de validation
        self.__bouton_valider = QPushButton("Valider")
        self.__bouton_valider.setMinimumSize(300, 50)
        self.__bouton_valider.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.__bouton_valider.clicked.connect(self.__on_valider_clicked)
        self.__bouton_valider.setStyleSheet("""
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
        """)

        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.__titre)
        layout_principal.addLayout(grille)
        layout_principal.addWidget(self.__bouton_valider, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_principal.setContentsMargins(20, 20, 20, 10)
        layout_principal.setSpacing(15)
        self.setLayout(layout_principal)

    def set_controleur(self, controleur):
        """Définit le contrôleur associé à cette vue"""
        self.__controleur = controleur

    def __on_valider_clicked(self):
        """Gère le clic sur le bouton valider"""
        if self.__controleur:
            articles_selectionnes = [case.text() for case in self.__cases_cocher if case.isChecked()]
            self.__controleur.valider_liste(articles_selectionnes)

    def afficher_message(self, message):
        """Affiche un message à l'utilisateur"""
        self.__titre.setText(message) 