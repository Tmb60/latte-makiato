# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoffeeInfo(object):
    def setupUi(self, CoffeeInfo):
        CoffeeInfo.setObjectName("CoffeeInfo")
        CoffeeInfo.resize(809, 600)
        self.central_widget = QtWidgets.QWidget(CoffeeInfo)
        self.central_widget.setObjectName("central_widget")
        self.table = QtWidgets.QTableWidget(self.central_widget)
        self.table.setGeometry(QtCore.QRect(10, 50, 791, 441))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 490, 791, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.updateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout.addWidget(self.updateButton)
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        CoffeeInfo.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(CoffeeInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 26))
        self.menubar.setObjectName("menubar")
        CoffeeInfo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CoffeeInfo)
        self.statusbar.setObjectName("statusbar")
        CoffeeInfo.setStatusBar(self.statusbar)

        self.retranslateUi(CoffeeInfo)
        QtCore.QMetaObject.connectSlotsByName(CoffeeInfo)

    def retranslateUi(self, CoffeeInfo):
        _translate = QtCore.QCoreApplication.translate
        CoffeeInfo.setWindowTitle(_translate("CoffeeInfo", "MainWindow"))
        self.addButton.setText(_translate("CoffeeInfo", "Добавить"))
        self.updateButton.setText(_translate("CoffeeInfo", "Изменить"))
        self.label.setText(_translate("CoffeeInfo", "Прайс-лист"))
