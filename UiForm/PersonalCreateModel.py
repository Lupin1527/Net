# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PersonalCreateModel.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(499, 407)
        self.AddPoint = QtWidgets.QPushButton(Form)
        self.AddPoint.setGeometry(QtCore.QRect(360, 190, 91, 31))
        self.AddPoint.setObjectName("AddPoint")
        self.AddLIne = QtWidgets.QPushButton(Form)
        self.AddLIne.setGeometry(QtCore.QRect(360, 250, 101, 31))
        self.AddLIne.setObjectName("AddLIne")

        self.retranslateUi(Form)
        self.AddPoint.clicked.connect(Form.GoToAddPoint)
        self.AddLIne.clicked.connect(Form.GoToAddLine)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.AddPoint.setText(_translate("Form", "添加结点"))
        self.AddLIne.setText(_translate("Form", "添加线"))
