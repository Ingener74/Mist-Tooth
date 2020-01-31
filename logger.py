#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from loguru import logger

logger.add("debug.log", rotation="100 MB")
