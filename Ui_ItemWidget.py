# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ItemWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_ItemWidget(object):
    def setupUi(self, ItemWidget):
        if ItemWidget.objectName():
            ItemWidget.setObjectName(u"ItemWidget")
        ItemWidget.resize(505, 163)
        self.horizontalLayout = QHBoxLayout(ItemWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelThumbnail = QLabel(ItemWidget)
        self.labelThumbnail.setObjectName(u"labelThumbnail")

        self.horizontalLayout.addWidget(self.labelThumbnail)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(ItemWidget)
        self.labelTitle.setObjectName(u"labelTitle")

        self.verticalLayout.addWidget(self.labelTitle)

        self.labelInfo = QLabel(ItemWidget)
        self.labelInfo.setObjectName(u"labelInfo")

        self.verticalLayout.addWidget(self.labelInfo)

        self.progressBar = QProgressBar(ItemWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(ItemWidget)

        QMetaObject.connectSlotsByName(ItemWidget)
    # setupUi

    def retranslateUi(self, ItemWidget):
        ItemWidget.setWindowTitle(QCoreApplication.translate("ItemWidget", u"Form", None))
        self.labelThumbnail.setText("")
        self.labelTitle.setText("")
        self.labelInfo.setText("")
    # retranslateUi

from resources_rc import *
