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

        num1_label =QLabel("Enter first number",self)
        num1_label.resize(200,20)
        num1_label.move(20,20)
        self.num1_input=QLineEdit(self)
        self.num1_input.move(200,20)

        num2_label =QLabel("Enter second number",self)
        num2_label.resize(200,20)
        num2_label.move(20,60)
        self.num2_input=QLineEdit(self)
        self.num2_input.move(200,60)

        self.result_label =QLabel("Result",self)
        self.result_label.move(20,100)

        # new code added
        calculate_button = QPushButton("Calculate",self)
        calculate_button.move(300,100)
        calculate_button.clicked.connect(self.calculate_sum)
    def calculate_sum(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            result = num1+num2

            self.result_label.setText(f"Results: {result:.2f} ")
            self.result_label.resize(300,20)
        except ValueError:
            self.result_label.setText("Invalid Input, Please enter number")
            self.result_label.resize(300,20)

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())