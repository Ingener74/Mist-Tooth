#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import run
from sys import platform
run(["pyinstaller.exe" if platform == 'win32' else 'pyinstaller',
    '-F',
    '-n', 'Youtube Download',
    '-i', 'res/icon.ico' if platform == 'win32' else 'res/icon.icns',
    '-w',
    '--log-level', 'INFO',
    'MistTooth.py'])
