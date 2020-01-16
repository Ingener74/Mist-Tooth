# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWidget.ui'
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

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/main/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWidget.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(MainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(MainWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Youtube \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u0442\u0435\u043b\u044c", None))
    # retranslateUi

from resources_rc import *