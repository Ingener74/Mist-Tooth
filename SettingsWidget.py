#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, QDir, QFileInfo, QUrl
from PySide2.QtGui import QKeyEvent, QDesktopServices
from PySide2.QtWidgets import QWidget, QFileDialog
from loguru import logger

from Ui_SettingsWidget import Ui_SettingsWidget
from settings import settings, DOWNLOAD_DIR, VLC_PATH


class SettingsWidget(QWidget):
    SETTINGS_GEOMETRY = 'settings_geom'

    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)

        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)

        self.settings = settings()

        self.ui.pushButtonChangeDownloadDir.clicked.connect(self.change_dir_pressed)
        self.ui.pushButtonOpenSettingsDir.clicked.connect(self.open_settings_dir_pressed)
        self.ui.pushButtonChangeVlcPath.clicked.connect(self.change_vlc_path)

    def closeEvent(self, event):
        self.settings.setValue(self.SETTINGS_GEOMETRY, self.saveGeometry())
        self.settings.sync()

    def showEvent(self, event):
        if self.settings.contains(self.SETTINGS_GEOMETRY):
            self.restoreGeometry(self.settings.value(self.SETTINGS_GEOMETRY))

        if self.settings.contains(VLC_PATH):
            self.ui.labelVlcExePath.setText(self.settings.value(VLC_PATH))

        self.ui.labelDownloadDir.setText(
            self.settings.value(DOWNLOAD_DIR) if self.settings.contains(DOWNLOAD_DIR) else QDir.currentPath())

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.hide()
        else:
            event.ignore()

    def change_dir_pressed(self):
        download_dir = QFileDialog.getExistingDirectory(self, 'Укажите каталог для скачанных видео',
                                                        self.settings.value(DOWNLOAD_DIR) if self.settings.contains(
                                                            DOWNLOAD_DIR) else QDir.currentPath())
        if download_dir == '':
            return
        self.settings.setValue(DOWNLOAD_DIR, download_dir)
        self.settings.sync()
        self.ui.labelDownloadDir.setText(download_dir)

    def open_settings_dir_pressed(self):
        download_dir = QFileInfo(self.settings.fileName()).dir().absolutePath()
        download_dir = f'file:///{download_dir}'
        QDesktopServices.openUrl(QUrl(download_dir))

    def change_vlc_path(self):
        file, file_filter = QFileDialog.getOpenFileName(self, 'Укажите путь к испольняемому файлу VLC',
                                                        QDir.currentPath())
        logger.debug(file)
        if file == '':
            return
        self.settings.setValue(VLC_PATH, file)
        self.settings.sync()
        self.ui.labelVlcExePath.setText(file)
