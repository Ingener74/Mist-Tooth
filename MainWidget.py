#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, QTimerEvent, Slot, Signal
from PySide2.QtWidgets import QWidget, QListWidgetItem, QApplication, QMessageBox
from PySide2.QtGui import QKeyEvent

from Ui_MainWidget import Ui_MainWidget
from ItemWidget import ItemWidget

class MainWidget(QWidget):
    YOUTUBE_LINK_PATTERN = 'https://www.youtube.com/watch?v='

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        clipboard = QApplication.clipboard()
        clipboard.changed.connect(self.on_clipboard)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()
        else:
            event.ignore()

    def on_clipboard(self, mode):
        clipboard = self.sender()
        text_from_clipboard = clipboard.text()

        if text_from_clipboard == '':
            return

        if not text_from_clipboard.startswith(self.YOUTUBE_LINK_PATTERN):
            return

        self.add_download(text_from_clipboard)
        clipboard.clear()

    @Slot()
    def complete(self, item: QListWidgetItem):
        row = self.ui.listWidget.row(item)
        print(row)
        self.ui.listWidget.takeItem(row)

    def add_download(self, link: str):
        list_item = QListWidgetItem()
        self.ui.listWidget.addItem(list_item)
        download_item = ItemWidget(list_item)
        # download_item.on_complete_signal.connect(self.complete)
        list_item.setSizeHint(download_item.sizeHint())
        self.ui.listWidget.setItemWidget(list_item, download_item)
        download_item.start_download(link)
