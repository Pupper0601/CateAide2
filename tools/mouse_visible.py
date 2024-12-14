#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import ctypes

from libs.global_variables import GDV
from tools.logs import logger


def is_mouse_visible():
    """
    判断鼠标是否可见
    :return:  True: 可见  False: 不可见
    """
    class CURSORINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint),
                    ("flags", ctypes.c_uint),
                    ("hCursor", ctypes.c_void_p),
                    ("ptScreenPos", ctypes.c_long * 2)]

    CI_FLAGS_SHOWING = 0x00000001
    info = CURSORINFO(cbSize=ctypes.sizeof(CURSORINFO))
    ctypes.windll.user32.GetCursorInfo(ctypes.byref(info))
    if info.flags == CI_FLAGS_SHOWING:
        return True
    else:
        if not GDV.in_game:
            GDV.in_game = True
        return False