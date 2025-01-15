#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from PySide6.QtCore import Signal
from pynput import keyboard

from app.common.grenade.grenade_win import GrenadeMainWin
from libs.common import is_mouse_button_down
from libs.config import VK_LBUTTON
from libs.global_variables import GDV, THREAD_POOL
from libs.identification import backpack_identification, current_shooting_state, posture_in_car, \
    start_weapon_identification
from tools.mouse_visible import is_mouse_visible


class KeyboardMonitor:
    GrenadeSignal = Signal()
    def __init__(self, state_win, grenade_win, distance_win, map_mark_win):
        self.monitoring = False
        self.listener = None
        self.state_win = state_win
        self.grenade_win = grenade_win
        self.distance_win = distance_win
        self.map_mark_win = map_mark_win

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
                    if GDV.current_weapon_info:
                        GDV.current_weapon = key
                        if not GDV.shooting_state:
                            GDV.shooting_state = True
                        GDV.state_left_info = "自动识别已完成"
                    else:
                        GDV.state_left_info = "获取背包信息失败, 请重试"
                    self.state_win.Left_StateSignal.emit()
                    self.state_win.Right_PressedSignal.emit()

                elif key in ("3", "4", "5", "x"):
                    self._shooting_state()

                elif key in ("ctrl_l", "space", "z", "c"):
                    if GDV.posture_state_button == key :
                        if GDV.posture_state == "zhan" or GDV.posture_state == "pa":
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
                    self.state_win.Left_StateSignal.emit()

                elif key == "r":
                    if not GDV.shooting_state and is_mouse_button_down(VK_LBUTTON):
                        self.grenade_win.ShowGrenadeSignal.emit()

                elif key == "alt_l":
                    if GDV.map_distance:
                        self.distance_win.ShowDistanceSignal.emit()

                elif key == "up":
                    if GDV.map_marking:
                        self.map_mark_win.MapUpSignal.emit()
                elif key == "down":
                    if GDV.map_marking:
                        self.map_mark_win.MapDownSignal.emit()
    def on_key_release(self, keys):
        key = str(keys.name if isinstance(keys, keyboard.Key) else keys.char).lower()
        if self.monitoring:
            if GDV.pubg_win and GDV.in_game:
                if key == "tab":
                    future = THREAD_POOL.submit(backpack_identification)
                    future.add_done_callback(self.on_backpack_identification)

                elif key == "esc":
                    self._close_backpack()
                    self.map_mark_win.MapMarkCloseSignal.emit()

                elif  key == "m":
                    if is_mouse_visible():
                        if GDV.shooting_state:
                            GDV.shooting_state = False
                        if GDV.map_marking:
                            self.map_mark_win.MapMarkShowSignal.emit()
                    else:
                        self._shooting_state()
                        if GDV.map_marking:
                            self.map_mark_win.MapMarkCloseSignal.emit()
                    self.state_win.Left_StateSignal.emit()

                elif key == "f":
                    self._car_state()

                elif key == "alt_l":
                    self.distance_win.CloneDistanceSignal.emit()
            else:
                if GDV.shooting_state:
                    GDV.shooting_state = False
                self.state_win.Left_StateSignal.emit()

    def on_backpack_identification(self, future):
        future.result()
        if GDV.backpack_state:
            if GDV.shooting_state:
                GDV.shooting_state = False
            GDV.state_left_info = "武器识别中..."
            self.state_win.Left_StateSignal.emit()
            start_weapon_identification()
            GDV.mouse_right_identification = True
            self.state_win.Right_PressedSignal.emit()  # 发送信号
        else:
            self._close_backpack()

    def _shooting_state(self):
        future = THREAD_POOL.submit(current_shooting_state, 0.5)
        future.add_done_callback(self.on_shooting_state)

    def on_shooting_state(self, future):
        future.result()
        if not GDV.shooting_state:
            GDV.state_left_info = "没有手持枪械"
            self.state_win.Left_StateSignal.emit()
        else:
            GDV.state_left_info = "自动识别已完成"
            self.state_win.Left_StateSignal.emit()

    def _close_backpack(self):
        GDV.mouse_right_identification = False
        GDV.backpack_state = False
        if GDV.guns_data:
            self._shooting_state()
        else:
            if GDV.shooting_state:
                GDV.shooting_state = False
            GDV.state_left_info = "获取背包信息失败, 请重试"
            self.state_win.Left_StateSignal.emit()

    def _car_state(self):
        future = THREAD_POOL.submit(posture_in_car)
        future.add_done_callback(self.on_car_state)

    def on_car_state(self, future):
        future.result()
        self.state_win.Left_StateSignal.emit()

