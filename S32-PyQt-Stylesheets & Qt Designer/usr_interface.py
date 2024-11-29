import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QStyleFactory


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Contact Form")
        self.setGeometry(0,0, 700, 500)

app =QApplication(sys.argv)
app.setStyle("windows")
window = Window()
window.show()
# print(QStyleFactory.keys()) #its print what kind of styling our app is using
# print(app.style().name()) #its print what kind of styling our app is using
app.exec()
