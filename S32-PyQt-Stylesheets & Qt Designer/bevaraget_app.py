import sys

from PyQt6.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QCheckBox

stylesheet = """
    QWidget#Tea{
            background-color:darkkhaki;
    }
    QWidget#Tea_liquid{
            background-color:lightcoral;

    }

    QWidget#Tea_spice{
            background-color:darkred;

    }
    
    
    QWidget#Coffee{
            background-color:lightskyblue;

    }
    QWidget#coffee_liquid{
            background-color:orange;

    }

    QWidget#coffee_spice{
            background-color:lightsalmon;

    }
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Application")
        self.setGeometry(0, 0, 700, 500)
        tab_widget = QTabWidget()

        # Create tabs
        tea_tab = QWidget()
        tea_tab.setObjectName("Tea")
        coffee_tab = QWidget()
        coffee_tab.setObjectName("Coffee")

        tab_widget.addTab(tea_tab, "Tea")
        tab_widget.addTab(coffee_tab, "Coffee")

        # Tea layout
        tea_layout = QVBoxLayout()
        coffee_layout = QVBoxLayout()

        liquid_label_coffe = QLabel("<h3><font color ='lightcyan'> Select Milk/Water </h3>",self)
        milk_button = QRadioButton(" Milk ")
        water_button = QRadioButton("Water")

        # Create container for milk/water
        liquid_group = QGroupBox()
        liquid_group.setObjectName("Tea_liquid")

        # Creating a layout for the liquid container
        liquid_group_layout = QVBoxLayout()

        liquid_group_layout.addWidget(milk_button)
        liquid_group_layout.addWidget(water_button)

        liquid_group.setLayout(liquid_group_layout)
        tea_layout.addWidget(liquid_label_coffe)
        tea_layout.addWidget(liquid_group)
        tea_tab.setLayout(tea_layout)

        spice_label = QLabel("<h3><font color ='lightcyan'> Select spice to add </h3>",self)

        tea_layout.addWidget(spice_label)

        #creating spice container
        spice_box = QGroupBox()
        spice_box.setObjectName("Tea_spice")
        #creating layout for spice box
        spice_box_layout = QVBoxLayout()
        spice_box.setLayout(spice_box_layout)
        spices = ['sugar', 'clove', 'black pepper', 'cinamon', 'tumrmuric']
        for spice in spices:
            spice_check_box = QCheckBox(spice)
            spice_box_layout.addWidget(spice_check_box)
        tea_layout.addWidget(spice_box)

        # Add widgets to tea_layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(tab_widget)

        #creating coofee label

        liquid_label = QLabel("<h3><font color ='lightolive'> Select spice to add </h3>",self)
        milk_button = QRadioButton("Milk")
        water_button = QRadioButton("Water")

        # Create container for milk/water
        liquid_group = QGroupBox()
        liquid_group.setObjectName("coffee_liquid")

        # Creating a layout for the liquid container
        liquid_group_layout = QVBoxLayout()
        liquid_group_layout.addWidget(milk_button)
        liquid_group_layout.addWidget(water_button)

        liquid_group.setLayout(liquid_group_layout)
        coffee_layout.addWidget(liquid_label)
        coffee_layout.addWidget(liquid_group)
        coffee_tab.setLayout(coffee_layout)

        spice_label = QLabel("<h3><font color ='lightivory'> Select spice to add </h3>",self)
        coffee_layout.addWidget(spice_label)

        #creating spice container
        spice_box = QGroupBox()
        spice_box.setObjectName("coffee_spice")
        #creating layout for spice box
        spice_box_layout = QVBoxLayout()
        spice_box.setLayout(spice_box_layout)
        spices = ['sugar', 'clove', 'black pepper', 'cinamon', 'tumrmuric']
        for spice in spices:
            spice_check_box = QCheckBox(spice)
            spice_box_layout.addWidget(spice_check_box)
        coffee_layout.addWidget(spice_box)

        # Add widgets to coffe_layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(tab_widget)


app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = Window()
window.show()
app.exec()
