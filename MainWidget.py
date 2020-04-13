#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, QTimerEvent, Signal
from PySide2.QtGui import QKeyEvent, QPixmap, QDropEvent, QDragEnterEvent
from PySide2.QtWidgets import QWidget, QListWidgetItem, QApplication

from ItemWidget import ItemWidget
from Ui_MainWidget import Ui_MainWidget
from settings import settings


class MainWidget(QWidget):
    start_download_signal = Signal(str)
    complete_download_signal = Signal(str, QPixmap)

    LINK_PATTERNS = ['https://www.youtube.com/watch?v=', 'https://youtu.be/']

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        self.settings = settings()

        self.clipboard = QApplication.clipboard()

        self.clipboard_update_timer = self.startTimer(100)

        self.setAcceptDrops(True)

    def closeEvent(self, event):
        self.settings.setValue('geom', self.saveGeometry())

    def on_close(self):
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

    def dragEnterEvent(self, event: QDragEnterEvent):
        event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            self.add_download_from_text(event.mimeData().text())

    def on_clipboard(self, mode):
        text_from_clipboard = self.clipboard.text()
        self.add_download_from_text(text_from_clipboard)
        self.clipboard.clear()

    def add_download_from_text(self, text: str):
        if not text:
            return False

        for pattern in self.LINK_PATTERNS:
            if text.startswith(pattern):
                break
        else:
            return False        

        self.add_download(text)
        return True

    def complete(self, item: QListWidgetItem, thumbnail: QPixmap):
        widget: ItemWidget = self.ui.listWidget.itemWidget(item)
        self.complete_download_signal.emit(widget.ui.labelTitle.text(), thumbnail)
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
