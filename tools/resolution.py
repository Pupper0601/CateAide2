#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com


from screeninfo import get_monitors

from tools.logs import logger


def get_primary_screen_resolution():
    """ 获取主屏幕分辨率 """
    monitors = get_monitors()
    for monitor in monitors:
        if monitor.is_primary:
            return monitor.width, monitor.height
    logger.error("未找到主屏幕")
    return None


if __name__ == "__main__":
    resolution = get_primary_screen_resolution()
    if resolution:
        print(f"主屏幕分辨率: {resolution[0]}x{resolution[1]}")
    else:
        print("未找到主屏幕")
