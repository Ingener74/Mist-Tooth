#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, QTimerEvent, Slot, Signal, QDir, QSysInfo
from PySide2.QtWidgets import QWidget, QListWidgetItem, QApplication, QMessageBox
from PySide2.QtGui import QKeyEvent, QDesktopServices

from Ui_MainWidget import Ui_MainWidget
from ItemWidget import ItemWidget
from settings import settings, DOWNLOAD_DIR
from logger import logger


class MainWidget(QWidget):
    start_download_signal = Signal(str)
    complete_download_signal = Signal(str)

    YOUTUBE_LINK_PATTERN = 'https://www.youtube.com/watch?v='

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        self.settings = settings()

        self.clipboard = QApplication.clipboard()

        self.clipboard_update_timer = self.startTimer(100)

    def closeEvent(self, event):
        self.settings.setValue('geom', self.saveGeometry())
        self.killTimer(self.clipboard_update_timer)

    def showEvent(self, event):
        if self.settings.contains('geom'):
            self.restoreGeometry(self.settings.value('geom'))

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()
        else:
            event.ignore()

    def timerEvent(self, event: QTimerEvent):
        if event.timerId() == self.clipboard_update_timer:
            text = self.clipboard.text()
            if text and self.add_download_from_text(text):
                self.clipboard.clear()

    def on_clipboard(self, mode):
        text_from_clipboard = self.clipboard.text()
        self.add_download_from_text(text_from_clipboard)
        self.clipboard.clear()

    def add_download_from_text(self, text: str):
        if not text:
            return False

        if not text.startswith(self.YOUTUBE_LINK_PATTERN):
            logger.debug("Text doesn't starts with youtube pattern")
            return False

        self.add_download(text)
        return True

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
