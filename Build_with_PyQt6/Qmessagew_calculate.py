import math
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("this is Qmessage calculate")
        self.setGeometry(0, 0, 400, 400)

        self.number_label = QLabel("Enter a number", self)
        self.number_label.move(20, 20)

        self.number_input = QLineEdit(self)
        self.number_input.move(200, 20)

        calculate_button = QPushButton("Find Root", self)
        calculate_button.move(200, 80)

        self.result_label = QLabel("Result: ", self)
        self.result_label.move(20, 100)
        calculate_button.clicked.connect(self.calculate_square)

    def calculate_square(self):
        try:
            number = float(self.number_input.text())
            squre_root = math.sqrt(number)
            if squre_root.is_integer():
                self.result_label.setText(f"Square root: {squre_root}")
                self.result_label.adjustSize()
            else:
                msg =QMessageBox.warning(self,"Not A perfect square","The number is not a perfect square")
        except ValueError :
            QMessageBox.warning(self,"Invalid Input", "Please enter valid  number")
            # self.result_label.setText("Invalid Input, Please enter number")
            # self.result_label.resize(300, 30)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
