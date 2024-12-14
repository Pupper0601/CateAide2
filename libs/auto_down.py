#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import ctypes
import time

import pydirectinput


def mouse_move_y(gun_data:dict):
    special_guns = ["ZDZT", "MINI14", "SKS", "VSS", "QBU", "MK14", "MK12", "DLGNF", "M16A4", "MK47"]

    move_coefficient =  move_coefficient_handle(gun_data)

    if gun_data["coefficient"] == "none":
        return
    if gun_data["shooting_state"] == "0":
        return
    if gun_data["weapon"] in special_guns:
        return

    start_time = round(time.perf_counter(), 3) * 1000

    for value in move_coefficient:
        move_sum = int(round(value * gun_data["coefficient"], 2))   # 计算当前移动的距离
        _speed = int(round(move_sum / gun_data["weapon_intervals"] * 15, 2))    # 计算当前移动的速度
        while True:
            if move_sum > _speed:
                pydirectinput.move(xOffset=0, yOffset=_speed, relative=True)
                move_sum -= _speed
            elif move_sum > 0:
                pydirectinput.move(xOffset=0, yOffset=move_sum, relative=True)
                move_sum = 0
            elapsed = (round(time.perf_counter(), 3) * 1000 - start_time)
            if not is_mouse_pressed("left") or elapsed > (value+1)*elapsed + 10:
                if move_sum > 0:
                    pydirectinput.move(xOffset=0, yOffset=move_sum, relative=True)
                break
            time.sleep(0.01)

def move_coefficient_handle(gun_data):
    # 处理武器的移动系数
    lists = []
    for i in gun_data["guns_trajectory"]:
        for key, value in i.items():
            lists.append(value)
    return lists

def is_mouse_pressed(button='left'):
    # 获取某个按键的状态
    if button == 'left':
        return ctypes.windll.user32.GetAsyncKeyState(0x01) != 0
    elif button == 'right':
        return ctypes.windll.user32.GetAsyncKeyState(0x02) != 0
    else:
        raise ValueError("只支持 'left' 或 'right' 按键判断！")