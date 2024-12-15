#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com


import re

import pygetwindow as gw

from tools.logs import logger


def is_pubg_active():
    """
    判断当前活动窗口是否是 PUBG
    :return:  True: 是  False: 不是
    """
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            title = active_window.title.lower()
            if re.search(r'pubg', title):
                return True
    except Exception as e:
        logger.error(f"获取活动窗口失败: {e}")
    return False


if __name__ == "__main__":
    if is_pubg_active():
        print("当前活动窗口是 PUBG")
    else:
        print("当前活动窗口不是 PUBG")
