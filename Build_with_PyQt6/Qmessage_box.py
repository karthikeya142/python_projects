from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QWidget,QMessageBox ,QApplication, QLabel, QPushButton, QCheckBox, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.count =0
        self.setWindowTitle("My first PyQt Window ")
        self.setGeometry(0, 0, 400, 400)

        button = QPushButton("Show Messagebox",self)
        button.setGeometry(150,80,200,40)
        button.clicked.connect(self.show_message_box)

    def show_message_box(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message box title")
        msg.setText("This is a simple QMessageBox")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        result=msg.exec()

        if result == QMessageBox.StandardButton.ok:
            print("ok button is clicked")
        else:
            print("Cancel button is clicked")



app =QApplication(sys.argv)
window =Window()
window.show()

sys.exit(app.exec())

