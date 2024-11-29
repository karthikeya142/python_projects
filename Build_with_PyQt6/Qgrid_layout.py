import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QHBoxLayout, QWidget, \
    QVBoxLayout, QGridLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QBox Layout")
        self.setGeometry(0, 0, 400, 150)
        
        label1 =QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")
        label4 = QLabel("Label 4")

        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        button4 = QPushButton("Button4")

        layout =QGridLayout()
        self.setLayout(layout)

        layout.addWidget(label1,0,0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 0, 2)
        layout.addWidget(label4, 0, 3)

        layout.addWidget(button1,1,0)
        layout.addWidget(button2, 1, 1)
        layout.addWidget(button3, 1, 2)
        layout.addWidget(button4, 1, 3)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
