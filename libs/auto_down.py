#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import ctypes
import time

from pynput import mouse
from pynput.keyboard import Controller, Key

from libs.global_variables import GDV, GHUB
from tools.logs import logger


def mouse_move_y(gun_data:dict):
    if not gun_data:
        logger.info("当前武器数据为空")
        return

    special_guns = ["ZDZT", "MINI14", "SKS", "VSS", "QBU", "MK14", "MK12", "DLGNF", "M16A4", "MK47"]

    move_coefficient =  move_coefficient_handle(gun_data)

    if gun_data["coefficient"] == "none":
        return
    if gun_data["shooting_state"] == "0":
        return
    if gun_data["weapon"] in special_guns:
        return
    # keyboard = Controller() # 创建键盘对象
    # keyboard.press(Key.shift)   # 按下shift键
    for index, value in enumerate(move_coefficient):
        if not GDV.mouse_left_state:
            break
        num = 0
        start_time = round(time.perf_counter(), 3) * 1000
        move_sum = int(round(value * gun_data["coefficient"], 2))   # 计算当前移动的距离
        _speed = int(round(move_sum / gun_data["weapon_intervals"] * 15, 2))    # 计算当前移动的速度
        logger.info(f"\n\n 当前子弹数为: {index + 1}, 需要移动的距离为: {move_sum}, 每次移动的距离为: {_speed}, 鼠标左键状态:"
                    f" {GDV.mouse_left_state}")
        while GDV.mouse_left_state:
            if move_sum > _speed:
                GHUB.mouse_xy(0, _speed)
                move_sum -= _speed
            elif move_sum > 0:
                GHUB.mouse_xy(0, _speed)
                move_sum = 0
            elapsed = (round(time.perf_counter(), 3) * 1000 - start_time)
            if not GDV.mouse_left_state or elapsed > gun_data["weapon_intervals"] - 10:
                if move_sum > 0:
                    GHUB.mouse_xy(0, _speed)
                logger.info(f"退出循环, {elapsed}")
                break
            time.sleep(0.01)
            num += 1
            # logger.info(f"当前移动次数: {num},  剩余移动距离: {move_sum}, 消耗的时间: {elapsed}")
    # keyboard.release(Key.shift) # 释放shift键

def move_coefficient_handle(gun_data):
    # 处理武器的移动系数
    lists = []
    for i in gun_data["guns_trajectory"]:
        for key, value in i.items():
            lists.append(value)
    return lists
