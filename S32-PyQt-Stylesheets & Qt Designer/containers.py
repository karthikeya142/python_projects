import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,400,200)
        #step 1 creating a container
        box = QGroupBox()
        box2 = QGroupBox()
        box3= QGroupBox()
        #step 2 creating widgets to be add the conatiner
        button1 =QPushButton("Button 1")
        button2 =QPushButton("Button 2")

        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")

        button5 = QPushButton("Button 5")
        button6 = QPushButton("Button 6")

        #step 3 create a lauout and  the above widgets
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        layout2 = QHBoxLayout()
        layout2.addWidget(button3)
        layout2.addWidget(button4)

        layout3 = QHBoxLayout()
        layout3.addWidget(button5)
        layout3.addWidget(button6)


        #step4 add the above layout to the container
        box.setLayout(layout)
        box2.setLayout(layout2)
        box3.setLayout(layout3)
        #step 5 set the mainwindow's to the layout to the container
        main_layout =QVBoxLayout(self)
        main_layout.addWidget(box)
        main_layout.addWidget(box2)
        main_layout.addWidget(box3)



app =QApplication(sys.argv)
window= Window()
window.show()
app.exec()