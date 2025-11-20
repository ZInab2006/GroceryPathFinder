from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QSizePolicy,
    QToolButton,
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

from src.core.paths import image_path

class SupermarcheVue(QWidget):
    def __init__(self):
        super().__init__()
        self.__controleur = None  # Sera défini par le contrôleur
        self.setWindowTitle("Choix du supermarché")
        self.setFixedSize(500, 500)  # Même taille que la page d'accueil
        print("Vue du supermarché initialisée")
        self.__init_interface()

    def __init_interface(self):
        print("Initialisation de l'interface")
        # Label titre, centré horizontalement
        self.__titre = QLabel("Choisissez votre supermarché")
        self.__titre.setObjectName("title_label")
        self.__titre.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Chemins vers les images pour les boutons
        icon_paths = [
            image_path("plan_1.png"),
            image_path("plan_2.png"),
            image_path("plan_3.png"),
            image_path("plan_4.jpg"),
        ]

        # Création des 4 boutons avec taille minimum, politique d'expansion et icône
        self.__boutons = []
        noms = ["Super, marchez", "Hyper Z", "E-Leclown", "Intermar-CHEH"]
        for nom, chemin_icone in zip(noms, icon_paths):
            bouton = QToolButton()
            bouton.setText(nom)
            bouton.clicked.connect(self.__on_bouton_clicked)
            bouton.setMinimumSize(150, 80)
            bouton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

            # Charger et appliquer l'icône
            if chemin_icone.exists():
                icone = QIcon(str(chemin_icone))
                if not icone.isNull():
                    bouton.setIcon(icone)
                    bouton.setIconSize(QSize(48, 48))
                    bouton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
                    print(f"Image chargée pour {nom}")
            else:
                print(f"Image non trouvée : {chemin_icone}")

            self.__boutons.append(bouton)

        # Layout en grille 2x2 pour former un carré
        grille = QGridLayout()
        grille.addWidget(self.__boutons[0], 0, 0)
        grille.addWidget(self.__boutons[1], 0, 1)
        grille.addWidget(self.__boutons[2], 1, 0)
        grille.addWidget(self.__boutons[3], 1, 1)
        grille.setHorizontalSpacing(20)
        grille.setVerticalSpacing(20)

        # Faire en sorte que les lignes et colonnes grandissent également
        grille.setRowStretch(0, 1)
        grille.setRowStretch(1, 1)
        grille.setColumnStretch(0, 1)
        grille.setColumnStretch(1, 1)

        # Container pour centrer le grid layout
        container = QWidget()
        container.setLayout(grille)

        # Layout principal vertical
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.__titre, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_principal.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)

        # Marges et espacement réduits
        layout_principal.setContentsMargins(20, 10, 20, 20)
        layout_principal.setSpacing(10)

        self.setLayout(layout_principal)
        print("Interface initialisée avec succès")

    def set_controleur(self, controleur):
        """Définit le contrôleur associé à cette vue"""
        self.__controleur = controleur
        print("Contrôleur défini pour la vue du supermarché")

    def __on_bouton_clicked(self):
        """Gère le clic sur un bouton et notifie le contrôleur"""
        sender = self.sender()
        print(f"Bouton cliqué : {sender.text()}")
        if self.__controleur:
            print("Contrôleur trouvé, appel de supermarche_choisi")
            self.__controleur.supermarche_choisi(sender.text())
        else:
            print("ERREUR : Contrôleur non défini !") 