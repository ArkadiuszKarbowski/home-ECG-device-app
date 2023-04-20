from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QGraphicsOpacityEffect
from PyQt5.QtGui import QPixmap
import sys

class EKGAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ustawienia okna
        self.setWindowTitle('EKG App')
        self.setGeometry(100, 100, 400, 200)
        
        
        # Kontener główny
        main_container = QWidget()
        self.setCentralWidget(main_container)
        main_layout = QVBoxLayout()
        main_container.setLayout(main_layout)

        # Tło w formie obrazu
        background_img = QPixmap("static/background_logo.png")
        # Zmiana rozmiaru obrazu na 400x200
        background_img = background_img.scaled(1000, 800)
        
        background_label = QLabel()
        background_label.setStyleSheet("Opacity: 110")
        background_label.setPixmap(background_img)
        main_layout.addWidget(background_label)
        


        self.setFixedSize(background_img.size())
        # Kontenery na napisy
        label1 = QLabel("Napis 1", background_label)
        label2 = QLabel("Napis 2", background_label)

        # Ustawienie styli dla napisów
        label1.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); margin-top: 50px; margin-left: 50px;")
        label2.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); margin-top: 100px; margin-left: 100px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EKGAppWindow()
    window.show()
    sys.exit(app.exec_())
