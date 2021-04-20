#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 4/21/21-14:22
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : superior_god
# @File     : os_detector.py
# @Project  : 00PythonProjects
from platform import system


def detect_os(bypass=False):
    """Check OS, as multiprocessing may not work properly in Windows and macOS"""
    if bypass is True:
        return

    os_name = system()

    if os_name in ['Windows']:
        print("It seems that you are running this code from {}, in which the Python multiprocessing may not work properly. Consider running this code in Linux.".format(os_name))
        print("Exiting..")
        exit()
    else:
        print("Linux is fine! Python multiprocessing works.")
