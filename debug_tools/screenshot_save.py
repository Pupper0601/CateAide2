#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

"""
    在指定位置截图, 自适应二值化处理后保存, 用于调试
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from mss import mss
from PIL import Image

import matplotlib


# 设置支持中文的字体（假设你已经安装相应的中文字体）
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置为黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题


def capture_screen_and_process(lists, save_path):
    """截取屏幕区域并保存为图片"""
    sct = mss()
    region = {'left': lists[0], 'top': lists[1], 'width': lists[2], 'height': lists[3]}
    screenshot = sct.grab(region)

    img = Image.frombytes('RGBA', screenshot.size, screenshot.bgra, 'raw', 'BGRA')
    img = img.convert('RGB')  # 转换为 RGB 格式（如果需要保存为 JPEG 或 PNG）

    img_array = np.array(img)
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    # 自适应阈值二值化处理
    binary_img = cv2.adaptiveThreshold(
        gray_img, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        3, 2
    )

    # 保存处理后的图像
    processed_img = Image.fromarray(binary_img)
    processed_img.save(save_path)

    return img, binary_img


def main():
    _paths = r"F:\Object\GitHub\CateAide2\basis_images\stock"
    _lists = {
        "zhedie": [1760, 239, 44, 44],
        "zidandai": [1760, 465, 44, 44]
    }
    for key, value in _lists.items():
        save_path = f"{_paths}/{key}.png"
        screenshot, binary_image = capture_screen_and_process(value, save_path)
        plots(screenshot, binary_image)

def plots(screenshot, binary_image):
    # 显示原图和自适应二值化后的图像
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(screenshot)
    plt.title('原图')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(binary_image, cmap='gray')
    plt.title('自适应二值化图')
    plt.axis('off')

    plt.show()


if __name__ == "__main__":
    main()