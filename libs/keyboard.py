#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import asyncio

from pynput import keyboard

from libs.config import debug
from libs.identification import backpack_identification, weapon_identification
from tools.current_window import is_pubg_active
from tools.logs import logger
import libs.global_variables as gv


class KeyboardMonitor:
    def __init__(self):
        self.monitoring = False
        self.listener = None

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
                        weapon_identification()
                        gv.MOUSE_RIGHT_IDENTIFICATION = True
                    else:
                        gv.MOUSE_RIGHT_IDENTIFICATION = False
                elif key == "esc":
                    if not backpack_identification():
                        print("按下了 esc 键")
                elif key in ("1", "2", "3", "4", "5"):
                    print(f"按下了数字键 {key}")
                elif key == "x":
                    print("按下了 x 键")


