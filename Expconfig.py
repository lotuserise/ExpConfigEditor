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
		MainWindow.resize(1000, 680)
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
		self.tab_2 = QtGui.QWidget()
		self.tab_2.setObjectName(_fromUtf8("tab_2"))
		self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
		self.tab_3 = QtGui.QWidget()
		self.tab_3.setObjectName(_fromUtf8("tab_3"))
		self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
		self.tab_4 = QtGui.QWidget()
		self.tab_4.setObjectName(_fromUtf8("tab_4"))
		self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
		self.tab_5 = QtGui.QWidget()
		self.tab_5.setObjectName(_fromUtf8("tab_5"))
		self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
		self.tab_6 = QtGui.QWidget()
		self.tab_6.setObjectName(_fromUtf8("tab_6"))
		self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
		self.tab_7 = QtGui.QWidget()
		self.tab_7.setObjectName(_fromUtf8("tab_7"))
		self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
		self.tab_8 = QtGui.QWidget()
		self.tab_8.setObjectName(_fromUtf8("tab_8"))
		self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
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
		self.MyCombo.setEnabled(False)
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

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 24))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):

		#create Window
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

		#create Tab
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "SSCH", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "FE/TC", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "ST1", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "ST2", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "ST4c", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "ST5", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "ST6", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "CCSR", None))

		#Set Label
		vertical_header = csv.reader(open('exp.csv','rt'), delimiter=',')
		cals1=list(vertical_header)
		self.tableWidget.setColumnCount(len(cals1))
		for data1 in cals1:
			setcaldata1 = self.tableWidget.setVerticalHeaderLabels(data1)

		horizontal_header = open("exp_2015.csv",'rt')
		lines = horizontal_header.readlines()
		horizontal_header.close()
		addr = lines[1]
		addr1=addr.split(",")
		cals2 = list(addr1)
		self.tableWidget.setColumnCount(len(cals2))
		setcaldata2 =self.tableWidget.setHorizontalHeaderLabels((cals2[0],cals2[1],cals2[2],cals2[3],cals2[4]))

#		horizontal_header = csv.reader(open('horizon.csv','rt'), delimiter=',')
#		cals2=list(horizontal_header)
#		self.tableWidget.setColumnCount(20)
#		for data2 in cals2:
#			setcaldata2 =self.tableWidget.setHorizontalHeaderLabels(data2)

		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.addItem("IMPERX")
		self.MyCombo.addItem("MPCCD")         
		self.tableWidget.setCellWidget(0,1,self.MyCombo)
		#ComboBox Copy

		#Create Button
		self.pushButton.setText(_translate("MainWindow", "File Save", None))
		self.pushButton.setEnabled(False)
		self.pushButton_1.setText(_translate("MainWindow", "File Read", None))
		self.label.setText(_translate("MainWindow", "Exp.Info.", None))

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())