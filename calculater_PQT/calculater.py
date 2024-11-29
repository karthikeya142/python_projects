import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")

        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""

        layout = QGridLayout()
        self.setLayout(layout)
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [QPushButton(str(i)) for i in range(10)]

        operators = ["+", "-", "*", "/"]
        operator_buttons = [QPushButton(op) for op in operators]

        equals_button = QPushButton("=")
        clear_button = QPushButton("C")

        # Adding event handling method for number buttons
        for button in buttons:
            button.clicked.connect(self.number_button_clicked)

        # Adding event handling method for operators
        for button in operator_buttons:
            button.clicked.connect(self.operator_button_clicked)

        # Adding buttons to the layout
        for i, button in enumerate(buttons):
            row, col = divmod(i, 3)
            layout.addWidget(button, row + 1, col)

        for i, op_button in enumerate(operator_buttons):
            layout.addWidget(op_button, i + 1, 3)

        layout.addWidget(equals_button, 4, 1)
        layout.addWidget(clear_button, 4, 2)

        equals_button.clicked.connect(self.calculate)
        clear_button.clicked.connect(self.clear)

    # Creating a method to handle number button clicks
    def number_button_clicked(self):
        digit = self.sender().text()
        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        self.display.setText(self.current_input)

    def operator_button_clicked(self):
        operator = self.sender().text()
        if self.current_operator == "":
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = "0"
        else:
            # Calculate the current result
            self.calculate()
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = "0"

    def calculate(self):
        try:
            if self.current_operator == "+":
                result = float(self.previous_input) + float(self.current_input)
            elif self.current_operator == "-":
                result = float(self.previous_input) - float(self.current_input)
            elif self.current_operator == "*":
                result = float(self.previous_input) * float(self.current_input)
            elif self.current_operator == "/":
                if self.current_input == "0":
                    result = "Error"
                else:
                    result = float(self.previous_input) / float(self.current_input)
            else:
                result = self.current_input

            self.display.setText(str(result))
            self.current_input = str(result)
            self.current_operator = ""

        except Exception as e:
            self.display.setText("Error")
            self.current_input = "0"
            self.previous_input = ""
            self.current_operator = ""

    def clear(self):
        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""
        self.display.setText("0")

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
