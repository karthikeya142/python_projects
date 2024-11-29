import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QStyleFactory, QLabel, QVBoxLayout


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Styling HTML & CSS")
        self.setGeometry(0,0, 700, 500)
        label =QLabel("<h1><font color ='red'> This is a label </h1>",self)
        label.adjustSize()
        label.resize(200,50)
        layout =QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
app =QApplication(sys.argv)
window = Window()
window.show()
app.exec()
