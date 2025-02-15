#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pynput import mouse

from libs.auto_down import mouse_move_y
from libs.global_variables import GDV, THREAD_POOL
from libs.identification import current_posture_state, current_shooting_state, get_in_game, \
    start_weapon_identification
from tools.current_window import is_pubg_active
from tools.mouse_visible import is_mouse_visible


class MouseMonitor:
    def __init__(self, state_win):
        self.monitoring = False
        self.listener = None
        self.state_win = state_win
        self.right_click = False

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
                GDV.mouse_right_state = False
                if GDV.mouse_right_identification and GDV.backpack_state:
                    future = THREAD_POOL.submit(start_weapon_identification)
                    future.add_done_callback(self.on_start_weapon_identification)
                else:
                    if not is_mouse_visible():
                        if not self.right_click:
                            self._shooting_state()
                            self.right_click = True
                        else:
                            self.right_click = False

            elif pressed and button == mouse.Button.right:
                if GDV.in_game and not is_mouse_visible():
                    GDV.mouse_right_state = True
                    self.posture_state()

            elif not pressed and (button == mouse.Button.left or button == mouse.Button.right):
                GDV.mouse_left_state = False
                GDV.mouse_right_state = False
                if not is_pubg_active():    # 判断当前窗口是否是PUBG
                    if GDV.shooting_state:
                        GDV.shooting_state = False
                    if GDV.pubg_win:
                        GDV.pubg_win = False
                    GDV.state_left_info = "当前窗口不是PUBG"
                    self.state_win.Left_StateSignal.emit()
                else:
                    if not GDV.pubg_win:
                        GDV.pubg_win = True
                    self.get_game_state()   # 获取当前是否在对局中


            elif pressed and button == mouse.Button.left:
                if GDV.mouse_server != 2:
                    if GDV.opening_method == 0:
                        GDV.mouse_left_state = True
                        self.auto_down_state()
                    elif GDV.opening_method == 1:
                        if GDV.mouse_right_state:
                            GDV.mouse_left_state = True
                            self.auto_down_state()



    def _shooting_state(self):
        future = THREAD_POOL.submit(current_shooting_state, 0.3)
        future.add_done_callback(self.on_shooting_state)

    def on_shooting_state(self, future):
        future.result()
        if GDV.shooting_state:
            GDV.state_left_info = "自动识别已完成"
            self.state_win.Left_StateSignal.emit()
        else:
            GDV.state_left_info = "没有手持枪械"
            self.state_win.Left_StateSignal.emit()

    def get_game_state(self):
        future = THREAD_POOL.submit(get_in_game)    # 获取当前是否在对局中
        future.add_done_callback(self.on_get_in_game)   # 回调函数

    def on_get_in_game(self, future):
        future.result()
        if not GDV.in_game:
            if GDV.shooting_state:
                GDV.shooting_state = False
            if GDV.posture_state != "zhan":
                GDV.posture_state = "zhan"
            if GDV.in_car:
                GDV.in_car = False
            GDV.state_left_info = "当前不在对局中"
            GDV.guns_data.clear()
            GDV.current_weapon_info.clear()
            self.state_win.Left_StateSignal.emit()
            self.state_win.Right_PressedSignal.emit()
        else:
            if GDV.current_weapon_info:
                self._shooting_state()
            else:
                if GDV.shooting_state:
                    GDV.shooting_state = False
                GDV.state_left_info = "当前没有枪械信息"
                self.state_win.Left_StateSignal.emit()

    def on_start_weapon_identification(self, future):
        future.result()
        self.state_win.Right_PressedSignal.emit()

    def auto_down_state(self):
        future = THREAD_POOL.submit(is_mouse_visible)
        future.add_done_callback(self.mouse_to)

    def mouse_to(self, future):
        if not future.result():
            mouse_move_y(GDV.output_gun_info)

    def posture_state(self):
        future = THREAD_POOL.submit(current_posture_state)
        future.add_done_callback(self.on_posture_state)

    def on_posture_state(self, future):
        future.result()
        self.state_win.Left_StateSignal.emit()
