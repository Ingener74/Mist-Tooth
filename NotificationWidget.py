#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtGui import QShowEvent, QPixmap, QPainterPath, QRegion, QScreen
from PySide2.QtCore import QTimerEvent, Qt, QRect, QPoint, QRectF

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

    def showEvent(self, event: QShowEvent):
        pass

    def resizeEvent(self, event):
        radius = 8
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), radius, radius)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

    def timerEvent(self, event: QTimerEvent):
        if self.hide_timer is not None and event.timerId() == self.hide_timer:
            self.hide()
            self.killTimer(self.hide_timer)

    def show_(self, *, title: str = '', thumbnail: QPixmap = None, move_to: QRect = None, app: QApplication = None):
        self.ui.labelTitle.setText(title)
        if thumbnail:
            self.ui.labelThumbnail.setPixmap(thumbnail)
        else:
            self.ui.labelThumbnail.clear()
        if move_to and app:
            for screen in app.screens():
                if screen.geometry().contains(move_to):
                    break
            if move_to.center().y() > screen.geometry().height() / 2:
                p = move_to.center() - QPoint(self.width() / 2, self.height() + 24)
            else:
                p = move_to.center() + QPoint(- self.width() / 2, 24)
            # p = move_to.center() - QPoint(self.width() / 2, self.height() + 24)
            self.move(p)
        self.hide_timer = self.startTimer(3000)
        self.show()
        self.activateWindow()
