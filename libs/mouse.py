#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import asyncio
import threading

from pynput import mouse

from libs.common import Worker
from libs.identification import start_weapon_identification

import libs.global_variables as gv


class MouseMonitor:
    def __init__(self, window):
        self.monitoring = False
        self.listener = None
        self.window = window

    def start(self):
        self.monitoring = True
        # 初始化并启动鼠标监听器
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def stop(self):
        self.monitoring = False
        # 停止监听器
        if self.listener:
            self.listener.stop()

    def on_click(self, x, y, button, pressed):
        if self.monitoring:
            if pressed and button == mouse.Button.right and  gv.MOUSE_RIGHT_IDENTIFICATION:
                start_weapon_identification()
                self.window.keyPressedSignal.emit("right")



