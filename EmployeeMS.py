# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmployeeMS.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem
from PyQt5.QtCore import Qt
from datetime import datetime
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1314, 883)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1301, 51))
        self.label.setStyleSheet("font: 26pt \"Algerian\";\n"
"background-color: rgb(176, 176, 176);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 1301, 20))
        self.line.setStyleSheet("background-color: rgb(48, 58, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 441, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/asus/Downloads/Black And Blue Simple Travel Banner Landscape (2).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 70, 451, 191))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/asus/Downloads/Black And Blue Simple Travel Banner Landscape (1).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(900, 70, 411, 191))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/asus/Downloads/Black And Blue Simple Travel Banner Landscape.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 1301, 541))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/asus/Downloads/Untitled design (11).png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 270, 1271, 521))
        self.frame.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 0, 271, 31))
        self.label_6.setStyleSheet("color: rgb(255, 8, 32);\n"
"font: 14pt \"Algerian\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.label_7.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.label_8.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 101, 31))
        self.label_9.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.label_10.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 190, 101, 31))
        self.label_11.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(340, 30, 101, 31))
        self.label_12.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(340, 70, 101, 31))
        self.label_13.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(340, 110, 111, 31))
        self.label_14.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(340, 150, 111, 31))
        self.label_15.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(340, 190, 101, 31))
        self.label_16.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(680, 30, 101, 31))
        self.label_17.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(680, 70, 101, 31))
        self.label_18.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(680, 110, 101, 31))
        self.label_19.setStyleSheet("\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(120, 40, 191, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 200, 191, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(470, 120, 191, 22))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(470, 200, 191, 22))
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(120, 160, 191, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_2.setGeometry(QtCore.QRect(470, 160, 191, 22))
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(120, 80, 191, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 120, 191, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 40, 191, 22))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 80, 191, 22))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(790, 40, 191, 22))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(790, 80, 191, 22))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(790, 120, 191, 22))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1050, 40, 201, 41))
        self.pushButton.setStyleSheet("background-color: rgb(40, 25, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(1050, 90, 201, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(40, 25, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(1050, 140, 201, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(40, 25, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(1050, 190, 201, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(40, 25, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 230, 1271, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(550, 290, 55, 16))
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(0, 240, 1271, 31))
        self.label_21.setStyleSheet("color: rgb(4, 4, 4);\n"
"background-color: rgb(144, 144, 144);\n"
"font: 14pt \"Algerian\";")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 271, 1251, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1314, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "EMPLOYEE MANAGEMENT SYSTEM"))
        self.label_6.setText(_translate("MainWindow", "EMPLOYEE INFORMATION"))
        self.label_7.setText(_translate("MainWindow", "Department"))
        self.label_8.setText(_translate("MainWindow", "Designation"))
        self.label_9.setText(_translate("MainWindow", "Address"))
        self.label_10.setText(_translate("MainWindow", "Date Of Birth"))
        self.label_11.setText(_translate("MainWindow", "Identity"))
        self.label_12.setText(_translate("MainWindow", "Name"))
        self.label_13.setText(_translate("MainWindow", "Email"))
        self.label_14.setText(_translate("MainWindow", "Married Status"))
        self.label_15.setText(_translate("MainWindow", "Date Of joining"))
        self.label_16.setText(_translate("MainWindow", "Gender"))
        self.label_17.setText(_translate("MainWindow", "Phone NO."))
        self.label_18.setText(_translate("MainWindow", "Country"))
        self.label_19.setText(_translate("MainWindow", "Salary(CTC)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "IT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "HR"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Admin"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Sales Dept"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Accounts"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "AADHAR CARD"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "PEN CARD"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Voter ID Card"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Driving License"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Married"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "UnMarried"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Divorced"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Male"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Female"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_3.setText(_translate("MainWindow", "Update"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset"))
        self.label_21.setText(_translate("MainWindow", "EMPLOYEE INFORMATION RECORD"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Department"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Designation"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date Of Birth"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Identity"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Married Status"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Date Of joining"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Phone NO."))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Country"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Salary(CTC)"))
        self.initEvent()

    def initEvent(self):
        self.pushButton.clicked.connect(self.saveData)
        self.pushButton_2.clicked.connect(self.deleteData)
        self.pushButton_3.clicked.connect(self.updateData)
        self.pushButton_4.clicked.connect(self.resetData)

    def saveData(self):
        #data retrieve
        department = self.comboBox.currentText()
        designation = self.lineEdit.text()
        address = self.lineEdit_2.text()
        date_of_birth = self.dateEdit.date().toString(Qt.ISODate)
        identity = self.comboBox_2.currentText()
        name = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        married_status = self.comboBox_3.currentText()
        date_of_joining = self.dateEdit_2.date().toString(Qt.ISODate)
        gender = self.comboBox_4.currentText()
        phone_number = self.lineEdit_5.text()
        country = self.lineEdit_6.text()
        salary = self.lineEdit_7.text()

        # data add to the table

        row_position = self.tableWidget.rowCount()
        # print(row_position)
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(department))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(designation))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(address))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(date_of_birth))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(identity))
        self.tableWidget.setItem(row_position, 5, QTableWidgetItem(name))
        self.tableWidget.setItem(row_position, 6, QTableWidgetItem(email))
        self.tableWidget.setItem(row_position, 7, QTableWidgetItem(married_status))
        self.tableWidget.setItem(row_position, 8, QTableWidgetItem(date_of_joining))
        self.tableWidget.setItem(row_position, 9, QTableWidgetItem(gender))
        self.tableWidget.setItem(row_position, 10, QTableWidgetItem(phone_number))
        self.tableWidget.setItem(row_position, 11, QTableWidgetItem(country))
        self.tableWidget.setItem(row_position, 12, QTableWidgetItem(salary))
        
    def deleteData(self):
        selected_rows = self.tableWidget.selectedItems()
        # print("Row is..",selected_rows)
        
        if not selected_rows:
                print("No rows selected for deletion..")
                return
        selected_rows_indices = set(item.row() for item in selected_rows)
        print(selected_rows_indices)

        for row_index in sorted(selected_rows_indices, reverse = True):
                self.tableWidget.removeRow(row_index)
        
        
    def updateData(self):
        selected_rows = set(index.row() for index in self.tableWidget.selectedIndexes())
        print("selected rows.",selected_rows)

        if not selected_rows or len(selected_rows) > 1:
                print("Please select a single row to update..")
                return

        row_index = next(iter(selected_rows))
        #retrieve data
        department = self.tableWidget.item(row_index,0).text()
        designation = self.tableWidget.item(row_index,1).text()
        address = self.tableWidget.item(row_index,2).text()
        date_of_birth = self.tableWidget.item(row_index,3).text()
        identity = self.tableWidget.item(row_index,4).text()
        name = self.tableWidget.item(row_index,5).text()
        email = self.tableWidget.item(row_index,6).text()
        married_status = self.tableWidget.item(row_index,7).text()
        date_of_joining = self.tableWidget.item(row_index,8).text()
        gender = self.tableWidget.item(row_index,9).text()
        phone_number = self.tableWidget.item(row_index,10).text()
        country = self.tableWidget.item(row_index,11).text()
        salary = self.tableWidget.item(row_index,12).text()

        #set data
        self.comboBox.setCurrentText(department)
        self.lineEdit.setText(designation)
        self.lineEdit_2.setText(address)
        self.dateEdit.setDate(QtCore.QDate.fromString(date_of_birth, Qt.ISODate))
        self.comboBox_2.setCurrentText(identity)
        self.lineEdit_3.setText(name)
        self.lineEdit_4.setText(email)
        self.comboBox_3.setCurrentText(married_status)
        self.dateEdit_2.setDate(QtCore.QDate.fromString(date_of_joining, Qt.ISODate))
        self.comboBox_4.setCurrentText(gender)
        self.lineEdit_5.setText(phone_number)
        self.lineEdit_6.setText(country)
        self.lineEdit_7.setText(salary)
        

    def resetData(self):
        #clear inputs
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.dateEdit.setDate(QDate(2000, 1, 1))
        self.dateEdit_2.setDate(QDate(2000, 1, 1))
        # self.dateEdit.setDate(datetime.now().date())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
