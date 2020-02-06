#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QShowEvent, QPixmap
from PySide2.QtCore import QTimerEvent, Qt, QRect, QPoint

from Ui_NotificationWidget import Ui_NotificationWidget

from loguru import logger

class NotificationWidget(QWidget):
    def __init__(self, parent=None):
        super(NotificationWidget, self).__init__(parent, Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        self.ui = Ui_NotificationWidget()
        self.ui.setupUi(self)

        self.ui.labelThumbnail.setText('')
        self.ui.labelIcon.setText('')
        self.ui.labelTitle.setText('')

        self.hide_timer = None

        self.__move_to: QRect = None

    def showEvent(self, event: QShowEvent):
        self.hide_timer = self.startTimer(3000)
        if self.__move_to:
            p = self.__move_to.center() - QPoint(self.width() / 2, self.height() + 24)
            self.move(p)

    def timerEvent(self, event: QTimerEvent):
        if self.hide_timer is not None and event.timerId() == self.hide_timer:
            self.hide()
            self.killTimer(self.hide_timer)

    def show_(self, *, title: str = '', thumbnail: QPixmap = None, move_to: QRect = None):
        self.ui.labelTitle.setText(title)
        if thumbnail:
            self.ui.labelThumbnail.setPixmap(thumbnail)
        if move_to:
            self.__move_to = move_to
        self.show()
        self.activateWindow()

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

    @property
    def move_to(self):
        return self.__move_to

    @move_to.setter
    def move_to(self, move_to):
        self.__move_to = move_to
