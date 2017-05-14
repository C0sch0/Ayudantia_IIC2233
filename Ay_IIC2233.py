import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize


class Tinder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_tinder()

    def init_tinder(self):
        # Titulo
        self.titulo = QLabel(self)
        self.titulo.setText("Progra-Tinder")
        self.titulo.move(160,10)
        self.titulo.show()

        # Boton Match
        self.match = QPushButton(self)
        self.match.setText("Match")
        self.match.move(70, 60)
        self.match.clicked.connect(self.hacer_match)

        # Boton Next
        self.next = QPushButton(self)
        self.next.setText("Next")
        self.next.move(220, 60)
        self.next.clicked.connect(self.cambiar_imagen)

        # Cantidad de matches
        self.nro_matches = QLabel(self)
        self.nro_matches.setText("Matches:  ")
        self.nro_matches.move(160,120)
        self.nro_matches.show()

        self.path_imagenes = "Imgs/"

        self.imagen_principal = QLabel(self)
        self.imagen_principal.setFixedWidth(120)
        self.imagen_principal.setFixedHeight(120)
        self.imagen_principal.move(150,160)
        self.imagen_principal.show()


        # se da forma a la ventana principal y se muestra
        self.setGeometry(100, 100, 400, 300)
        self.show()

        self.numero_matches = 0
        self.nombres = ["1", "2", "3","4",
                        "5", "6","7", "8",
                        "9", "10", "11", "12",
                        "b"]
        self.imagen_actual = 0

    def cambiar_imagen(self):
        self.imagen_actual += 1
        if self.imagen_actual >= 12:
            self.imagen_actual = 0
        self.opcion_actual = self.nombres[self.imagen_actual]

        pixmap = QPixmap("Imgs/{0}.png".format(self.opcion_actual))
        pixmap = pixmap.scaled(120,120)
        self.imagen_principal.setPixmap(pixmap)

    def hacer_match(self):
        self.numero_matches += 1
        self.cambiar_imagen()
        self.nro_matches.setText("Matches: {0}".format(self.numero_matches))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tinder()
    sys.exit(app.exec_())