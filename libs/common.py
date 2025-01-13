#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import ctypes

from PySide6.QtCore import QObject, Signal


# 自定义信号类，用于发射完成信号
class Worker(QObject):
    finished = Signal()

    def __init__(self, target_function):
        super().__init__()
        self.target_function = target_function

    def run(self):
        self.target_function()
        self.finished.emit()


# 获取键盘状态
def is_mouse_button_down(key):
    state = ctypes.windll.user32.GetAsyncKeyState(key)
    return state & 0x8000 != 0