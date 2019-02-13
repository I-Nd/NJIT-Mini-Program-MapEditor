import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView, QTableWidgetItem, QMessageBox, QFileDialog, QDialog
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from mapEditor_ui import *


class CategoryDialog(QDialog):
    def __init__(self, title, cid, name, icon, tapIcon, quantities):
        super().__init__()
        self.title = title
        self.setupUi(self)
        self.cidEdit.setText(cid)
        self.nameEdit.setText(name)
        self.iconEdit.setText(icon)
        self.tapIconEdit.setText(tapIcon)
        self.quantitiesEdit.setText(quantities)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(234, 212)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 170, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 60, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 60, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 80, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 80, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 60, 20))
        self.label_5.setObjectName("label_5")
        self.cidEdit = QtWidgets.QLineEdit(Dialog)
        self.cidEdit.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.cidEdit.setObjectName("cidEdit")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.iconEdit = QtWidgets.QLineEdit(Dialog)
        self.iconEdit.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.iconEdit.setObjectName("iconEdit")
        self.tapIconEdit = QtWidgets.QLineEdit(Dialog)
        self.tapIconEdit.setGeometry(QtCore.QRect(100, 110, 113, 20))
        self.tapIconEdit.setObjectName("tapIconEdit")
        self.quantitiesEdit = QtWidgets.QLineEdit(Dialog)
        self.quantitiesEdit.setGeometry(QtCore.QRect(100, 140, 113, 20))
        self.quantitiesEdit.setObjectName("quantitiesEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.title))
        self.label.setText(_translate("Dialog", "分类编号"))
        self.label_2.setText(_translate("Dialog", "分类名称"))
        self.label_3.setText(_translate("Dialog", "默认图标地址"))
        self.label_4.setText(_translate("Dialog", "高亮图标地址"))
        self.label_5.setText(_translate("Dialog", "建筑数量"))

    def get_data(self):
        return self.cidEdit.text(), self.nameEdit.text(), self.iconEdit.text(), self.tapIconEdit.text(), self.quantitiesEdit.text()


class BuildingDialog(QDialog):
    def __init__(self, title, cid, bid, name, longitude, latitude, image):
        super().__init__()
        self.title = title
        self.setupUi(self)
        self.cidEdit.setText(cid)
        self.bidEdit.setText(bid)
        self.nameEdit.setText(name)
        self.longitudeEdit.setText(longitude)
        self.latitudeEdit.setText(latitude)
        self.imageEdit.setText(image)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(234, 236)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 200, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 60, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 60, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 60, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 60, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 60, 20))
        self.label_5.setObjectName("label_5")
        self.cidEdit = QtWidgets.QLineEdit(Dialog)
        self.cidEdit.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.cidEdit.setObjectName("cidEdit")
        self.bidEdit = QtWidgets.QLineEdit(Dialog)
        self.bidEdit.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.bidEdit.setObjectName("bidEdit")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.longitudeEdit = QtWidgets.QLineEdit(Dialog)
        self.longitudeEdit.setGeometry(QtCore.QRect(100, 110, 113, 20))
        self.longitudeEdit.setObjectName("longitudeEdit")
        self.latitudeEdit = QtWidgets.QLineEdit(Dialog)
        self.latitudeEdit.setGeometry(QtCore.QRect(100, 140, 113, 20))
        self.latitudeEdit.setObjectName("latitudeEdit")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 80, 20))
        self.label_6.setObjectName("label_6")
        self.imageEdit = QtWidgets.QLineEdit(Dialog)
        self.imageEdit.setGeometry(QtCore.QRect(100, 170, 113, 20))
        self.imageEdit.setObjectName("imageEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.title))
        self.label.setText(_translate("Dialog", "分类编号"))
        self.label_2.setText(_translate("Dialog", "建筑编号"))
        self.label_3.setText(_translate("Dialog", "建筑名称"))
        self.label_4.setText(_translate("Dialog", "坐标经度"))
        self.label_5.setText(_translate("Dialog", "坐标纬度"))
        self.label_6.setText(_translate("Dialog", "建筑图片地址"))

    def get_data(self):
        return self.cidEdit.text(), self.bidEdit.text(), self.nameEdit.text(), self.longitudeEdit.text(), self.latitudeEdit.text(), self.imageEdit.text()


class ClientWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ClientWindow, self).__init__(parent)
        self.setupUi(self)
        self.categoriesTable.setColumnWidth(0, 64)
        self.categoriesTable.setColumnWidth(1, 64)
        self.categoriesTable.setColumnWidth(2, 199)
        self.categoriesTable.setColumnWidth(3, 199)
        self.categoriesTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.categoriesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.categoriesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.buildingsTable.setColumnWidth(0, 64)
        self.buildingsTable.setColumnWidth(1, 64)
        self.buildingsTable.setColumnWidth(2, 120)
        self.buildingsTable.setColumnWidth(3, 120)
        self.buildingsTable.setColumnWidth(4, 120)
        self.buildingsTable.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.buildingsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.buildingsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.openButton.clicked.connect(self.openfile)
        self.saveButton.clicked.connect(self.savefile)
        self.catAddBut.clicked.connect(self.cat_add)
        self.catDelBut.clicked.connect(self.cat_del)
        self.catModBut.clicked.connect(self.cat_mod)
        self.budAddBut.clicked.connect(self.bud_add)
        self.budDelBut.clicked.connect(self.bud_del)
        self.budModBut.clicked.connect(self.bud_mod)
        self.categoriesTable.itemClicked.connect(self.category_click)

    @pyqtSlot()
    def openfile(self):
        file_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'JSON files(*.json)')[0]
        print(file_name)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as f:
                nav_data = json.load(f)
                print(nav_data)
            categories = nav_data['categories']
            buildings = nav_data['buildings']
            self.categoriesTable.setRowCount(0)
            self.buildingsTable.setRowCount(0)
            for category in categories:
                row_count = self.categoriesTable.rowCount()
                self.categoriesTable.setRowCount(row_count + 1)
                self.categoriesTable.setItem(row_count, 0, QTableWidgetItem(str(category['cid'])))
                self.categoriesTable.setItem(row_count, 1, QTableWidgetItem(category['name']))
                self.categoriesTable.setItem(row_count, 2, QTableWidgetItem(category['icon']))
                self.categoriesTable.setItem(row_count, 3, QTableWidgetItem(category['tapIcon']))
                self.categoriesTable.setItem(row_count, 4, QTableWidgetItem(str(category['quantities'])))
                for index in range(self.categoriesTable.columnCount()):
                    self.categoriesTable.item(row_count, index).setTextAlignment(Qt.AlignCenter)
            for building in buildings:
                row_count = self.buildingsTable.rowCount()
                self.buildingsTable.setRowCount(row_count + 1)
                self.buildingsTable.setItem(row_count, 0, QTableWidgetItem(str(building['cid'])))
                self.buildingsTable.setItem(row_count, 1, QTableWidgetItem(str(building['bid'])))
                self.buildingsTable.setItem(row_count, 2, QTableWidgetItem(building['name']))
                self.buildingsTable.setItem(row_count, 3, QTableWidgetItem(str(building['longitude'])))
                self.buildingsTable.setItem(row_count, 4, QTableWidgetItem(str(building['latitude'])))
                self.buildingsTable.setItem(row_count, 5, QTableWidgetItem(building['image']))
                for index in range(self.buildingsTable.columnCount()):
                    self.buildingsTable.item(row_count, index).setTextAlignment(Qt.AlignCenter)

    @pyqtSlot()
    def savefile(self):
        try:
            categories = []
            row_count = self.categoriesTable.rowCount()
            for i in range(0, row_count):
                category = {}
                category['cid'] = int(self.categoriesTable.item(i, 0).text())
                category['name'] = self.categoriesTable.item(i, 1).text()
                category['icon'] = self.categoriesTable.item(i, 2).text()
                category['tapIcon'] = self.categoriesTable.item(i, 3).text()
                category['quantities'] = int(self.categoriesTable.item(i, 4).text())
                categories.append(category)
            buildings = []
            row_count = self.buildingsTable.rowCount()
            for i in range(0, row_count):
                building = {}
                building['cid'] = int(self.buildingsTable.item(i, 0).text())
                building['bid'] = int(self.buildingsTable.item(i, 1).text())
                building['name'] = self.buildingsTable.item(i, 2).text()
                building['longitude'] = float(self.buildingsTable.item(i, 3).text())
                building['latitude'] = float(self.buildingsTable.item(i, 4).text())
                building['image'] = self.buildingsTable.item(i, 5).text()
                buildings.append(building)
            nav_data = {'categories': categories, 'buildings': buildings}
            print(nav_data)
            file_name = QFileDialog.getSaveFileName(self, '保存文件', '', 'JSON files(*.json)')[0]
            print(file_name)
            if file_name:
                with open(file_name, 'w', encoding="utf-8") as f:
                    json.dump(nav_data, f, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
        except Exception as e:
            QMessageBox.warning(self, "警告", "出现异常，无法保存！\n请排除异常后再试！\n\n 异常信息：\n" + str(e), QMessageBox.Yes)

    @pyqtSlot()
    def cat_add(self):
        category_dialog = CategoryDialog('添加分类', '', '', '', '', '')
        if category_dialog.exec_():
            print(category_dialog.get_data())
            category = category_dialog.get_data()
            row_count = self.categoriesTable.rowCount()
            self.categoriesTable.setRowCount(row_count + 1)
            self.categoriesTable.setItem(row_count, 0, QTableWidgetItem(category[0]))
            self.categoriesTable.setItem(row_count, 1, QTableWidgetItem(category[1]))
            self.categoriesTable.setItem(row_count, 2, QTableWidgetItem(category[2]))
            self.categoriesTable.setItem(row_count, 3, QTableWidgetItem(category[3]))
            self.categoriesTable.setItem(row_count, 4, QTableWidgetItem(category[4]))
            for index in range(self.categoriesTable.columnCount()):
                self.categoriesTable.item(row_count, index).setTextAlignment(Qt.AlignCenter)

    @pyqtSlot()
    def cat_del(self):
        print(self.categoriesTable.currentRow())
        if self.categoriesTable.currentRow() < 0:
            QMessageBox.warning(self, "警告", "请先选择一行分类！", QMessageBox.Yes )
        else:
            reply = QMessageBox.information(self, "确认", "是否删除分类 " + self.categoriesTable.item(self.categoriesTable.currentRow(), 1).text(), QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.categoriesTable.removeRow(self.categoriesTable.currentRow())

    @pyqtSlot()
    def cat_mod(self):
        print(self.categoriesTable.currentRow())
        if self.categoriesTable.currentRow() < 0:
            QMessageBox.warning(self, "警告", "请先选择一行分类！", QMessageBox.Yes)
        else:
            select_row = self.categoriesTable.currentRow()
            category_dialog = CategoryDialog('修改分类', self.categoriesTable.item(select_row, 0).text(),
                                             self.categoriesTable.item(select_row, 1).text(),
                                             self.categoriesTable.item(select_row, 2).text(),
                                             self.categoriesTable.item(select_row, 3).text(),
                                             self.categoriesTable.item(select_row, 4).text())
            if category_dialog.exec_():
                print(category_dialog.get_data())
                category = category_dialog.get_data()
                self.categoriesTable.setItem(select_row, 0, QTableWidgetItem(category[0]))
                self.categoriesTable.setItem(select_row, 1, QTableWidgetItem(category[1]))
                self.categoriesTable.setItem(select_row, 2, QTableWidgetItem(category[2]))
                self.categoriesTable.setItem(select_row, 3, QTableWidgetItem(category[3]))
                self.categoriesTable.setItem(select_row, 4, QTableWidgetItem(category[4]))
                for index in range(self.categoriesTable.columnCount()):
                    self.categoriesTable.item(select_row, index).setTextAlignment(Qt.AlignCenter)

    @pyqtSlot()
    def bud_add(self):
        building_dialog = BuildingDialog('添加建筑', '', '', '', '', '', '')
        if building_dialog.exec_():
            print(building_dialog.get_data())
            building = building_dialog.get_data()
            row_count = self.buildingsTable.rowCount()
            self.buildingsTable.setRowCount(row_count + 1)
            self.buildingsTable.setItem(row_count, 0, QTableWidgetItem(building[0]))
            self.buildingsTable.setItem(row_count, 1, QTableWidgetItem(building[1]))
            self.buildingsTable.setItem(row_count, 2, QTableWidgetItem(building[2]))
            self.buildingsTable.setItem(row_count, 3, QTableWidgetItem(building[3]))
            self.buildingsTable.setItem(row_count, 4, QTableWidgetItem(building[4]))
            self.buildingsTable.setItem(row_count, 5, QTableWidgetItem(building[5]))
            for index in range(self.buildingsTable.columnCount()):
                self.buildingsTable.item(row_count, index).setTextAlignment(Qt.AlignCenter)

    @pyqtSlot()
    def bud_del(self):
        print(self.buildingsTable.currentRow())
        if self.buildingsTable.currentRow() < 0:
            QMessageBox.warning(self, "警告", "请先选择一行建筑！", QMessageBox.Yes)
        else:
            reply = QMessageBox.information(self, "确认",  "是否删除建筑 " + self.buildingsTable.item(self.buildingsTable.currentRow(), 2).text(), QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.buildingsTable.removeRow(self.buildingsTable.currentRow())

    @pyqtSlot()
    def bud_mod(self):
        print(self.buildingsTable.currentRow())
        if self.buildingsTable.currentRow() < 0:
            QMessageBox.warning(self, "警告", "请先选择一行建筑！", QMessageBox.Yes)
        else:
            select_row = self.buildingsTable.currentRow()
            building_dialog = BuildingDialog('修改建筑', self.buildingsTable.item(select_row, 0).text(),
                                             self.buildingsTable.item(select_row, 1).text(),
                                             self.buildingsTable.item(select_row, 2).text(),
                                             self.buildingsTable.item(select_row, 3).text(),
                                             self.buildingsTable.item(select_row, 4).text(),
                                             self.buildingsTable.item(select_row, 5).text())
            if building_dialog.exec_():
                print(building_dialog.get_data())
                building = building_dialog.get_data()
                self.buildingsTable.setItem(select_row, 0, QTableWidgetItem(building[0]))
                self.buildingsTable.setItem(select_row, 1, QTableWidgetItem(building[1]))
                self.buildingsTable.setItem(select_row, 2, QTableWidgetItem(building[2]))
                self.buildingsTable.setItem(select_row, 3, QTableWidgetItem(building[3]))
                self.buildingsTable.setItem(select_row, 4, QTableWidgetItem(building[4]))
                self.buildingsTable.setItem(select_row, 5, QTableWidgetItem(building[5]))
                for index in range(self.buildingsTable.columnCount()):
                    self.buildingsTable.item(select_row, index).setTextAlignment(Qt.AlignCenter)

    @pyqtSlot()
    def category_click(self):
        category = self.categoriesTable.item(self.categoriesTable.currentRow(), 0).text()
        row_count = self.buildingsTable.rowCount()
        print(row_count)
        for i in range(0, row_count):
            self.buildingsTable.setRowHidden(i, True)
            if self.buildingsTable.item(i, 0).text() == category:
                self.buildingsTable.setRowHidden(i, False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clientWindow = ClientWindow()
    clientWindow.show()
    sys.exit(app.exec_())