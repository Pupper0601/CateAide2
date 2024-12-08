#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

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