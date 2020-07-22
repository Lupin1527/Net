# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPiontUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPoint(object):
    def setupUi(self, AddPoint):
        AddPoint.setObjectName("AddPoint")
        AddPoint.resize(400, 300)
        self.layoutWidget = QtWidgets.QWidget(AddPoint)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 20, 241, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.NameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.NameEdit.setObjectName("NameEdit")
        self.horizontalLayout.addWidget(self.NameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.vulneListEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.vulneListEdit.setObjectName("vulneListEdit")
        self.horizontalLayout_2.addWidget(self.vulneListEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.posEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.posEdit.setObjectName("posEdit")
        self.horizontalLayout_3.addWidget(self.posEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.catEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.catEdit.setObjectName("catEdit")
        self.horizontalLayout_4.addWidget(self.catEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.AcceptButton = QtWidgets.QPushButton(AddPoint)
        self.AcceptButton.setGeometry(QtCore.QRect(260, 250, 112, 32))
        self.AcceptButton.setObjectName("AcceptButton")
        self.rejectButton = QtWidgets.QPushButton(AddPoint)
        self.rejectButton.setGeometry(QtCore.QRect(40, 250, 112, 32))
        self.rejectButton.setObjectName("rejectButton")

        self.retranslateUi(AddPoint)
        self.AcceptButton.clicked.connect(AddPoint.acceptPoint)
        self.rejectButton.clicked.connect(AddPoint.reject_exit)
        QtCore.QMetaObject.connectSlotsByName(AddPoint)

    def retranslateUi(self, AddPoint):
        _translate = QtCore.QCoreApplication.translate
        AddPoint.setWindowTitle(_translate("AddPoint", "Form"))
        self.label.setText(_translate("AddPoint", "结点名字"))
        self.label_2.setText(_translate("AddPoint", "结点漏洞"))
        self.label_4.setText(_translate("AddPoint", "结点坐标"))
        self.label_5.setText(_translate("AddPoint", "结点类型"))
        self.AcceptButton.setText(_translate("AddPoint", "确定"))
        self.rejectButton.setText(_translate("AddPoint", "取消"))
