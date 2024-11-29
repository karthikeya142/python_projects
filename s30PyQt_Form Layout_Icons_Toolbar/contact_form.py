import sys

from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit, QComboBox, QTextEdit, QPushButton, QLabel, QApplication, \
    QMessageBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Contact Form")
        self.setGeometry(100, 100, 400, 200)

        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()

        self.subject_combo = QComboBox()
        self.subject_combo.addItems(["Select Subject", "Personal", "Business"])

        self.message_edit = QTextEdit()

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.SubmitClicked)

        form_layout.addRow(QLabel("Name"), self.name_edit)
        form_layout.addRow(QLabel("Email"), self.email_edit)
        form_layout.addRow(QLabel("Phone Number"), self.phone_edit)
        form_layout.addRow(QLabel("Subject"), self.subject_combo)
        form_layout.addRow(QLabel("Message"), self.message_edit)
        form_layout.addRow(submit_button)

    def SubmitClicked(self,submit):
            name = self.name_edit.text()
            email = self.email_edit.text()
            phone = self.phone_edit.text()
            subject = self.subject_combo.currentText()
            message = self.message_edit.toPlainText()
            # print(f"Name:{name} \n Email:{email} \n Phone:{phone} \n Subject:{subject} \n Message:{message}")















app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
