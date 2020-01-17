#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, QTimerEvent, Slot, Signal, QDir
from PySide2.QtWidgets import QWidget, QListWidgetItem, QApplication, QMessageBox
from PySide2.QtGui import QKeyEvent, QDesktopServices

from Ui_MainWidget import Ui_MainWidget
from ItemWidget import ItemWidget
from settings import settings, DOWNLOAD_DIR


class MainWidget(QWidget):
    start_download_signal = Signal(str)
    complete_download_signal = Signal(str)

    YOUTUBE_LINK_PATTERN = 'https://www.youtube.com/watch?v='

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        self.settings = settings()

        clipboard = QApplication.clipboard()
        clipboard.changed.connect(self.on_clipboard)

    def closeEvent(self, event):
        self.settings.setValue('geom', self.saveGeometry())

    def showEvent(self, event):
        if self.settings.contains('geom'):
            self.restoreGeometry(self.settings.value('geom'))

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

    def complete(self, item: QListWidgetItem):
        widget: ItemWidget = self.ui.listWidget.itemWidget(item)
        self.complete_download_signal.emit(widget.ui.labelTitle.text())
        self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def add_download(self, link: str):
        list_item = QListWidgetItem()
        self.ui.listWidget.addItem(list_item)
        download_item = ItemWidget(list_item)
        download_item.on_complete_signal.connect(self.complete)
        list_item.setSizeHint(download_item.sizeHint())
        self.ui.listWidget.setItemWidget(list_item, download_item)
        download_item.start_download(link)
        self.start_download_signal.emit(link)
