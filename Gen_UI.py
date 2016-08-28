#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\QtSDK\QtCreator\bin\Generator.ui'
#
# Created: Sun Mar 08 17:19:29 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(397, 156)
        self.genButton = QtGui.QPushButton(Dialog)
        self.genButton.setGeometry(QtCore.QRect(120, 10, 166, 23))
        self.genButton.setObjectName("genButton")
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 38, 371, 101))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Opertional Name Generator", "Opertional Name Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.genButton.setText(QtGui.QApplication.translate("Opertional Name Generator", "Generate New Operational Name", None, QtGui.QApplication.UnicodeUTF8))

