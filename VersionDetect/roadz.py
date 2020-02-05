#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 - 2020 Tuhinshubhra

# Roadiz CMS version detection
# Rev 1

import cmseekdb.basic as cmseek
import re

def start(ga_content):
    ga_content = ga_content.lower()
    regex = re.findall(r'roadiz (.*?) -', ga_content)
    if regex != []:
        version = regex[0]
        cmseek.success('Roadiz CMS version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
        return version
    else:
        cmseek.error('Version detection failed!')
        return '0'
