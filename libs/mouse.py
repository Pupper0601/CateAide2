#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pynput import mouse

from libs.auto_down import is_mouse_pressed, mouse_move_y
from libs.identification import current_weapon_identification, get_in_game, start_weapon_identification

from libs.global_variables import GDV, THREAD_POOL
from tools.current_window import is_pubg_active
from tools.mouse_visible import is_mouse_visible


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
                    if GDV.pubg_win and is_mouse_visible():
                        future = THREAD_POOL.submit(start_weapon_identification)
                        future.add_done_callback(self.on_start_weapon_identification)

            elif not pressed and button == mouse.Button.left:
                if not is_pubg_active():
                    if GDV.shooting_state:
                        GDV.shooting_state = False
                    if GDV.pubg_win:
                        GDV.pubg_win = False
                    GDV.state_left_info = "当前窗口不是PUBG"
                    self.window.shootingSignal.emit()
                else:
                    if not GDV.pubg_win:
                        GDV.pubg_win = True
                    if not  GDV.backpack_state:
                        self.get_game_state()   # 获取当前是否在对局中

    def _shooting_state(self):
        future = THREAD_POOL.submit(current_weapon_identification)
        future.add_done_callback(self.on_shooting_state)

    def on_shooting_state(self, future):
        if future.result() ==  "0":
            if GDV.shooting_state:
                GDV.shooting_state = False
            GDV.state_left_info = "没有手持枪械"
            self.window.shootingSignal.emit()
        else:
            if not GDV.shooting_state:
                GDV.shooting_state = True
            GDV.state_left_info = "自动识别已完成"
            self.window.shootingSignal.emit()

    def get_game_state(self):
        future = THREAD_POOL.submit(get_in_game)
        future.add_done_callback(self.on_get_in_game)

    def on_get_in_game(self, future):
        future.result()
        if not GDV.in_game:
            if GDV.shooting_state:
                GDV.shooting_state = False
            if GDV.posture_state != "zhan":
                GDV.posture_state = "zhan"
            GDV.state_left_info = "当前不在对局中"
            self.window.shootingSignal.emit()
        else:
            if GDV.current_weapon_info:
                self._shooting_state()
            else:
                if GDV.shooting_state:
                    GDV.shooting_state = False
                GDV.state_left_info = "当前没有枪械信息"
                self.window.shootingSignal.emit()

    def on_start_weapon_identification(self, future):
        future.result()
        self.window.keyPressedSignal.emit()