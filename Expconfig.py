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

		#menubar
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 3000, 24))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menuFile = QtGui.QMenu(self.menubar)
		self.menuFile.setObjectName(_fromUtf8("menuFile"))
		self.menuLoad = QtGui.QMenu(self.menubar)
		self.menuLoad.setObjectName(_fromUtf8("menuLoad"))
		self.actionTest = QtGui.QAction(MainWindow)
		self.actionTest.setObjectName(_fromUtf8("actionTest"))
		self.menuFile.addAction(self.actionTest)
		self.menubar.addAction(self.menuFile.menuAction())
 
		#label setting
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(10, 15, 181, 41))
		self.label.setWordWrap(False)
		self.label.setObjectName(_fromUtf8("label"))

		#pushButton setting
		self.pushButton = QtGui.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(950, 520, 100, 50))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		MainWindow.setCentralWidget(self.centralwidget)
		self.pushButton.clicked.connect(self.FileSave)

		self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_1.setGeometry(QtCore.QRect(950, 600, 100, 50))
		self.pushButton_1.setObjectName(_fromUtf8("pushButton"))
		MainWindow.setCentralWidget(self.centralwidget)
		self.pushButton_1.clicked.connect(self.FileLoad)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 24))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow )
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
		self.pushButton_1.setText(_translate("MainWindow", "File Read", None))
		self.label.setText(_translate("MainWindow", "Exp.Info.", None))

		self.menuFile.setTitle(_translate("MainWindow", "File", None))
		self.menuLoad.setTitle(_translate("MainWindow", "Load", None))
		self.actionTest.setText(_translate("MainWindow", "Load", None))
		self.actionTest.setText(_translate("MainWindow", "Save", None))

	def StorageSelect(self, MainWindow):
		pass

	def CreateTab(self, MainWindow):
		#create Tab
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "TEST", None))

	def LoadTale(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

		#initializations of arrays
		data1 = [ v for v in csv.reader(open("exp_2015.csv", "r")) if len(v) != 0]

		#read csv file
		for column in range(2,len(data1)):
			for row in range(0,len(data1[2])-1):
				x = data1[column][row]
				self.MyCombo = QtGui.QComboBox()
				self.MyCombo.addItem(data1[column][row])
				#1行目と2行目を省いてデータをセルに入力
				self.tableWidget.setCellWidget(row,column-2,self.MyCombo)
				item = QtGui.QTableWidgetItem(data1[column][row])
				self.tableWidget.setItem(row, column,item)

		data = [ v for v in csv.reader(open("exp_2015.csv", "r")) if len(v) != 0] 

		#VerticalHeadderLabels
		vertical_header=[]
		for row in range(0,len(data[1])):
			list1 =data[1][row]
			vertical_header.append(list1)

		setVerticalLabels = self.tableWidget.setVerticalHeaderLabels(vertical_header)
		self.tableWidget.setRowCount((len(data[1])))

		#HorizonalHeadderLabels
		horizontal_header=[]
		for col in range(2,len(data) ):
			list2=data[col][0]
			horizontal_header.append(list2)

		SetHorizontalLabels = self.tableWidget.setHorizontalHeaderLabels(horizontal_header)
		self.tableWidget.setColumnCount((len(data)-2))

	def FileSave(self,MainWindow):
		#FileName
		path = QtGui.QFileDialog.getSaveFileName(None, 'Save current As...', './', "CSV File (*.csv)" )
		writefile=open(path,'wb')
		
		# write array of column & row data in a csv file
		with writefile:
			for column in range(0,self.tableWidget.columnCount()):
				rowdata = []
				for row in range(0,self.tableWidget.rowCount()):
					item = self.tableWidget.item(row, column)
					csv = ",".join(rowdata)
					if item is not None:
						rowdata.append(item.text())
					else: 
						rowdata.append('')
				writefile.write(csv+"\n")

	def FileLoad(self,MainWindow):
		path = QtGui.QFileDialog.getOpenFileName(None, "Open File",'CSV(*.csv)')
		readfile=open(path,'rb')

		# read array of column & row data in a csv file
		if not path.isEmpty():
			with readfile:
				self.table.setRowCount(0)
				self.table.setColumnCount(0)
				for rowdata in csv.reader(stream):
					row = self.table.rowCount()
					self.table.insertRow(row)
					self.table.setColumnCount(len(rowdata))
					for column, data in enumerate(rowdata):
						item = QtGui.QTableWidgetItem(data.decode('utf8'))
						self.table.setItem(row, column, item)

		#read csv file
		for column in range(2,len(readfile)):
			for row in range(0,len(readfile[2])-1):
				x = readfile[column][row]
				self.MyCombo = QtGui.QComboBox()
				self.MyCombo.addItem(readfile[column][row])
				#1行目と2行目を省いてデータをセルに入力
				self.tableWidget.setCellWidget(row,column-2,self.MyCombo)
				item = QtGui.QTableWidgetItem(readfile[column][row])
				self.tableWidget.setItem(row, column,item)

		#VerticalHeadderLabels
		vertical_header=[]
		for row in range(0,len(readfile[1])):
			list1 =data[1][row]
			vertical_header.append(list1)

		setVerticalLabels = self.tableWidget.setVerticalHeaderLabels(vertical_header)
		self.tableWidget.setRowCount((len(readfile[1])))

		#HorizonalHeadderLabels
		horizontal_header=[]
		for col in range(2,len(readfile) ):
			list2=data[col][0]
			horizontal_header.append(list2)

		SetHorizontalLabels = self.tableWidget.setHorizontalHeaderLabels(horizontal_header)
		self.tableWidget.setColumnCount((len(readfile)-2))

	def ComboSelect(self):
		pass

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())