#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import run

run('pyside2-rcc res/resources.qrc -o resources_rc.py'.split())
run('pyside2-uic res/MainWidget.ui -o Ui_MainWidget.py'.split())
run('pyside2-uic res/SettingsWidget.ui -o Ui_SettingsWidget.py'.split())
run('pyside2-uic res/ItemWidget.ui -o Ui_ItemWidget.py'.split())
run('pyside2-uic res/NotificationWidget.ui -o Ui_NotificationWidget.py'.split())


def append_import_resources(filename):
    with open(filename, 'a') as f:
        f.write('from resources_rc import *\n')


append_import_resources('Ui_MainWidget.py')
append_import_resources('Ui_SettingsWidget.py')
append_import_resources('Ui_ItemWidget.py')
append_import_resources('Ui_NotificationWidget.py')
