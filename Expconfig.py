# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExpConfigEditor(new).ui'
#
# Created: Wed Jan 28 08:58:48 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import csv
import string
import datetime
import traceback
import os.path
import sys
import logging
from functools import reduce
import configparser


try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(1200, 680)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.tabWidget = QtGui.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(10, 50, 731, 601))
		self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
		self.tabWidget.setIconSize(QtCore.QSize(20, 20))
		self.tabWidget.setDocumentMode(False)
		self.tabWidget.setTabsClosable(False)
		self.tabWidget.resize(900,700)
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		self.tab = QtGui.QWidget()
		self.tab.setObjectName(_fromUtf8("tab"))
		self.tabWidget.addTab(self.tab, _fromUtf8(""))

		self.tableWidget = QtGui.QTableWidget(self.tab)
		self.tableWidget.setGeometry(QtCore.QRect(10, 10, 731, 601))
		self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
		self.tableWidget.setColumnCount(24)
		self.tableWidget.setRowCount(24)
		self.tableWidget.resize(800,600)

		#label setting
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(10, 10, 181, 41))
		self.label.setWordWrap(False)
		self.label.setObjectName(_fromUtf8("label"))

		#pushButton setting
		self.pushButton = QtGui.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(950, 520, 100, 50))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		MainWindow.setCentralWidget(self.centralwidget)

		self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_1.setGeometry(QtCore.QRect(950, 600, 100, 50))
		self.pushButton_1.setObjectName(_fromUtf8("pushButton"))
		MainWindow.setCentralWidget(self.centralwidget)

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 24))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
 
 		#Load Function
		self.retranslateUi(MainWindow)
		self.CreateTab(MainWindow)
		self.LoadTale(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):

		#Create Window
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

		#Create Button
		self.pushButton.setText(_translate("MainWindow", "File Save", None))
		self.pushButton.setEnabled(False)
		self.pushButton_1.setText(_translate("MainWindow", "File Read", None))
		self.label.setText(_translate("MainWindow", "Exp.Info.", None))

	def StorageSelect(self, MainWindow):
		pass

	def CreateTab(self, MainWindow):
		#create Tab
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "TEST", None))

	def LoadTale(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

		#csvを配列化 
		data1 = [ v for v in csv.reader(open("exp_2015.csv", "r")) if len(v) != 0]

		for i in range(2,len(data1)):
			for j in range(0,len(data1[2])-1):
				x = data1[i][j]
				self.MyCombo = QtGui.QComboBox()
				self.MyCombo.addItem(data1[i][j])
				#1行目と2行目を省いてデータをセルに入力
				self.tableWidget.setCellWidget(j,i-2,self.MyCombo)

		data = [ v for v in csv.reader(open("exp_2015.csv", "r")) if len(v) != 0]

		#VerticalHeadderLabels
		vertical_header=[]
		for row in range(0,len(data[1])):
			list1=data[1][row]
			vertical_header.append(list1)

		setVerticalLabels = self.tableWidget.setVerticalHeaderLabels(vertical_header)
		self.tableWidget.setRowCount((len(data[1])))

		#HorizonalHeadderLabels
		horizontal_header=[]
		for col in range(2,len(data)):
			list2=data[col][0]
			horizontal_header.append(list2)

		SetHorizontalLabels = self.tableWidget.setHorizontalHeaderLabels(horizontal_header)
		self.tableWidget.setColumnCount((len(data)-2))

	def FileSave(self):
		pass

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())