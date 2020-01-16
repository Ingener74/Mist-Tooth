# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ItemWidget.ui',
# licensing of 'res/ItemWidget.ui' applies.
#
# Created: Wed Jul 24 14:22:57 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ItemWidget(object):
    def setupUi(self, ItemWidget):
        ItemWidget.setObjectName("ItemWidget")
        ItemWidget.resize(200, 100)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ItemWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelThumbnail = QtWidgets.QLabel(ItemWidget)
        self.labelThumbnail.setText("")
        self.labelThumbnail.setObjectName("labelThumbnail")
        self.horizontalLayout.addWidget(self.labelThumbnail)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(ItemWidget)
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.progressBar = QtWidgets.QProgressBar(ItemWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ItemWidget)
        QtCore.QMetaObject.connectSlotsByName(ItemWidget)

    def retranslateUi(self, ItemWidget):
        ItemWidget.setWindowTitle(QtWidgets.QApplication.translate("ItemWidget", "Form", None, -1))

