import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from design import Ui_Form


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)
        self.ui.lineEdit.setMaxLength(8)
        self.ui.lineEdit_2.setMaxLength(9)

        self.ui.pushButton.clicked.connect(self.checked)


    def checked(self):

        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username == "Admin" and password =="Admin@123" :
            print("Valid username and password")
        else:
            print("Invalid username and password")



app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
