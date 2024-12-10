#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import asyncio
from functools import partial

from pynput import keyboard

from libs.config import debug
from libs.identification import backpack_identification, current_weapon_identification, start_weapon_identification
from libs.global_variables import GDV, THREAD_POOL


class KeyboardMonitor:
    def __init__(self, window):
        self.monitoring = False
        self.listener = None
        self.window = window

    def start(self):
        self.monitoring = True
        # 初始化并启动键盘监听器
        self.listener = keyboard.Listener(on_press=self.on_key_press)
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
            if GDV.pubg_win or debug:
                if key == "tab":
                    future = THREAD_POOL.submit(backpack_identification)
                    future.add_done_callback(self.on_backpack_identification)

                elif key == "esc":
                    self._close_backpack()

                elif key in ("1", "2"):
                    GDV.current_weapon = key
                    self.window.keyPressedSignal.emit(key)
                    self._shooting_state()

                elif key in ("3", "4", "5", "x", "m"):
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
                    self._shooting_state()
    def on_backpack_identification(self, future):
        future.result()
        if GDV.backpack_state:
            if GDV.shooting_state:
                GDV.shooting_state = False
            self.window.shootingSignal.emit("武器识别中...")
            start_weapon_identification()
            GDV.mouse_right_identification = True
            self.window.keyPressedSignal.emit(GDV.current_weapon)  # 发送信号
        else:
            self._close_backpack()

    def _shooting_state(self):
        future = THREAD_POOL.submit(current_weapon_identification)
        future.add_done_callback(self.on_shooting_state)

    def on_shooting_state(self, future):
        future.result()
        if not GDV.current_weapon_info:
            if GDV.shooting_state:
                GDV.shooting_state = False
            self.window.shootingSignal.emit("没有手持枪械")
        else:
            if not GDV.shooting_state:
                GDV.shooting_state = True
            self.window.shootingSignal.emit("自动识别已完成")

    def _close_backpack(self):
        GDV.mouse_right_identification = False
        GDV.backpack_state = False
        if GDV.guns_data:
            self._shooting_state()
        else:
            if GDV.shooting_state:
                GDV.shooting_state = False
            self.window.shootingSignal.emit("获取背包信息失败, 请重试")
