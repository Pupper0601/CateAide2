#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import asyncio
import threading

from PySide6.QtCore import QObject, QThread, Signal
from pynput import keyboard

from libs.common import Worker
from libs.config import debug
from libs.identification import backpack_identification, current_weapon_identification, start_weapon_identification
from tools.current_window import is_pubg_active
from tools.logs import logger
import libs.global_variables as gv


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
            if is_pubg_active() or debug:
                if key == "tab":
                    if asyncio.run(backpack_identification()):
                        start_weapon_identification()
                        gv.MOUSE_RIGHT_IDENTIFICATION = True
                        self.window.keyPressedSignal.emit(key)  # 发送信号
                    else:
                        gv.MOUSE_RIGHT_IDENTIFICATION = False
                elif key == "esc":
                    if not asyncio.run(backpack_identification()):
                        gv.MOUSE_RIGHT_IDENTIFICATION = False
                elif key in ("1", "2"):
                    gv.CURRENT_WEAPON = key
                    self.window.keyPressedSignal.emit(key)
                elif key in ("3", "4", "5"):
                    if asyncio.run(current_weapon_identification()) == "0":
                        gv.shooting_state = False
                        self.window.shootingSignal.emit("没有手持枪械, 暂停压枪")
                    else:
                        gv.shooting_state = True
                        self.window.shootingSignal.emit("枪械已自动识别完成, 开始压枪")

                elif key == "x":
                    if asyncio.run(current_weapon_identification()) == "0":
                        gv.shooting_state = False
                        self.window.shootingSignal.emit("没有手持枪械, 暂停压枪")
                    else:
                        gv.shooting_state = True
                        self.window.shootingSignal.emit("枪械已自动识别完成, 开始压枪")
            else:
                self.window.shootingSignal.emit("当前不是 PUBG 窗口")
                gv.shooting_state = False

    def get_current_weapon(self):
        _gun = current_weapon_identification()
        if _gun == "0":
            gv.shooting_state = False
        else:
            gv.shooting_state = True
