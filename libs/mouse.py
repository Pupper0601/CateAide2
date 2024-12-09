#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import asyncio
import threading

from pynput import mouse

from libs.common import Worker
from libs.identification import get_in_gram, start_weapon_identification

import libs.global_variables as gv
from tools.current_window import is_pubg_active


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
            elif not pressed and button == mouse.Button.left:
                if not is_pubg_active():
                    self.window.shootingSignal.emit("当前窗口不是PUBG, 请切换到PUBG窗口")
                    gv.shooting_state = False
                    gv.pubg_win = False
                else:
                    gv.pubg_win = True

                    if not gv.GUNS_DATA:
                        self.window.shootingSignal.emit("当前没有枪械信息, 请按 'tab' 键获取")
                        gv.shooting_state = False
                    if not get_in_gram():
                        self.window.shootingSignal.emit("当前不在对局中, 请进入对局后再试")
                        gv.shooting_state = False
