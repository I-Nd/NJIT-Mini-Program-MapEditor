# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapEditor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 651, 261))
        self.groupBox.setObjectName("groupBox")
        self.categoriesTable = QtWidgets.QTableWidget(self.groupBox)
        self.categoriesTable.setGeometry(QtCore.QRect(10, 20, 591, 231))
        self.categoriesTable.setObjectName("categoriesTable")
        self.categoriesTable.setColumnCount(5)
        self.categoriesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(4, item)
        self.categoriesTable.horizontalHeader().setVisible(True)
        self.categoriesTable.horizontalHeader().setCascadingSectionResizes(False)
        self.categoriesTable.verticalHeader().setVisible(False)
        self.catAddBut = QtWidgets.QPushButton(self.groupBox)
        self.catAddBut.setGeometry(QtCore.QRect(610, 20, 31, 31))
        self.catAddBut.setObjectName("catAddBut")
        self.catDelBut = QtWidgets.QPushButton(self.groupBox)
        self.catDelBut.setGeometry(QtCore.QRect(610, 60, 31, 31))
        self.catDelBut.setObjectName("catDelBut")
        self.catModBut = QtWidgets.QPushButton(self.groupBox)
        self.catModBut.setGeometry(QtCore.QRect(610, 100, 31, 31))
        self.catModBut.setObjectName("catModBut")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 781, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.buildingsTable = QtWidgets.QTableWidget(self.groupBox_2)
        self.buildingsTable.setGeometry(QtCore.QRect(10, 20, 721, 261))
        self.buildingsTable.setObjectName("buildingsTable")
        self.buildingsTable.setColumnCount(6)
        self.buildingsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.buildingsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.buildingsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.buildingsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.buildingsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.buildingsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.buildingsTable.setHorizontalHeaderItem(5, item)
        self.buildingsTable.verticalHeader().setVisible(False)
        self.budAddBut = QtWidgets.QPushButton(self.groupBox_2)
        self.budAddBut.setGeometry(QtCore.QRect(740, 20, 31, 31))
        self.budAddBut.setObjectName("budAddBut")
        self.budDelBut = QtWidgets.QPushButton(self.groupBox_2)
        self.budDelBut.setGeometry(QtCore.QRect(740, 60, 31, 31))
        self.budDelBut.setObjectName("budDelBut")
        self.budModBut = QtWidgets.QPushButton(self.groupBox_2)
        self.budModBut.setGeometry(QtCore.QRect(740, 100, 31, 31))
        self.budModBut.setObjectName("budModBut")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(670, 120, 121, 31))
        self.openButton.setObjectName("openButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(670, 160, 121, 31))
        self.saveButton.setObjectName("saveButton")
        self.openJSButton = QtWidgets.QPushButton(self.centralwidget)
        self.openJSButton.setGeometry(QtCore.QRect(670, 200, 121, 31))
        self.openJSButton.setObjectName("openJSButton")
        self.saveJSButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveJSButton.setGeometry(QtCore.QRect(670, 240, 121, 31))
        self.saveJSButton.setObjectName("saveJSButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "校园导航数据编辑器"))
        self.groupBox.setTitle(_translate("MainWindow", "分类管理"))
        item = self.categoriesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "分类编号"))
        item = self.categoriesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "分类名称"))
        item = self.categoriesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "默认图标"))
        item = self.categoriesTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "高亮图标"))
        item = self.categoriesTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "建筑数量"))
        self.catAddBut.setText(_translate("MainWindow", "增"))
        self.catDelBut.setText(_translate("MainWindow", "删"))
        self.catModBut.setText(_translate("MainWindow", "改"))
        self.groupBox_2.setTitle(_translate("MainWindow", "建筑物管理"))
        item = self.buildingsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "分类编号"))
        item = self.buildingsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "建筑编号"))
        item = self.buildingsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "建筑名称"))
        item = self.buildingsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "坐标经度"))
        item = self.buildingsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "坐标纬度"))
        item = self.buildingsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "建筑图片"))
        self.budAddBut.setText(_translate("MainWindow", "增"))
        self.budDelBut.setText(_translate("MainWindow", "删"))
        self.budModBut.setText(_translate("MainWindow", "改"))
        self.openButton.setText(_translate("MainWindow", "读入JSON"))
        self.saveButton.setText(_translate("MainWindow", "写入JSON"))
        self.openJSButton.setText(_translate("MainWindow", "读入NavData.js"))
        self.saveJSButton.setText(_translate("MainWindow", "写入NavData.js"))

