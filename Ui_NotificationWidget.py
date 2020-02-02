# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NotificationWidget.ui'
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

class Ui_NotificationWidget(object):
    def setupUi(self, NotificationWidget):
        if NotificationWidget.objectName():
            NotificationWidget.setObjectName(u"NotificationWidget")
        NotificationWidget.resize(315, 121)
        self.horizontalLayout_2 = QHBoxLayout(NotificationWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelThumbnail = QLabel(NotificationWidget)
        self.labelThumbnail.setObjectName(u"labelThumbnail")
        self.labelThumbnail.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_2.addWidget(self.labelThumbnail)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelTitle = QLabel(NotificationWidget)
        self.labelTitle.setObjectName(u"labelTitle")

        self.horizontalLayout.addWidget(self.labelTitle)

        self.labelIcon = QLabel(NotificationWidget)
        self.labelIcon.setObjectName(u"labelIcon")

        self.horizontalLayout.addWidget(self.labelIcon)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(1, 1)

        self.retranslateUi(NotificationWidget)

        QMetaObject.connectSlotsByName(NotificationWidget)
    # setupUi

    def retranslateUi(self, NotificationWidget):
        NotificationWidget.setWindowTitle(QCoreApplication.translate("NotificationWidget", u"Form", None))
        self.labelThumbnail.setText(QCoreApplication.translate("NotificationWidget", u"Thumbnail", None))
        self.labelTitle.setText(QCoreApplication.translate("NotificationWidget", u"Title", None))
        self.labelIcon.setText(QCoreApplication.translate("NotificationWidget", u"Icon", None))
    # retranslateUi

from resources_rc import *
