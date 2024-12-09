#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import asyncio
from pynput import keyboard

from libs.config import debug
from libs.identification import backpack_identification, current_weapon_identification, start_weapon_identification
from libs.global_variables import GDV


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
                    if asyncio.run(backpack_identification()):
                        GDV.shooting_state = False
                        self.window.shootingSignal.emit("武器识别中...")
                        start_weapon_identification()
                        GDV.mouse_right_identification = True
                        self.window.keyPressedSignal.emit(key)  # 发送信号
                    else:
                        self._close_backpack()

                elif key == "esc":
                    self._close_backpack()

                elif key in ("1", "2"):
                    GDV.current_weapon = key
                    self.window.keyPressedSignal.emit(key)

                elif key in ("3", "4", "5", "x", "m"):
                    self._shooting_state()

                elif key in ("ctrl_l", "space", "z", "c"):
                    posture = GDV.posture_state
                    posture_map = {
                        "c"     : ("蹲姿", "站姿", "dun", "zhan"),
                        "ctrl_l": ("蹲姿", "站姿", "dun", "zhan"),
                        "z"     : ("卧姿", "站姿", "pa", "zhan"),
                        "space" : ("站姿", "站姿", "zhan", "zhan")
                    }
                    if key in posture_map:
                        if GDV.posture_state_button == key.lower() or key.lower() == "z":
                            if posture == posture_map[key][0]:
                                GDV.posture_state = posture_map[key][3]
                            else:
                                GDV.posture_state = posture_map[key][2]

                        elif key == "space":
                            if posture != posture_map[key][0]:
                                GDV.posture_state = posture_map[key][3]

                        self._shooting_state()

    def _shooting_state(self):
        if current_weapon_identification() == "0":
            GDV.shooting_state = False
            self.window.shootingSignal.emit("没有手持枪械")
        else:
            GDV.shooting_state = True
            self.window.shootingSignal.emit("自动识别已完成")

    def _close_backpack(self):
        GDV.mouse_right_identification = False
        if GDV.guns_data:
            self._shooting_state()
        else:
            GDV.shooting_state = False
            self.window.shootingSignal.emit("获取背包信息失败, 请重试")
