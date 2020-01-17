#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtCore import QSettings, QDir

DOWNLOAD_DIR = 'download_dir'
VLC_PATH = 'vlc_path'

def settings():
    s = QSettings(QSettings.IniFormat, QSettings.UserScope, 'ShnaiderPavel', 'MistTooth')
    if not s.contains(DOWNLOAD_DIR):
        s.setValue(DOWNLOAD_DIR, QDir.currentPath().absolutePath())
    return s
