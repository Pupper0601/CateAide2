#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

def coordinate(old):
    old_x, old_y, old_width, old_height = old
    _new_lites = [
        (1728, 1080),
        (1920, 1080),
        (2340, 1440),
        (2560, 1440),
        (2560, 1660),
        (3840, 2160)
    ]
    for _new in _new_lites:
        width_scale = _new[0] / 1920
        height_scale = _new[1] / 1080

        new_x = round(old_x * width_scale)
        new_y = round(old_y * height_scale)
        new_width = round(old_width * width_scale)
        new_height = round(old_height * height_scale)

        print([new_x, new_y, new_width, new_height])


if __name__ == '__main__':
    # _old = [1813, 25,6,30]
    _old = [909, 1000, 17, 20]
    coordinate(_old)
