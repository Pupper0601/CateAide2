#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pynput import keyboard

from libs.identification import backpack_identification, current_weapon_identification, start_weapon_identification
from libs.global_variables import GDV, THREAD_POOL
from tools.mouse_visible import is_mouse_visible


class KeyboardMonitor:
    def __init__(self, window):
        self.monitoring = False
        self.listener = None
        self.window = window

    def start(self):
        self.monitoring = True
        # 初始化并启动键盘监听器
        self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()

    def stop(self):
        self.monitoring = False
        # 停止监听器
        if self.listener:
            self.listener.stop()

    def on_key_press(self, keys):
        key = str(keys.name if isinstance(keys, keyboard.Key) else keys.char).lower()
        replace_dict = {"!": "1","@": "2","#": "3","$": "4","%": "5"}
        key = replace_dict.get(key, key)
        if self.monitoring: # 检查是否正在监听
            if GDV.pubg_win and GDV.in_game:
                if key in ("1", "2"):
                    GDV.current_weapon = key
                    self.window.keyPressedSignal.emit()
                    self._shooting_state()


                elif key in ("3", "4", "5", "x"):
                    self._shooting_state()

                elif key in ("ctrl_l", "space", "z", "c"):
                    if GDV.posture_state_button == key :
                        if GDV.posture_state == "zhan":
                            GDV.posture_state = "dun"
                        else:
                            GDV.posture_state = "zhan"
                    elif key == "space":
                        if GDV.posture_state != "zhan":
                            GDV.posture_state = "zhan"
                    elif key == "z":
                        if GDV.posture_state == "pa":
                            GDV.posture_state = "zhan"
                        else:
                            GDV.posture_state = "pa"
                    self.window.shootingSignal.emit()

    def on_key_release(self, keys):
        key = str(keys.name if isinstance(keys, keyboard.Key) else keys.char).lower()
        if self.monitoring:
            if GDV.pubg_win and GDV.in_game:
                if key == "tab":
                    future = THREAD_POOL.submit(backpack_identification)
                    future.add_done_callback(self.on_backpack_identification)

                elif key == "esc":
                    self._close_backpack()

                elif  key == "m":
                    if is_mouse_visible():
                        if GDV.shooting_state:
                            GDV.shooting_state = False
                    else:
                        self._shooting_state()
                    self.window.shootingSignal.emit()

    def on_backpack_identification(self, future):
        future.result()
        if GDV.backpack_state:
            if GDV.shooting_state:
                GDV.shooting_state = False
            GDV.state_left_info = "武器识别中..."
            self.window.shootingSignal.emit()
            start_weapon_identification()
            GDV.mouse_right_identification = True
            self.window.keyPressedSignal.emit()  # 发送信号
        else:
            self._close_backpack()

    def _shooting_state(self):
        future = THREAD_POOL.submit(current_weapon_identification)
        future.add_done_callback(self.on_shooting_state)

    def on_shooting_state(self, future):
        if future.result() == "0":
            if GDV.shooting_state:
                GDV.shooting_state = False
            GDV.state_left_info = "没有手持枪械"
            self.window.shootingSignal.emit()
        else:
            if not GDV.shooting_state:
                GDV.shooting_state = True
            GDV.state_left_info = "自动识别已完成"
            self.window.shootingSignal.emit()

    def _close_backpack(self):
        if not is_mouse_visible():
            GDV.mouse_right_identification = False
            GDV.backpack_state = False
            if GDV.guns_data:
                self._shooting_state()
            else:
                if GDV.shooting_state:
                    GDV.shooting_state = False
                GDV.state_left_info = "获取背包信息失败, 请重试"
                self.window.shootingSignal.emit()
        else:
            if GDV.shooting_state:
                GDV.shooting_state = False
            self.window.shootingSignal.emit()
