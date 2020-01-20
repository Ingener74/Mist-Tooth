#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import run
run(["pyinstaller.exe", 
    '-F', 
    '-n', 'Youtube Download', 
    '-i', 'res/icon.ico', 
    '-w', 
    '--log-level', 'INFO', 
    'MistTooth.py'])
