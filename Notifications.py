#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2.QtCore import (
    QObject, 
    QSysInfo)
from PySide2.QtWidgets import QSystemTrayIcon
from logger import logger
import subprocess as sp
from io import StringIO

class Notification(QObject):
    def __init__(self, parent=None):
        super(Notification, self).__init__(parent)

        self.system_tray = parent

    def show_notification(self, title, text):
        logger.debug(title)
        logger.debug(text)
        logger.debug(QSysInfo.kernelType())
        logger.debug(QSysInfo.kernelVersion())

        if QSysInfo.kernelType() == 'darwin':
            proc = sp.Popen('osascript', stdin=sp.PIPE)
            proc.communicate(input=f'display notification \"{text}\" with title \"{title}\"'.encode())
        elif QSysInfo.kernelType() == 'winnt':
            if QSysInfo.kernelVersion().startswith('10'):
                version = QSysInfo.kernelVersion().split('.')
                if int(version[2] > 17763):
                    logger.error(f'Notification system not implemented for {QSysInfo.kernelType()}, {QSysInfo.kernelVersion()}')
                else:
                    self.system_tray.showMessage(title, text)
            else:
                logger.error(f'Notification system not implemented for {QSysInfo.kernelType()}, {QSysInfo.kernelVersion()}')
        else:
            logger.error(f'Notification system not implemented for {QSysInfo.kernelType()}, {QSysInfo.kernelVersion()}')
