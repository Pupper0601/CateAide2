#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

"""
处理多个位置的屏幕截图并对比
"""
import asyncio
import time
import cv2
import numpy as np
from PIL import Image
from mss import mss

from libs.config import TRANSLATE, debug
from libs.global_variables import CACHE_IMAGES, GUNS_DATA
from tools.logs import logger
from skimage.metrics import structural_similarity as ssim
import libs.global_variables as gv



def take_screenshot(region):
    """截取屏幕区域并返回为图片"""
    sct = mss()
    screenshot = sct.grab(region)
    img = Image.frombytes('RGBA', screenshot.size, screenshot.bgra, 'raw', 'BGRA')
    img = img.convert('RGB')  # 转换为 RGB 格式
    return np.array(img)

def adaptive_binarize_image(image):
    """对输入图像进行自适应二值化处理"""
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 3, 2)
    return None

def compare_images(binary_image, key):
    """比较图片，返回与文件夹中图片的相似度最高的图片名称"""
    best_match = None     # 最佳匹配图片名称
    best_similarity = 0   # 最佳匹配图片的相似度

    for img_key, img_value in CACHE_IMAGES["images"][key].items():
        img_bin_value = adaptive_binarize_image(img_value)

        if img_bin_value is not None:
            # 计算 SSIM 相似度
            similarity, _ = ssim(binary_image, img_bin_value, full=True)

            if similarity > best_similarity:
                best_similarity = similarity
                best_match = img_key

    if debug:
        logger.info(f"{key} 相似度: {best_similarity:.2f}\n")

    return best_match, best_similarity

def process_screenshot(key, value):
    """处理单个截图，返回相似度最高的图片名称和相似度"""
    region = {'left': value[0], 'top': value[1], 'width': value[2], 'height': value[3]}
    screenshot = take_screenshot(region)

    if screenshot is None:
        logger.error(f"截图失败，区域: {region}")
        return None, None

    binary_image = adaptive_binarize_image(screenshot)

    if binary_image is None:
        logger.error(f"二值化处理失败，区域: {region}")
        return None, None

    best_match, best_similarity = compare_images(binary_image, key)
    return best_match, best_similarity

def start_weapon_identification():
    """处理枪械截图，返回相似度最高的图片名称和相似度"""
    start_time = time.time()
    _guns = {"1":{}, "2":{}}

    for key, value in CACHE_IMAGES["config"]["guns"].items():
        if weapon_position_identification(key):
            for _key, _value in value.items():
                best_match, best_similarity = process_screenshot(_key, _value)
                if best_match is not None:
                    if best_similarity > 0.6:
                        _guns[key][_key]= best_match
                    else:
                        _guns[key][_key]= f"{_key}_none"
                else:
                    _guns[key][_key]= f"{_key}_none"
        else:
            _guns[key] = {
                "weapon": "weapon_none",
                "scope": "scope_none",
                "muzzle": "muzzle_none",
                "grip": "grip_none",
                "stock": "stock_none"}

    logger.info(f"获取枪械信息耗时: {time.time() - start_time:.2f}秒")
    for key, value in _guns.items():
        for k, v in value.items():
            _guns[key][k] = [TRANSLATE.get(v, v), v]
    GUNS_DATA.update(_guns)
    logger.info(f"枪械信息: {GUNS_DATA}")

async def backpack_identification():
    """处理背包截图"""
    await asyncio.sleep(0.1)
    start_time = time.time()
    _value = CACHE_IMAGES["config"]["inventory"]["inventory"]

    best_match, best_similarity = process_screenshot("inventory", _value)
    if best_similarity > 0.6:
        logger.info(f"当前背包状态 --->>> 打开, 识别耗时: {time.time() - start_time:.2f}秒, 相似度: {best_similarity:.2f}")
        return True
    else:
        logger.info(f"当前背包状态 --->>> 关闭, 识别耗时: {time.time() - start_time:.2f}秒, 相似度: {best_similarity:.2f}")
        return False

def weapon_position_identification(key):
    """处理枪械位置截图"""
    start_time = time.time()
    _value = CACHE_IMAGES["config"]["position"][key]

    best_match, best_similarity = process_screenshot("position", _value)
    if best_similarity > 0.6:
        logger.info(f"{key} 号位置 有武器, 识别耗时: {time.time() - start_time:.2f}秒, 相似度: {best_similarity:.2f}")
        return True
    else:
        logger.info(f"{key} 号位置 没有武器, 识别耗时: {time.time() - start_time:.2f}秒, 相似度: {best_similarity:.2f}")
        if gv.CURRENT_WEAPON == key:
            gv.CURRENT_WEAPON = "2" if key == "1" else "1"
        return False

async def current_weapon_identification():
    """处理当前武器截图"""
    await asyncio.sleep(0.5)
    start_time = time.time()
    _value = CACHE_IMAGES["config"]["shooting_state"]
    for k, v in _value.items():
        region = {'left': v[0], 'top': v[1], 'width': v[2], 'height': v[3]}
        screenshot = take_screenshot(region)
        if has_large_color_block(screenshot):
            logger.info(f"当前武器状态 --->>> {k}, 识别耗时: {time.time() - start_time:.2f}秒")
            return k
    logger.info(f"当前武器状态 --->>> 无, 识别耗时: {time.time() - start_time:.2f}秒")
    return "0"

def has_large_color_block(image_array, threshold=210):
    """检查图像中是否存在大于阈值的色块"""
    if np.any(image_array > threshold):
        return True
    return False

def get_in_gram():
    start_time = time.time()
    _value = CACHE_IMAGES["config"]["ingram"]["ingram"]
    region = {'left': _value[0], 'top': _value[1], 'width': _value[2], 'height': _value[3]}
    screenshot = take_screenshot(region)
    if has_large_color_block(screenshot):
        logger.info(f"当前正在对局中, 识别耗时: {time.time() - start_time:.2f}秒")
        return True
    else:
        logger.info(f"当前未在对局中, 识别耗时: {time.time() - start_time:.2f}秒")
        return False




if __name__ == '__main__':
    # weapon_identification()
    # print(GUNS_DATA)
    # print(backpack_identification())
    # print(weapon_position_identification("2"))
    print(current_weapon_identification())
