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

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelTitle = QLabel(ItemWidget)
        self.labelTitle.setObjectName(u"labelTitle")

        self.verticalLayout_2.addWidget(self.labelTitle)

        self.labelInfo = QLabel(ItemWidget)
        self.labelInfo.setObjectName(u"labelInfo")

        self.verticalLayout_2.addWidget(self.labelInfo)

        self.progressBar = QProgressBar(ItemWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButtonStop = QPushButton(ItemWidget)
        self.pushButtonStop.setObjectName(u"pushButtonStop")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStop.sizePolicy().hasHeightForWidth())
        self.pushButtonStop.setSizePolicy(sizePolicy)
        self.pushButtonStop.setMinimumSize(QSize(60, 60))
        self.pushButtonStop.setMaximumSize(QSize(60, 60))
        self.pushButtonStop.setBaseSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/main/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonStop.setIcon(icon)
        self.pushButtonStop.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.pushButtonStop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(ItemWidget)

        QMetaObject.connectSlotsByName(ItemWidget)
    # setupUi

    def retranslateUi(self, ItemWidget):
        ItemWidget.setWindowTitle(QCoreApplication.translate("ItemWidget", u"Form", None))
        self.labelThumbnail.setText("")
        self.labelTitle.setText("")
        self.labelInfo.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonStop.setToolTip(QCoreApplication.translate("ItemWidget", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonStop.setText("")
    # retranslateUi

from resources_rc import *
