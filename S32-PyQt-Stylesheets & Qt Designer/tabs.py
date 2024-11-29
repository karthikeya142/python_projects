import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QTabWidget, QPushButton


stylesheet="""
    QPushButton#My_Button1{
                background-color:grey;                          
                padding:5px;
               }
               QPushButton#My_Button1:pressed{
                            background-color:blue;
                            
               }
    QPushButton#My_Button2{
                background-color:orange;                          
                padding:5px;
               }
               QPushButton#My_Button2:pressed{
                            background-color:red;
                            
               }
QWidget#My_tab1{
            background-color:gold;
            
    }
    
    QWidget#My_tab2{
            background-color:silver;
            
    }
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,400,200)
        #creating a tab widget
        tab_widget =QTabWidget()
        #create tab
        tab1 =QWidget()
        tab1.setObjectName("My_tab1")
        tab2 =QWidget()
        tab2.setObjectName("My_tab2")
        #adding above tabs to the tab widget
        tab_widget.addTab(tab1,"tab1")
        tab_widget.addTab(tab2,"karthik")
        #create a buttons to added to tabs
        button1 =QPushButton("Button1")
        button2 =QPushButton("Button2")
        button1.setObjectName("My_Button1")
        button2.setObjectName("My_Button2")
        #creating layout for the tab1 and tab2
        layout1 =QVBoxLayout()
        layout1.addWidget(button1)
        layout2 = QVBoxLayout()
        layout2.addWidget(button2)

        # setting the tab layout to layout1 and layout2
        tab1.setLayout(layout1)
        tab2.setLayout(layout2)
        #add the above tab widget to the main window
        layout= QVBoxLayout(self)
        layout.addWidget(tab_widget)






app =QApplication(sys.argv)
window= Window()
app.setStyleSheet(stylesheet)
window.show()
app.exec()
