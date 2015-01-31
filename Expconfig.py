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
		self.tabWidget.resize(820,600)
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
		self.tabWidget.addTab(self.tab_7, _fromUtf8(""))

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
		self.pushButton.setGeometry(QtCore.QRect(850, 520, 100, 50))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		MainWindow.setCentralWidget(self.centralwidget)

		self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_1.setGeometry(QtCore.QRect(850, 600, 100, 50))
		self.pushButton_1.setObjectName(_fromUtf8("pushButton"))
		MainWindow.setCentralWidget(self.centralwidget)

		#ComboBox Copy
		for combo in range(0,22):
			self.MyCombo = QtGui.QComboBox()
			self.tableWidget.setCellWidget(combo,0,self.MyCombo)
			
		config = configparser.ConfigParser()
		config.read('config.ini')
		config.sections()
		detector1=config['DetectorName']['Detector1']
		detector2=config['DetectorName']['Detector2']
		self.MyCombo = QtGui.QComboBox()
		self.MyCombo.addItem (detector1)
		self.MyCombo.addItem (detector2)
		self.tableWidget.setCellWidget(0,0,self.MyCombo)

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

		#SetColumLabel
		config_header = csv.reader(open('exp.csv','rt'), delimiter=',')
		cals=list(config_header)
		self.tableWidget.setColumnCount(len(cals))
#		self.tableWidget.setRowCount(len(cals))
		for data in cals:
			setrowdata = self.tableWidget.setVerticalHeaderLabels(data)
#			setrowdata = self.tableWidget.setHorizontalHeaderLabels(data)

		#SetRowLabel
		#Create Button
		self.pushButton.setText(_translate("MainWindow", "File Save", None))
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