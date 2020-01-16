#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
import re
from datetime import datetime
from time import strftime

# import requests
import youtube_dl
from PySide2.QtCore import Qt, QThread, Signal, Slot
from PySide2.QtWidgets import QListWidgetItem, QMessageBox, QWidget
from PySide2.QtGui import QPixmap
from loguru import logger

from Ui_ItemWidget import Ui_ItemWidget

class YouTubeDownloader(QThread):
    progress_signal = Signal(int)
    complete_signal = Signal()
    title_signal = Signal(str)
    error_signal = Signal(str)
    thumbnail_filename_signal = Signal(str)
    info_signal = Signal(str)

    def __init__(self, parent=None):
        super(YouTubeDownloader, self).__init__(parent)
        self.link: str = ''

        self.title: str = ''

    def run(self):
        if self.link == '':
            self.error_signal.emit('Bad link')
            return
        try:
            self.title_signal.emit(self.link)
            self.progress_signal.emit(0)

            class Logger(object):
                def __init__(self, outer):
                    self.__outer = outer
                
                def info(self, msg):
                    pass

                def debug(self, msg):
                    a = 'Writing thumbnail to'
                    if a in msg:
                        thumbnail_filename = msg[msg.find(a) + len(a) + 2:]
                        self.__outer.thumbnail(thumbnail_filename)

                def warning(self, msg):
                    pass

                def error(self, msg):
                    logger.error(msg)

            ydl_opts = {
                'writethumbnail': True,
                'logger': Logger(self),
                'progress_hooks': [self.hooks]
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.link])

        except Exception as e:
            print('Exception: ' + str(e))
            print(traceback.print_exc())
            self.error_signal.emit(str(e))

    def hooks(self, data):
        # logger.info(data)
        if 'filename' in data:
            if data['filename'] != self.title:
                self.title = data['filename']
                self.title_signal.emit(self.title)

        if 'status' in data:
            if data['status'] == 'downloading':
                if 'downloaded_bytes' in data and 'total_bytes' in data:
                    progress = data['downloaded_bytes'] / data['total_bytes']
                    progress_in_percent = progress * 100
                    self.progress_signal.emit(int(progress_in_percent))
                if '_eta_str' in data and '_speed_str' in data and '_total_bytes_str' in data:
                    self.info_signal.emit(
                        'Времени осталось: ' + data['_eta_str'] + ', Скорость: ' + data['_speed_str'] + ', Полный размер: ' + data['_total_bytes_str']
                    )
            if data['status'] == 'finished':
                self.complete_signal.emit()

    def thumbnail(self, filename):
        self.thumbnail_filename_signal.emit(filename)

    def start_download(self, link: str):
        self.link = link

class ItemWidget(QWidget):
    on_complete_signal = Signal(QListWidgetItem)

    def __init__(self, item, parent=None):
        super(ItemWidget, self).__init__(parent)

        self.ui = Ui_ItemWidget()
        self.ui.setupUi(self)

        self.youtube = YouTubeDownloader()
        self.youtube.progress_signal.connect(self.set_progress, Qt.QueuedConnection)
        self.youtube.title_signal.connect(self.set_title, Qt.QueuedConnection)
        self.youtube.info_signal.connect(self.set_info, Qt.QueuedConnection)
        # self.youtube.error_signal.connect(self.error, Qt.QueuedConnection)
        self.youtube.complete_signal.connect(self.complete, Qt.QueuedConnection)
        self.youtube.thumbnail_filename_signal.connect(self.set_thumbnail, Qt.QueuedConnection)

        self.item = item

    def start_download(self, link: str):
        self.youtube.start_download(link)
        self.youtube.start()

    def set_title(self, name: str):
        self.ui.labelTitle.setText(name)

    def set_info(self, info: str):
        self.ui.labelInfo.setText(info)

    def set_thumbnail(self, filename: str):
        pixmap: QPixmap = QPixmap(filename)
        pixmap = pixmap.scaledToHeight(self.rect().height())
        self.ui.labelThumbnail.setPixmap(pixmap)

    def set_progress(self, progress: int):
        self.ui.progressBar.setValue(progress)

    def error(self, message: str):
        QMessageBox.critical(self, 'Error', message)
        self.on_complete_signal.emit(self.item)

    def complete(self):
        self.on_complete_signal.emit(self.item)
