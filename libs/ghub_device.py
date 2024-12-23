#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from ctypes import CDLL

from tools.logs import logger
from tools.paths import object_join_path

class GHubDevice:

    def __init__(self):
        try:
            self.gm = CDLL(object_join_path(r'libs/ghub_device.dll'))
            self.ghd = self.gm.device_open() == 1
            if not self.ghd:
                logger.info('未安装ghub或者lgs驱动!!!')
            else:
                logger.info('初始化成功!')
        except FileNotFoundError:
            logger.error('缺少文件')

    #按下鼠标按键
    def press_mouse_button(self, button):
        if self.ghd:
            self.gm.mouse_down(button)

    #松开鼠标按键
    def release_mouse_button(self, button):
        if self.ghd:
            self.gm.mouse_up(button)

    #点击鼠标
    def click_mouse_button(self, button):
        self.press_mouse_button(button)
        self.release_mouse_button(button)

    #按下键盘按键
    def press_key(self, code):
        if self.ghd:
            self.gm.key_down(code)

    #松开键盘按键
    def release_key(self, code):
        if self.ghd:
            self.gm.key_up(code)

    #点击键盘按键
    def click_key(self, code):
        self.press_key(code)
        self.release_key(code)

    # 鼠标移动
    def mouse_xy(self, x, y, abs_move = False):
        if self.ghd:
            self.gm.moveR(int(x), int(y), abs_move)