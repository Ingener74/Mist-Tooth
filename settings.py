#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtCore import QSettings, QDir

APPLICATION_NAME = 'MistTooth'
COMPANY = 'ShnaiderPavel'

DOWNLOAD_DIR = 'download_dir'
VLC_PATH = 'vlc_path'


def settings():
    s = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPLICATION_NAME)
    if not s.contains(DOWNLOAD_DIR):
        s.setValue(DOWNLOAD_DIR, QDir.currentPath())
    return s
