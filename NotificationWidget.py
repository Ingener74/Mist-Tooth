#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QShowEvent, QPixmap
from PySide2.QtCore import QTimerEvent, Qt

from Ui_NotificationWidget import Ui_NotificationWidget

class NotificationWidget(QWidget):
    def __init__(self, parent=None):
        super(NotificationWidget, self).__init__(parent, Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        self.ui = Ui_NotificationWidget()
        self.ui.setupUi(self)

        self.ui.labelThumbnail.setText('')
        self.ui.labelIcon.setText('')
        self.ui.labelTitle.setText('')

        self.hide_timer = None

    def showEvent(self, event: QShowEvent):
        self.hide_timer = self.startTimer(2000)

    def timerEvent(self, event: QTimerEvent):
        if self.hide_timer is not None and event.timerId() == self.hide_timer:
            self.hide()
            self.killTimer(self.hide_timer)

    @property
    def title(self):
        return self.ui.labelTitle.text()

    @title.setter
    def title(self, title: str):
        self.ui.labelTitle.setText(title)

    @property
    def thumbnail(self):
        return self.ui.labelThumbnail.pixmap()

    @thumbnail.setter
    def thumbnail(self, thumbnail: QPixmap):
        self.ui.labelThumbnail.setPixmap(thumbnail)
