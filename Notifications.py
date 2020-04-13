#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess as sp

from PySide2.QtCore import (QObject, QSysInfo)

from logger import logger


def icon_in_res(filename):
    return os.path.normpath(os.path.abspath(os.path.join(os.path.dirname(__file__), 'res', filename)))


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
                version_patch = int(version[2])
                if version_patch > 17763:
                    logger.error(
                        f'Notification system not implemented for {QSysInfo.kernelType()}, {QSysInfo.kernelVersion()}')
                # elif version_patch < 18363:
                #     from win10toast import ToastNotifier
                #     toaster = ToastNotifier()
                #     toaster.show_toast(title, text, icon_in_res('icon.ico'))
                else:
                    self.system_tray.showMessage(title, text)
            else:
                logger.error(
                    f'Notification system not implemented for {QSysInfo.kernelType()}, {QSysInfo.kernelVersion()}')
        else:
            logger.error(f'Notification system not implemented for {QSysInfo.kernelType()}, {QSysInfo.kernelVersion()}')
