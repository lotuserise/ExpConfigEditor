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
		self.tableWidget.setColumnCount(23)
		self.tableWidget.setRowCount(23)
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
		self.LoadiniComboBox(MainWindow)
		self.CreateTab(MainWindow)
		self.LoadTale(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):

		#create Window
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

		#Create Button
		self.pushButton.setText(_translate("MainWindow", "File Save", None))
		self.pushButton.setEnabled(False)
		self.pushButton_1.setText(_translate("MainWindow", "File Read", None))
		self.label.setText(_translate("MainWindow", "Exp.Info.", None))

	def LoadiniComboBox(self, MainWindow):
		for combo in range(0,22):
			self.MyCombo = QtGui.QComboBox()
			self.tableWidget.setCellWidget(combo,0,self.MyCombo)

		self.MyCombo = QtGui.QComboBox()
		config = configparser.ConfigParser()
		config.read('fe_tc.ini')
		config.sections()

		detector1=config['SCM1']['DetectorName']
		#Disable of Combobox
		self.MyCombo.setEnabled(False)
		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.addItem (detector1)
		self.tableWidget.setCellWidget(0,0,self.MyCombo)

		detector2=config['SCM1']['Type[Camera]']
		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.setEnabled(False)
		self.MyCombo.addItem (detector2)
		self.tableWidget.setCellWidget(1,0,self.MyCombo)

		detector3=config['SCM1']['HostName[Camera]']
		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.setEnabled(False)
		self.MyCombo.addItem (detector3)
		self.tableWidget.setCellWidget(2,0,self.MyCombo)

		detector4=config['SCM1']['HostName[LossLess]']
		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.setEnabled(False)
		self.MyCombo.addItem (detector4)
		self.tableWidget.setCellWidget(3,0,self.MyCombo)

		detector4=config['SCM1']['HostName[Storage]']
		self.MyCombo = QtGui.QComboBox()
#		self.MyCombo.setEnabled(False)
		self.MyCombo.addItem (detector4)
		self.tableWidget.setCellWidget(4,0,self.MyCombo)

		detector4=config['SCM1']['Object[CamerServer]']
		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.setEnabled(False)
		self.MyCombo.addItem (detector4)
		self.tableWidget.setCellWidget(5,0,self.MyCombo)

		detector4=config['SCM1']['Object[VME_Board]']
		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.setEnabled(False)
		self.MyCombo.addItem (detector4)
		self.tableWidget.setCellWidget(6,0,self.MyCombo)

		detector4=config['SCM1']['Object[CameraSelector]']
		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.setEnabled(False)
		self.MyCombo.addItem (detector4)
		self.tableWidget.setCellWidget(7,0,self.MyCombo)

		detector4=config['SCM1']['Object[Trigger]']
		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.setEnabled(False)
		self.MyCombo.addItem (detector4)
		self.tableWidget.setCellWidget(8,0,self.MyCombo)

	def StorageSelect(self, MainWindow):
		pass

	def CreateTab(self, MainWindow):
		#create Tab
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "TEST", None))

	def LoadTale(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		#Set Hedder_Label

		#onelinerでまとめる場合（リスト配列化） 
		data = [ v for v in csv.reader(open("exp_2015.csv", "r")) if len(v) != 0]

		#set VerticalHeadderLabel
		setVerticalLabels = self.tableWidget.setVerticalHeaderLabels((data[1][0],data[1][1],data[1][2],data[1][3],data[1][4],
			data[1][5],data[1][6],data[1][7],data[1][8],data[1][9],data[1][10],data[1][11],data[1][12],data[1][13],
			data[1][14],data[1][15],data[1][16],data[1][17],data[1][18],data[1][19],data[1][20],data[1][21],data[1][22]))

		#set HorizonalHeadderLabel

		horizontal_header=[]
		for a in range(2,len(data)):
			list1=data[a][0]
			horizontal_header.append(list1)

		SetHorizontalLabels = self.tableWidget.setHorizontalHeaderLabels(horizontal_header)
		self.tableWidget.setColumnCount((len(data)-2))

#		exp_csv = open("exp_2015.csv",'rt')
#		lines = exp_csv.readlines()
#		exp_csv.close()
#		addr = lines[1]
#		addr1=addr.split(",")
#		vh = list(addr1)
#		self.tableWidget.setColumnCount(len(cals2))

#		setVerticalLabels=self.tableWidget.setVerticalHeaderLabels((vh[0],vh[1],vh[2],vh[3],vh[4],vh[5],vh[6],vh[7],
#			vh[8],vh[9],vh[10],vh[11],vh[12],vh[13],vh[14],vh[15],vh[16],vh[17],vh[18],vh[19],vh[20],vh[21],vh[22]))

#		addr = lines[2]
#		addr1=addr.split(",")
#		hl = list(addr1)
#		setHorizontalLabels =self.tableWidget.setHorizontalHeaderLabels((hl[0],hl[1],hl[2],))

#		vertical_header = csv.reader(open('exp.csv','rt'), delimiter=',')
#		cals1=list(vertical_header)
#		self.tableWidget.setColumnCount(len(cals1))
#		for data1 in cals1:
#			setcaldata1 = self.tableWidget.setVerticalHeaderLabels(data1)

#		horizontal_header = csv.reader(open('horizon.csv','rt'), delimiter=',')
#		cals2=list(horizontal_header)
#		self.tableWidget.setColumnCount(20)
#		for data2 in cals2:
#			setcaldata2 =self.tableWidget.setHorizontalHeaderLabels(data2)

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