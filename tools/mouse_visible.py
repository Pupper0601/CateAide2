#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import ctypes


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
    return info.flags == CI_FLAGS_SHOWING