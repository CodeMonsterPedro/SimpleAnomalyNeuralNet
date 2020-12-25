# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Fri Dec 25 14:09:57 2020
#      by: pyside2-uic  running on PySide2 5.13.2
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
        self.tbw_data.setGeometry(QtCore.QRect(10, 10, 1031, 571))
        self.tbw_data.setObjectName("tbw_data")
        self.tbw_data.setColumnCount(0)
        self.tbw_data.setRowCount(0)
        self.cb_method = QtWidgets.QComboBox(self.centralwidget)
        self.cb_method.setGeometry(QtCore.QRect(220, 610, 381, 31))
        self.cb_method.setObjectName("cb_method")
        self.btn_setFile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setFile.setGeometry(QtCore.QRect(80, 610, 121, 31))
        self.btn_setFile.setObjectName("btn_setFile")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(500, 770, 101, 31))
        self.btn_start.setObjectName("btn_start")
        self.btn_stat = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stat.setGeometry(QtCore.QRect(500, 710, 101, 31))
        self.btn_stat.setObjectName("btn_stat")
        self.cb_metric = QtWidgets.QComboBox(self.centralwidget)
        self.cb_metric.setGeometry(QtCore.QRect(220, 660, 381, 31))
        self.cb_metric.setObjectName("cb_metric")
        self.cb_target = QtWidgets.QComboBox(self.centralwidget)
        self.cb_target.setGeometry(QtCore.QRect(660, 610, 361, 31))
        self.cb_target.setObjectName("cb_target")
        self.btn_setNeuralnet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setNeuralnet.setGeometry(QtCore.QRect(80, 660, 121, 31))
        self.btn_setNeuralnet.setObjectName("btn_setNeuralnet")
        self.tbw_net_tree = QtWidgets.QTableWidget(self.centralwidget)
        self.tbw_net_tree.setGeometry(QtCore.QRect(1060, 10, 251, 571))
        self.tbw_net_tree.setObjectName("tbw_net_tree")
        self.tbw_net_tree.setColumnCount(0)
        self.tbw_net_tree.setRowCount(0)
        self.btn_addlayout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addlayout.setGeometry(QtCore.QRect(1030, 610, 111, 31))
        self.btn_addlayout.setObjectName("btn_addlayout")
        self.btn_dellayout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dellayout.setGeometry(QtCore.QRect(1030, 660, 111, 31))
        self.btn_dellayout.setObjectName("btn_dellayout")
        self.ln_id = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_id.setGeometry(QtCore.QRect(1150, 660, 151, 31))
        self.ln_id.setObjectName("ln_id")
        self.spb_neirons = QtWidgets.QSpinBox(self.centralwidget)
        self.spb_neirons.setGeometry(QtCore.QRect(1150, 610, 151, 31))
        self.spb_neirons.setMinimum(1)
        self.spb_neirons.setMaximum(99999)
        self.spb_neirons.setObjectName("spb_neirons")
        self.btn_build = QtWidgets.QPushButton(self.centralwidget)
        self.btn_build.setGeometry(QtCore.QRect(80, 770, 121, 31))
        self.btn_build.setObjectName("btn_build")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.btn_setFile.setText(QtWidgets.QApplication.translate("MainWindow", "Файл данных", None, -1))
        self.btn_start.setText(QtWidgets.QApplication.translate("MainWindow", "Начать", None, -1))
        self.btn_stat.setText(QtWidgets.QApplication.translate("MainWindow", "Статистика", None, -1))
        self.btn_setNeuralnet.setText(QtWidgets.QApplication.translate("MainWindow", "Файл нейросети", None, -1))
        self.btn_addlayout.setText(QtWidgets.QApplication.translate("MainWindow", "Добавть слой", None, -1))
        self.btn_dellayout.setText(QtWidgets.QApplication.translate("MainWindow", "Убрать слой", None, -1))
        self.btn_build.setText(QtWidgets.QApplication.translate("MainWindow", "Собрать сеть", None, -1))

