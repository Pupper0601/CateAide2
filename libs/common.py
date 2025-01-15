#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import ctypes

from PySide6.QtCore import QObject, Signal
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


# 自定义信号类，用于发射完成信号
class Worker(QObject):
    finished = Signal()

    def __init__(self, target_function):
        super().__init__()
        self.target_function = target_function

    def run(self):
        self.target_function()
        self.finished.emit()


# 获取键盘状态
def is_mouse_button_down(key):
    """
    获取鼠标按键状态
    :param key:     按键
    :return:   True 按下，False 未按下
    """
    state = ctypes.windll.user32.GetAsyncKeyState(key)
    return state & 0x8000 != 0

def get_volume():
    # 获取默认音频输出设备
    device = AudioUtilities.GetSpeakers()
    interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # 获取当前音量
    current_volume = volume.GetMasterVolumeLevelScalar()
    return volume, current_volume

def volume_control(volume, current_volume, config):

    # 设定新的音量（例如设定为70%）
    new_volume = current_volume / config
    volume.SetMasterVolumeLevelScalar(new_volume, None)