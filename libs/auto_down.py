#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import time
import pydirectinput

from libs.global_variables import GDV, GHUB
from tools.logs import logger


def mouse_move_y(gun_data: dict):
    if gun_data is None or len(gun_data) == 0:
        logger.info("当前武器数据为空")
        return

    if gun_data["coefficient"] == "none":
        return
    if gun_data["shooting_state"] == "0":
        return

    special_guns = ["ZDZT", "MINI14", "SKS", "VSS", "QBU", "MK14", "MK12", "DLGNF", "M16A4", "MK47"]
    if gun_data["weapon"] in special_guns:
        return
    # keyboard = Controller() # 创建键盘对象
    # keyboard.press(Key.shift)   # 按下shift键

    move_coefficient = move_coefficient_handle(gun_data)

    for index, value in enumerate(move_coefficient):
        if not GDV.mouse_left_state:
            break

        num = 0
        start_time = round(time.perf_counter(), 3) * 1000   # 记录开始时间
        move_sum = round(value * gun_data["coefficient"], 2)  # 计算当前移动的距离
        _speed = round(move_sum / gun_data["weapon_intervals"] * 15, 2)  # 计算当前移动的速度
        logger.info(
            f"\n\n 当前子弹数为: {index + 1}, 需要移动的距离为: {move_sum}, 每次移动的距离为: {_speed}, 鼠标左键状态:"
            f" {GDV.mouse_left_state}")
        while GDV.mouse_left_state:
            move_y = keep_deci(_speed)
            if move_sum > _speed:
                mouse_move(0, move_y)
                move_sum -= move_y
            elif move_sum > 0:
                mouse_move(0, _speed)
                move_sum = 0
            elapsed = (round(time.perf_counter(), 3) * 1000 - start_time)
            if not GDV.mouse_left_state or elapsed > gun_data["weapon_intervals"] - 10:
                if move_sum > 0:
                    mouse_move(0, _speed)
                logger.info(f"退出循环, {elapsed}")
                break
            time.sleep(0.01)
            num += 1
        logger.info(f"当前子弹移动耗时: {round(time.perf_counter(), 3) * 1000 - start_time}")
        # logger.info(f"当前移动次数: {num},  剩余移动距离: {move_sum}, 消耗的时间: {elapsed}")
    # keyboard.release(Key.shift) # 释放shift键


decimals = 0
def  keep_deci(moves):
    # 保留小数点后三位
    global decimals
    moves += decimals
    tmp_int = int(moves)
    decimals = moves - tmp_int
    return tmp_int


def move_coefficient_handle(gun_data):
    # 处理武器的移动系数
    lists = []
    for i in gun_data["guns_trajectory"]:
        for key, value in i.items():
            lists.append(value)
    return lists

def mouse_move(x,y):
    if GDV.mouse_server == 0:
        pydirectinput.move(x,y)
    elif GDV.mouse_server == 1:
        GHUB.mouse_xy(x,y)
