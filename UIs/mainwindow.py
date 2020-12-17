# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Sun May 24 10:15:37 2020
#      by: pyside2-uic  running on PySide2 5.9.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1330, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbw_data = QtWidgets.QTableWidget(self.centralwidget)
        self.tbw_data.setGeometry(QtCore.QRect(10, 10, 1311, 521))
        self.tbw_data.setObjectName("tbw_data")
        self.tbw_data.setColumnCount(0)
        self.tbw_data.setRowCount(0)
        self.lw_parametrs = QtWidgets.QListWidget(self.centralwidget)
        self.lw_parametrs.setGeometry(QtCore.QRect(1300, 540, 21, 21))
        self.lw_parametrs.setObjectName("lw_parametrs")
        self.cb_method = QtWidgets.QComboBox(self.centralwidget)
        self.cb_method.setGeometry(QtCore.QRect(220, 540, 381, 31))
        self.cb_method.setObjectName("cb_method")
        self.btn_setFile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setFile.setGeometry(QtCore.QRect(100, 540, 101, 31))
        self.btn_setFile.setObjectName("btn_setFile")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(500, 700, 101, 31))
        self.btn_start.setObjectName("btn_start")
        self.btn_stat = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stat.setGeometry(QtCore.QRect(500, 640, 101, 31))
        self.btn_stat.setObjectName("btn_stat")
        self.chb_twice = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_twice.setGeometry(QtCore.QRect(1300, 560, 20, 31))
        self.chb_twice.setObjectName("chb_twice")
        self.cb_metric = QtWidgets.QComboBox(self.centralwidget)
        self.cb_metric.setGeometry(QtCore.QRect(220, 590, 381, 31))
        self.cb_metric.setObjectName("cb_metric")
        self.cb_parametr1 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_parametr1.setGeometry(QtCore.QRect(660, 540, 361, 31))
        self.cb_parametr1.setObjectName("cb_parametr1")
        self.cb_parametr2 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_parametr2.setGeometry(QtCore.QRect(660, 590, 361, 31))
        self.cb_parametr2.setObjectName("cb_parametr2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 700, 31, 21))
        self.label.setObjectName("label")
        self.spb_k_count = QtWidgets.QSpinBox(self.centralwidget)
        self.spb_k_count.setGeometry(QtCore.QRect(720, 700, 71, 25))
        self.spb_k_count.setMinimum(5)
        self.spb_k_count.setMaximum(500)
        self.spb_k_count.setObjectName("spb_k_count")
        MainWindow.setCentralWidget(self.centralwidget)
        self.br_status = QtWidgets.QStatusBar(MainWindow)
        self.br_status.setObjectName("br_status")
        MainWindow.setStatusBar(self.br_status)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.btn_setFile.setText(QtWidgets.QApplication.translate("MainWindow", "Chsose file", None, -1))
        self.btn_start.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
        self.btn_stat.setText(QtWidgets.QApplication.translate("MainWindow", "Statistic", None, -1))
        self.chb_twice.setText(QtWidgets.QApplication.translate("MainWindow", "Twice dataset", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "K: ", None, -1))

