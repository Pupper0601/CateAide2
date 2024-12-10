#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pynput import mouse

from libs.identification import current_weapon_identification, get_in_game, start_weapon_identification

from libs.global_variables import GDV, THREAD_POOL
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
            if not pressed and button == mouse.Button.right:
                if GDV.mouse_right_identification:
                    future = THREAD_POOL.submit(start_weapon_identification)
                    future.add_done_callback(self.on_start_weapon_identification)

            elif not pressed and button == mouse.Button.left:
                if not is_pubg_active():
                    if GDV.shooting_state:
                        GDV.shooting_state = False
                    if GDV.pubg_win:
                        GDV.pubg_win = False
                    self.window.shootingSignal.emit("当前窗口不是PUBG")
                else:
                    if not GDV.pubg_win:
                        GDV.pubg_win = True
                    if not GDV.guns_data:
                        if GDV.shooting_state:
                            GDV.shooting_state = False
                        self.window.shootingSignal.emit("当前没有枪械信息")
                    else:
                        self._shooting_state()
                    if not get_in_game():
                        if GDV.shooting_state:
                            GDV.shooting_state = False
                        self.window.shootingSignal.emit("当前不在对局中")

    def _shooting_state(self):
        future = THREAD_POOL.submit(current_weapon_identification)
        future.add_done_callback(self.on_shooting_state)

    def on_shooting_state(self, future):
        if future.result() == "0":
            if GDV.shooting_state:
                GDV.shooting_state = False
            self.window.shootingSignal.emit("没有手持枪械")
        else:
            if not GDV.shooting_state:
                GDV.shooting_state = True
            self.window.shootingSignal.emit("自动识别已完成")

    def on_start_weapon_identification(self, future):
        self.window.keyPressedSignal.emit("right")