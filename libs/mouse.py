#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pynput import mouse

from libs.identification import current_weapon_identification, get_in_gram, start_weapon_identification

from libs.global_variables import GDV
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
            if pressed and button == mouse.Button.right and  GDV.mouse_right_identification:
                start_weapon_identification()
                self.window.keyPressedSignal.emit("right")
            elif not pressed and button == mouse.Button.left:
                if not is_pubg_active():
                    GDV.shooting_state = False
                    GDV.pubg_win = False
                    self.window.shootingSignal.emit("当前窗口不是PUBG")
                else:
                    GDV.pubg_win = True
                    if not GDV.guns_data:
                        GDV.shooting_state = False
                        self.window.shootingSignal.emit("当前没有枪械信息")
                    else:
                        if current_weapon_identification() != "0":
                            GDV.shooting_state = True
                            self.window.shootingSignal.emit("自动识别已完成")
                        else:
                            GDV.shooting_state = False
                            self.window.shootingSignal.emit("自动识别已完成")
                    if not get_in_gram():
                        GDV.shooting_state = False
                        self.window.shootingSignal.emit("当前不在对局中")
