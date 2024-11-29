import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QStyleFactory, QLabel, QVBoxLayout, QPushButton, QWidget

stylesheet="""
    QPushButton#My_Button{
                background-color:grey;                          
                padding:5px;
               }
               QPushButton#My_Button:pressed{
                            background-color:blue;
                            padding:5px;
               }
    QLabel#My_Label{
            background-color:green;
            color:white;
            margin:100px;
    }
"""

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Styling HTML & CSS")
        self.setGeometry(0,0, 700, 500)
        label =QLabel("<h1> This is a label </h1>",self)
        label.setObjectName("My_Label")
        label.adjustSize()
        button =QPushButton("click here")
        button.setObjectName("My_Button")
        layout =QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)


app =QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = Window()
window.show()
app.exec()
