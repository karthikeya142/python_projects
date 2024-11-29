import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from todo import Ui_Form


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)
        self.ui.addtaskButton.clicked.connect(self.add_task)
        self.ui.deletetask.clicked.connect(self.delete_task)

    def add_task(self):
        task = self.ui.taskEdit.text()
        if task:
            self.ui.listtask.addItem(task)  # QListWidget now supports addItem
            self.ui.taskEdit.clear()
    def delete_task(self):
        selected_task = self.ui.listtask.currentItem()
        if selected_task:
            self.ui.listtask.takeItem(self.ui.listtask.row(selected_task))






app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()










