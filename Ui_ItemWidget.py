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
        ItemWidget.resize(182, 121)
        ItemWidget.setMaximumSize(QSize(16777215, 121))
        self.horizontalLayout_2 = QHBoxLayout(ItemWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelThumbnail = QLabel(ItemWidget)
        self.labelThumbnail.setObjectName(u"labelThumbnail")
        self.labelThumbnail.setMaximumSize(QSize(16777215, 100))
        self.labelThumbnail.setPixmap(QPixmap(u":/main/loading.png"))

        self.horizontalLayout_2.addWidget(self.labelThumbnail)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelTitle = QLabel(ItemWidget)
        self.labelTitle.setObjectName(u"labelTitle")

        self.verticalLayout_2.addWidget(self.labelTitle)

        self.labelInfo = QLabel(ItemWidget)
        self.labelInfo.setObjectName(u"labelInfo")

        self.verticalLayout_2.addWidget(self.labelInfo)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonStop = QPushButton(ItemWidget)
        self.pushButtonStop.setObjectName(u"pushButtonStop")
        icon = QIcon()
        icon.addFile(u":/main/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonStop.setIcon(icon)
        self.pushButtonStop.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.pushButtonStop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(ItemWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.retranslateUi(ItemWidget)

        QMetaObject.connectSlotsByName(ItemWidget)
    # setupUi

    def retranslateUi(self, ItemWidget):
        ItemWidget.setWindowTitle(QCoreApplication.translate("ItemWidget", u"Form", None))
        self.labelThumbnail.setText(QCoreApplication.translate("ItemWidget", u"Thumbnail", None))
        self.labelTitle.setText(QCoreApplication.translate("ItemWidget", u"Title", None))
        self.labelInfo.setText(QCoreApplication.translate("ItemWidget", u"Info", None))
#if QT_CONFIG(tooltip)
        self.pushButtonStop.setToolTip(QCoreApplication.translate("ItemWidget", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonStop.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonStop.setShortcut(QCoreApplication.translate("ItemWidget", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

from resources_rc import *
