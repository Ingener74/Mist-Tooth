# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/MainWidget.ui',
# licensing of 'res/MainWidget.ui' applies.
#
# Created: Wed Jul 24 08:40:44 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(MainWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QtWidgets.QApplication.translate("MainWidget", "Mist Tooth", None, -1))

