#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtCore import QSettings

def settings():
    return QSettings(QSettings.IniFormat, QSettings.UserScope, 'ShnaiderPavel', 'MistTooth')
