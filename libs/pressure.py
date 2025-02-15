#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import json
import os
import sys
from pathlib import Path

from libs.global_variables import GDV, THREAD_POOL
from tools.files import load_file
from tools.logs import logger
from tools.paths import object_join_path

gun_data_factor = None


class Pressure:
    def __init__(self):
        # self.s = weapon_info
        THREAD_POOL.submit(self.write_dict_to_lua_file)

    @staticmethod
    def get_component_factor():
        if GDV.mouse_server != 2:
            _gun_data = load_file(object_join_path("gun_data.json"))
        else:
            _gun_data = load_file(object_join_path("ghub_data.json"))

        _factor_data = {}
        current_weapon_info = GDV.current_weapon_info
        # {'weapon': ['Beryl M762', 'M762'], 'scope': ['红点瞄准镜', 'hongdian'], 'muzzle': ['后座补偿器', 'buchang-b'], 'grip': ['垂直握把', 'chuizhi'], 'stock': ['无枪托', 'stock_none']}
        if current_weapon_info:
            _weapon_name = current_weapon_info["weapon"][1]
            # 获取当前武器名称
            _factor_data["weapon"] = _weapon_name

            # 获取当前武器的配件系数
            _components = _gun_data["component_factor"]
            if _weapon_name in _components.keys():
                _factors = _components[_weapon_name]
                for key, value in current_weapon_info.items():  # 'scope',  ['红点瞄准镜', 'hongdian']
                    if key != "weapon":
                        try:
                            if key == "scope":
                                _factor_data["magnifying_power"] = _gun_data["global_magnifying_power"][value[1]]
                            _factor_data[key] = _factors[key][value[1]]
                        except KeyError:
                            logger.error(f"配件系数中没有找到对应的配件: {value[1]}")
                            _factor_data[key] = 1.0

                # 获取当前是否在车上
                if GDV.in_car:
                    _factor_data["car"] = _factors["car"]["car"]
                else:
                    _factor_data["car"] = 1.0

                # 获取当前姿态
                _factor_data["posture_state"] = _factors["pose"][GDV.posture_state]
                # 获取当前武器基础系数
                if _weapon_name in _gun_data["alone_factor"].keys():
                    _factor_data["alone_factor"] = _gun_data["alone_factor"][_weapon_name]
                # 获取当前武器射击间隔
                if _weapon_name in _gun_data["weapon_intervals"].keys():
                    _factor_data["weapon_intervals"] = _gun_data["weapon_intervals"][_weapon_name]

                # 获取当前武器弹道
                if _weapon_name in _gun_data["guns_trajectory"].keys():
                    _factor_data["guns_trajectory"] = _gun_data["guns_trajectory"][_weapon_name]["default"]
            else:
                _factor_data["no_gun"] = True

            # 获取武器射击状态
            if GDV.shooting_state:
                _factor_data["shooting_state"] = "1"
            else:
                _factor_data["shooting_state"] = "0"

            # 开镜方式
            _factor_data["opening_method"] = GDV.opening_method

            # 获取全局 shift 系数
            _factor_data["global_lshift"] = _gun_data["global_lshift"]

            # 获取全局后坐力系数
            _factor_data["global_recoil"] = _gun_data["global_recoil"]

            logger.info(f"当前武器压枪信息: {_factor_data}")
            return _factor_data

    def calculate_factors(self):
        _effect_data = self.get_component_factor()
        if _effect_data is not None:
            if not _effect_data.get("no_gun"):
                coefficient = 1.0
                for key in ("scope", "muzzle", "grip", "stock", "global_recoil", "alone_factor", "magnifying_power",
                            "posture_state", "car"):
                    coefficient *= _effect_data[key]
                    del _effect_data[key]

                _effect_data["coefficient"] = coefficient

                return _effect_data
            else:
                _effect_data["coefficient"] = "none"
                return _effect_data

    def write_dict_to_lua_file(self):

        _gun_info = self.calculate_factors()
        logger.info(f"当前压枪数据: {_gun_info}")

        if _gun_info == GDV.output_gun_info:
            logger.info("压枪数据没有变化, 不需要更新")
            return
        else:
            GDV.output_gun_info = _gun_info

        if GDV.mouse_server != 2:    # 如果是系统鼠标, 则不写入文件
            logger.info("当前使用的是系统鼠标, 不写入文件")
            return

        file_path = "C:/CuteAide/output.lua"
        path = Path(file_path)  # 创建文件
        if not path.is_file():  # 如果文件不存在, 则创建文件
            path.parent.mkdir(parents=True, exist_ok=True)  # 创建文件夹
            path.touch()    # 创建文件

        with open(file_path, 'w', encoding='utf-8') as file:
            file.truncate(0)  # 清空文件内容
            if _gun_info is not None:
                for key, value in _gun_info.items():
                    if isinstance(value, str):
                        file.write(f"{key} = '{value}'\n")
                    elif isinstance(value, list):
                        if key == "guns_trajectory":
                            formatted_list = ", ".join([f"{{{list(item.keys())[0]}, {list(item.values())[0]}}}" for
                                                        item in value])
                            file.write(f"{key} = {{{formatted_list}}}\n")
                    else:
                        file.write(f"{key} = {value}\n")
                logger.info(f"更新压枪数据成功, 新数据以写入文件: {file_path}")


if __name__ == '__main__':
    a = {'weapon': ['Beryl M762', 'M762'], 'scope': ['红点瞄准镜', 'hongdian'], 'muzzle': ['后座补偿器', 'buchang-b'],
         'grip'  : ['垂直握把', 'chuizhi'], 'stock': ['无枪托', 'stock_none']}
    # p = Pressure(a)
