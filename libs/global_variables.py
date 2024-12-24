#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import threading
from concurrent.futures import ThreadPoolExecutor

from libs.ghub_device import GHubDevice
from tools.logs import logger

THREAD_POOL = ThreadPoolExecutor()

GHUB = GHubDevice()


class Observable:
    def __init__(self):
        self._observers = []
        self._last_notify_time = 0
        self._notify_lock = threading.Lock()
        self._timer = None
        self._auto_update_enabled = True  # 添加标志位

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        if not self._auto_update_enabled:
            return
        with self._notify_lock:
            if self._timer:
                self._timer.cancel()
            self._timer = threading.Timer(0.1, self._execute_notify)
            self._timer.start()

    def _execute_notify(self):
        with self._notify_lock:
            for observer in self._observers:
                observer.update()
            from libs.pressure import Pressure
            Pressure()


class GlobalVariable(Observable):
    def __init__(self):
        super().__init__()
        self._cache = None
        self._mouse_right_identification = False
        self._guns_data = {}
        self._current_weapon = "1"
        self._shooting_state = False
        self._pubg_win = False
        self._in_game = False
        self._current_weapon_info = {}
        self._output_gun_info = {}
        self._opening_method = "click"
        self._posture_state = "zhan"
        self._posture_state_button = "c"
        self._global_screenshot = None
        self._state_left_info = ""
        self._backpack_state = False
        self._mouse_left_state = False
        self._mouse_right_state = False
        self._in_car = False


    @property
    def CACHE(self):
        return self._cache

    @CACHE.setter
    def CACHE(self, value):
        self._cache = value

    @property
    def mouse_right_identification(self):
        return self._mouse_right_identification

    @mouse_right_identification.setter
    def mouse_right_identification(self, value):
        self._mouse_right_identification = value

    @property
    def guns_data(self):
        return self._guns_data

    @guns_data.setter
    def guns_data(self, value):
        self._guns_data = value

    @property
    def current_weapon(self):
        return self._current_weapon

    @current_weapon.setter
    def current_weapon(self, value):
        self._current_weapon = value
        self.notify_observers()

    @property
    def shooting_state(self):
        return self._shooting_state

    @shooting_state.setter
    def shooting_state(self, value):
        self._shooting_state = value
        self.notify_observers()

    @property
    def pubg_win(self):
        return self._pubg_win

    @pubg_win.setter
    def pubg_win(self, value):
        self._pubg_win = value

    @property
    def in_game(self):
        return self._in_game

    @in_game.setter
    def in_game(self, value):
        self._in_game = value

    @property
    def current_weapon_info(self):
        return self._current_weapon_info

    @current_weapon_info.setter
    def current_weapon_info(self, value):
        self._current_weapon_info = value
        self.notify_observers()

    @property
    def output_gun_info(self):
        return self._output_gun_info

    @output_gun_info.setter
    def output_gun_info(self, value):
        self._output_gun_info = value

    @property
    def opening_method(self):
        return self._opening_method

    @opening_method.setter
    def opening_method(self, value):
        self._opening_method = value
        self.notify_observers()

    @property
    def posture_state(self):
        return self._posture_state

    @posture_state.setter
    def posture_state(self, value):
        self._posture_state = value
        self.notify_observers()

    @property
    def posture_state_button(self):
        return self._posture_state_button

    @posture_state_button.setter
    def posture_state_button(self, value):
        self._posture_state_button = value

    @property
    def global_screenshot(self):
        return self._global_screenshot

    @global_screenshot.setter
    def global_screenshot(self, value):
        self._global_screenshot = value

    @property
    def state_left_info(self):
        return self._state_left_info

    @state_left_info.setter
    def state_left_info(self, value):
        self._state_left_info = value

    @property
    def backpack_state(self):
        return self._backpack_state

    @backpack_state.setter
    def backpack_state(self, value):
        self._backpack_state = value

    @property
    def mouse_left_state(self):
        return self._mouse_left_state

    @mouse_left_state.setter
    def mouse_left_state(self, value):
        self._mouse_left_state = value

    @property
    def mouse_right_state(self):
        return self._mouse_right_state

    @mouse_right_state.setter
    def mouse_right_state(self, value):
        self._mouse_right_state = value

    @property
    def in_car(self):
        return self._in_car

    @in_car.setter
    def in_car(self, value):
        self._in_car = value
        self.notify_observers()



GDV = GlobalVariable()  # 全局动态变量