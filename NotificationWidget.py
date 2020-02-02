#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QWidget

from Ui_NotificationWidget import Ui_NotificationWidget

class NotificationWidget(QWidget):
    def __init__(self, parent=None):
        super(NotificationWidget, self).__init__(parent)

        self.ui = Ui_NotificationWidget()
        self.ui.setupUi(self)
