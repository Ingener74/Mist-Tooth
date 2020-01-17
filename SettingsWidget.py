#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PySide2.QtCore import Qt, QTimerEvent, Slot, Signal, QDir, QFileInfo
from PySide2.QtWidgets import QWidget, QListWidgetItem, QApplication, QMessageBox, QFileDialog
from PySide2.QtGui import QKeyEvent, QDesktopServices
from loguru import logger

from Ui_SettingsWidget import Ui_SettingsWidget
from settings import settings, DOWNLOAD_DIR


class SettingsWidget(QWidget):

    SETTINGS_GEOMETRY = 'settings_geom'

    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)

        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)

        self.settings = settings()
        
        self.ui.pushButtonChangeDownloadDir.clicked.connect(self.change_dir_pressed)
        self.ui.pushButtonOpenSettingsDir.clicked.connect(self.open_settings_dir_pressed)

    def closeEvent(self, event):
        self.settings.setValue(self.SETTINGS_GEOMETRY, self.saveGeometry())
        self.settings.sync()

    def showEvent(self, event):
        if self.settings.contains(self.SETTINGS_GEOMETRY):
            self.restoreGeometry(self.settings.value(self.SETTINGS_GEOMETRY))

        self.ui.labelDownloadDir.setText(self.settings.value(DOWNLOAD_DIR) if self.settings.contains(DOWNLOAD_DIR) else QDir.currentPath())

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.hide()
        else:
            event.ignore()

    def change_dir_pressed(self):
        dir = QFileDialog.getExistingDirectory(
            self,
            'Укажите каталог для скачанных видео', 
            self.settings.value(DOWNLOAD_DIR) if self.settings.contains(DOWNLOAD_DIR) else QDir.currentPath())
        self.settings.setValue(DOWNLOAD_DIR, dir)
        self.settings.sync()
        self.ui.labelDownloadDir.setText(dir)

    def open_settings_dir_pressed(self):
        QDesktopServices.openUrl(QFileInfo(self.settings.fileName()).dir().absolutePath())
