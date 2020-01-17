# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsWidget.ui'
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

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(449, 183)
        icon = QIcon()
        icon.addFile(u":/main/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        SettingsWidget.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(SettingsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(SettingsWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelDownloadDir = QLabel(self.groupBox)
        self.labelDownloadDir.setObjectName(u"labelDownloadDir")

        self.horizontalLayout.addWidget(self.labelDownloadDir)

        self.pushButtonChangeDownloadDir = QPushButton(self.groupBox)
        self.pushButtonChangeDownloadDir.setObjectName(u"pushButtonChangeDownloadDir")

        self.horizontalLayout.addWidget(self.pushButtonChangeDownloadDir)

        self.pushButtonOpenDownloadDir = QPushButton(self.groupBox)
        self.pushButtonOpenDownloadDir.setObjectName(u"pushButtonOpenDownloadDir")
        icon1 = QIcon()
        icon1.addFile(u":/main/open_dir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenDownloadDir.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButtonOpenDownloadDir)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(SettingsWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelVlcExePath = QLabel(self.groupBox_2)
        self.labelVlcExePath.setObjectName(u"labelVlcExePath")

        self.horizontalLayout_2.addWidget(self.labelVlcExePath)

        self.pushButtonChangeVlcPath = QPushButton(self.groupBox_2)
        self.pushButtonChangeVlcPath.setObjectName(u"pushButtonChangeVlcPath")
        icon2 = QIcon()
        icon2.addFile(u":/main/vlc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonChangeVlcPath.setIcon(icon2)
        self.pushButtonChangeVlcPath.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButtonChangeVlcPath)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.pushButtonOpenSettingsDir = QPushButton(SettingsWidget)
        self.pushButtonOpenSettingsDir.setObjectName(u"pushButtonOpenSettingsDir")

        self.verticalLayout.addWidget(self.pushButtonOpenSettingsDir)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsWidget", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0441\u043a\u0430\u0447\u0430\u043d\u043d\u044b\u0445 \u0432\u0438\u0434\u0435\u043e", None))
        self.labelDownloadDir.setText("")
        self.pushButtonChangeDownloadDir.setText(QCoreApplication.translate("SettingsWidget", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0440\u0443\u0433\u043e\u0439", None))
#if QT_CONFIG(tooltip)
        self.pushButtonOpenDownloadDir.setToolTip(QCoreApplication.translate("SettingsWidget", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043a\u0430\u0442\u0430\u043b\u043e\u0433 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonOpenDownloadDir.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsWidget", u"\u041f\u0443\u0442\u044c \u043a \u0438\u0441\u043f\u043e\u043b\u043d\u044f\u0435\u043c\u043e\u043c\u0443 \u0444\u0430\u0439\u043b\u0443 VLC", None))
        self.labelVlcExePath.setText(QCoreApplication.translate("SettingsWidget", u"<html><head/><body><p>\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0433\u0434\u0435 \u043b\u0435\u0436\u0438\u0442 \u0444\u0430\u0439\u043b\u0430 -&gt;</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButtonChangeVlcPath.setToolTip(QCoreApplication.translate("SettingsWidget", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u0438\u0441\u043f\u043e\u043b\u043d\u044f\u0435\u043c\u044b\u0439 \u0444\u0430\u0439\u043b VLC", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonChangeVlcPath.setText("")
        self.pushButtonOpenSettingsDir.setText(QCoreApplication.translate("SettingsWidget", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043a\u0430\u0442\u0430\u043b\u043e\u0433 \u0433\u0434\u0435 \u043b\u0435\u0436\u0438\u0442 \u0444\u0430\u0439\u043b \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a", None))
    # retranslateUi

from resources_rc import *
