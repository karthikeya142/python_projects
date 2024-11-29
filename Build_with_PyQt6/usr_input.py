from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count =0
        self.setWindowTitle("My first PyQt Window ")
        self.setGeometry(0, 0, 400, 400)

        name_label =QLabel(self)
        name_label.setText("Enter Your Name ")
        name_label.move(60,10)

        self.name =QLineEdit(self)
        self.name.resize(200,20)
        self.name.move(60,50)

        button =QPushButton(self)
        button.setText("Add")
        button.move(200,80)
        button.clicked.connect(self.buttonclicked)

        self.result_label =QLabel(self)
        self.result_label.move(60,120)

    def buttonclicked(self):
        # print("Button clicked")
        # print("Your name is :"+ self.name.text())
        self.result_label.setText("Your name is:"+self.name.text())
        self.result_label.adjustSize()



app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
