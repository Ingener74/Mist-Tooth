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
        SettingsWidget.resize(251, 309)
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

        self.pushButtonOpenSettingsDir = QPushButton(SettingsWidget)
        self.pushButtonOpenSettingsDir.setObjectName(u"pushButtonOpenSettingsDir")

        self.verticalLayout.addWidget(self.pushButtonOpenSettingsDir)

        self.verticalSpacer = QSpacerItem(20, 196, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsWidget", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0441\u043a\u0430\u0447\u0430\u043d\u043d\u044b\u0445 \u0432\u0438\u0434\u0435\u043e", None))
        self.labelDownloadDir.setText(QCoreApplication.translate("SettingsWidget", u"TextLabel", None))
        self.pushButtonChangeDownloadDir.setText(QCoreApplication.translate("SettingsWidget", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0440\u0443\u0433\u043e\u0439", None))
#if QT_CONFIG(tooltip)
        self.pushButtonOpenDownloadDir.setToolTip(QCoreApplication.translate("SettingsWidget", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043a\u0430\u0442\u0430\u043b\u043e\u0433 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonOpenDownloadDir.setText("")
        self.pushButtonOpenSettingsDir.setText(QCoreApplication.translate("SettingsWidget", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043a\u0430\u0442\u0430\u043b\u043e\u0433 \u0433\u0434\u0435 \u043b\u0435\u0436\u0438\u0442 \u0444\u0430\u0439\u043b \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a", None))
    # retranslateUi

from resources_rc import *
