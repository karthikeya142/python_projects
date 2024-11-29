# -*- coding: utf-8 -*-
from PyQt6.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt6.QtWidgets import QPushButton, QLineEdit, QListView, QListWidget


################################################################################
## Form generated from reading UI file 'todoPNSGNO.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
#
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.addtaskButton = QPushButton(Form)
        self.addtaskButton.setObjectName(u"addtaskButton")
        self.addtaskButton.setGeometry(QRect(160, 40, 75, 24))
        self.taskEdit = QLineEdit(Form)
        self.taskEdit.setObjectName(u"taskEdit")
        self.taskEdit.setGeometry(QRect(20, 40, 113, 21))
        self.deletetask = QPushButton(Form)
        self.deletetask.setObjectName(u"deletetask")
        self.deletetask.setGeometry(QRect(250, 40, 75, 24))
        self.listtask = QListWidget(Form)  # Change QListView to QListWidget
        self.listtask.setObjectName(u"listtask")
        self.listtask.setGeometry(QRect(20, 80, 256, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.addtaskButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.deletetask.setText(QCoreApplication.translate("Form", u"Delete", None))
