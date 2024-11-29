import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QStyleFactory, QLabel, QVBoxLayout, QPushButton, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Styling HTML & CSS")
        self.setGeometry(0,0, 700, 500)
        label =QLabel("<h1> This is a label </h1>",self)
        label.setStyleSheet("""
                            background-color:red;
                            color:yellow;
                            margin:100px;
                            """)
        label.adjustSize()
        button =QPushButton("click here")
        button.setStyleSheet("""
                QPushButton{
                            background-color:grey;                          
                            padding:5px;
               }
               QPushButton:pressed{
                            background-color:blue;
                            padding:5px;
               }
                                    """)
        layout =QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)


app =QApplication(sys.argv)
window = Window()
window.show()
app.exec()
