# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statDialog.ui',
# licensing of 'statDialog.ui' applies.
#
# Created: Sat May 23 15:04:16 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1084, 878)
        self.tbw_stat = QtWidgets.QTableWidget(Dialog)
        self.tbw_stat.setGeometry(QtCore.QRect(10, 10, 1061, 341))
        self.tbw_stat.setObjectName("tbw_stat")
        self.tbw_stat.setColumnCount(0)
        self.tbw_stat.setRowCount(0)
        self.tbw_data = QtWidgets.QTableWidget(Dialog)
        self.tbw_data.setGeometry(QtCore.QRect(10, 360, 1061, 511))
        self.tbw_data.setObjectName("tbw_data")
        self.tbw_data.setColumnCount(0)
        self.tbw_data.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))

