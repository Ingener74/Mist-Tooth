#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
from datetime import datetime
from time import strftime

import requests
from PySide2.QtCore import Qt, QThread, Signal, Slot
from PySide2.QtWidgets import QListWidgetItem, QMessageBox, QWidget
from pytube import YouTube

from Ui_ItemWidget import Ui_ItemWidget


class YouTubeDownloader(QThread):
    progress_signal = Signal(int)
    complete_signal = Signal()
    title_signal = Signal(str)
    error_signal = Signal(str)

    def __init__(self, parent=None):
        super(YouTubeDownloader, self).__init__(parent)
        self.link: str = ''
        self.youtube = None

    def run(self):
        if self.link == '':
            self.error_signal.emit('Bad link')
            return
        try:
            self.title_signal.emit(self.link)
            self.progress_signal.emit(0)
            self.youtube = YouTube(url=self.link, 
                on_progress_callback=self.progress_callback,
                on_complete_callback=self.complete_callback)

            no_title = False
            try:
                self.title_signal.emit(self.youtube.title)
                
            except KeyError as e:
                print('Title error: ' + str(e))
                no_title = True

            stream = self.youtube.streams.filter(subtype='mp4').first()
            if no_title:
                now = datetime.now()
                fn = now.strftime('%H_%M_%S_%d_%m_%Y')
                stream.download(filename=fn)
            else:
                stream.download()
        except Exception as e:
            print('Exception: ' + str(e))
            print(traceback.print_exc())
            self.error_signal.emit(str(e))

    def progress_callback(self, stream, chunk, file_handle, bytes_remaining):
        a = stream.filesize - bytes_remaining
        b = a / stream.filesize
        c = b * 100
        self.progress_signal.emit(int(c))

    def complete_callback(self, stream, file_handle):
        self.complete_signal.emit()

    @Slot()
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
        self.youtube.error_signal.connect(self.error, Qt.QueuedConnection)
        self.youtube.complete_signal.connect(self.complete, Qt.QueuedConnection)

        self.item = item

    def start_download(self, link: str):
        self.youtube.start_download(link)
        self.youtube.start()

    def set_title(self, name: str):
        self.ui.labelTitle.setText(name)

    def set_progress(self, progress: int):
        self.ui.progressBar.setValue(progress)

    @Slot()
    def error(self, message: str):
        QMessageBox.critical(self, 'Error', message)
        self.on_complete_signal.emit(self.item)

    @Slot()
    def complete(self):
        self.on_complete_signal.emit(self.item)
