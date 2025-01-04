#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com


import os
import json
import time

import cv2
from PIL import Image

from tools.files import load_file
from tools.logs import logger
from tools.paths import get_project_root, object_join_path

def images_cache(paths):
    """缓存图片"""
    _start_time = time.time()
    images = load_images_from_folder(paths)
    config = load_images_config(paths)
    logger.info(f"图片缓存完成, 耗时: {time.time() - _start_time:.2f} 秒")
    return {"images": images, "config": config}

def load_images_from_folder(paths):
    """从文件夹中加载所有图片"""
    images_path = paths

    images = {}
    for root, dirs, files in os.walk(images_path):  # 遍历文件夹及其子文件夹
        folder_name = os.path.basename(root)  # 获取当前文件夹名称
        if folder_name not in images:
            images[folder_name] = {}

        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # 仅选择图像文件
                file_path = os.path.join(root, filename)
                try:
                    existing_image = cv2.imread(file_path)
                    images[folder_name][filename.split('.')[0]] = existing_image
                except Exception as e:
                    print(f"无法加载图片 {file_path}: {e}")

    return images

def load_images_config(paths):
    """从配置文件中加载图片"""
    config_path = paths + "/config.json"
    config = load_file(config_path)
    return config


if __name__ == "__main__":
    print(images_cache())
