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
import mss

from libs.config import TRANSLATE, debug
from libs.global_variables import GDV
from tools.logs import logger
from skimage.metrics import structural_similarity as ssim

from tools.mouse_visible import is_mouse_visible


def take_full_screenshot():
    """
    截取整个屏幕
    :return: 将截取的屏幕保存在全局变量中
    """
    with mss.mss() as sct:
        start_time = time.time()
        monitor = sct.monitors[1]  # 获取主显示器的分辨率
        captured_frame = sct.grab(monitor)  # 截取整个屏幕的屏幕截图
        img = Image.frombytes('RGBA', captured_frame.size, captured_frame.bgra, 'raw', 'BGRA')
        img = img.convert('RGB')  # 转换为 RGB 格式

        GDV.global_screenshot = np.array(img)
        logger.info(f"截取整个屏幕耗时: {time.time() - start_time:.2f}秒")

def get_specific_regin(image, region):
    """
    获取指定区域的图片
    :param image: 存放全屏截图的变量
    :param region: 需要截取的区域, 格式为 (left, top, width, height)
    :return: 返回截取的图片
    """
    region = {'left': region[0], 'top': region[1], 'width': region[2], 'height': region[3]}
    return image[region['top']:region['top'] + region['height'], region['left']:region['left'] + region['width']]

def take_screenshot(region):
    """
    截取屏幕指定区域
    :param region: 需要截取的区域, 格式为 (left, top, width, height)
    :return: 截取的图片
    """
    
    """截取屏幕区域并返回为图片"""
    region = {'left': region[0], 'top': region[1], 'width': region[2], 'height': region[3]}
    sct = mss.mss()
    screenshot = sct.grab(region)
    img = Image.frombytes('RGBA', screenshot.size, screenshot.bgra, 'raw', 'BGRA')
    img = img.convert('RGB')  # 转换为 RGB 格式
    return np.array(img)

def adaptive_binarize_image(image):
    """
    对输入图像进行自适应二值化处理
    :param image: 需要处理的图像
    :return: 返回处理后的图像 或 None
    """
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 3, 2)
    return None

def compare_images(binary_image, key):
    """
    比较图片，返回与文件夹中图片的相似度最高的图片名称
    :param binary_image: 二值化处理后的图片
    :param key: 需要遍历的文件夹名称
    :return: 最佳匹配图片名称, 最佳匹配图片的相似度
    """
    best_match = None     # 最佳匹配图片名称
    best_similarity = 0   # 最佳匹配图片的相似度

    for img_key, img_value in GDV.CACHE["images"][key].items():
        img_bin_value = adaptive_binarize_image(img_value)

        if img_bin_value is not None:
            # 计算 SSIM 相似度
            similarity, _ = ssim(binary_image, img_bin_value, full=True)

            if similarity > best_similarity:
                best_similarity = similarity
                best_match = img_key

    if debug:
        logger.info(f"{key} 相似度: {best_similarity:.2f}")

    return best_match, best_similarity

def process_screenshot(key, value):
    """
    截取指定区域的图片并进行二值化处理，返回与文件夹中图片的相似度最高的图片名称
    :param key: 需要遍历的文件夹名称
    :param value: 需要截取的区域, 格式为 (left, top, width, height)
    :return: 最佳匹配图片名称, 最佳匹配图片的相似度
    """

    screenshot = get_specific_regin(GDV.global_screenshot, value)

    if screenshot is None:
        logger.error(f"截图失败{key}，区域: {value}")
        return None, None

    binary_image = adaptive_binarize_image(screenshot)

    if binary_image is None:
        logger.error(f"二值化处理失败{key}，区域: {value}")
        return None, None

    best_match, best_similarity = compare_images(binary_image, key)
    return best_match, best_similarity

def start_weapon_identification():
    """
    获取背包中的枪械信息, 并将结果存入全局变量中
    :return:
    """
    take_full_screenshot()  # 截取整个屏幕
    start_time = time.time()
    _guns = {"1":{}, "2":{}}

    for key, value in GDV.CACHE["config"]["guns"].items():
        if weapon_position_identification(key): # 判断背包中的枪械位置是否有武器
            for _key, _value in value.items():
                best_match, best_similarity = process_screenshot(_key, _value)  # 获取枪械信息
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
    GDV.guns_data.update(_guns)

def backpack_identification():
    """
    判断当前是否打开背包
    :return: True or False
    """
    time.sleep(0.3)
    take_full_screenshot()
    start_time = time.time()
    _value = GDV.CACHE["config"]["inventory"]["inventory"]

    best_match, best_similarity = process_screenshot("inventory", _value)
    if best_similarity > 0.6:
        logger.info(f"当前背包状态 --->>> 打开, 识别耗时: {time.time() - start_time:.2f}秒, 相似度: {best_similarity:.2f}")
        GDV.backpack_state = True
    else:
        logger.info(f"当前背包状态 --->>> 关闭, 识别耗时: {time.time() - start_time:.2f}秒, 相似度: {best_similarity:.2f}")
        GDV.backpack_state = False


def weapon_position_identification(key):
    """
    判断背包中的枪械位置是否有武器
    :param key: 位置编号
    :return: True or False
    """
    start_time = time.time()
    _value = GDV.CACHE["config"]["position"][key]

    best_match, best_similarity = process_screenshot("position", _value)
    if best_similarity > 0.6:
        logger.info(f"{key} 号位置 有武器, 识别耗时: {time.time() - start_time:.2f}秒, 相似度: {best_similarity:.2f}")
        return True
    else:
        logger.info(f"{key} 号位置 没有武器, 识别耗时: {time.time() - start_time:.2f}秒, 相似度: {best_similarity:.2f}")
        if GDV.current_weapon == key:
            GDV.current_weapon = "2" if key == "1" else "1"
        return False

def current_weapon_identification():
    """
    判断当前所持的武器
    :return:
    """
    time.sleep(0.5)
    start_time = time.time()
    _value = GDV.CACHE["config"]["shooting_state"]
    _img = take_screenshot(_value)
    res, coordinates = has_large_color_block(_img)
    if res:
        if coordinates[0][0] > 50:
            k = "1"
        else:
            k = "2"
        logger.info(f"当前所持武器 --->>> {k}, 识别耗时: {time.time() - start_time:.2f}秒")
        GDV.current_weapon = k
        return k
    return "0"

def current_shooting_state(timeout=0):
    """
    判断当前是否可以压枪
    :return:  GDV.shooting_state(True or False)
    """
    time.sleep(timeout)
    start_time = time.time()
    _value = GDV.CACHE["config"]["shooting_state"]
    _img = take_screenshot(_value)
    res, coordinates = has_large_color_block(_img)
    if res:
        if not GDV.shooting_state:
            GDV.shooting_state = True
            logger.info(f"当前可以压枪, 识别耗时: {time.time() - start_time:.2f}秒")
    else:
        if GDV.shooting_state:
            GDV.shooting_state = False
            logger.info(f"当前不能压枪, 识别耗时: {time.time() - start_time:.2f}秒")

def has_large_color_block(image_array, threshold=220):
    """
    检查图像中是否存在大于阈值的色块，并返回其坐标
    :param image_array: 需要处理的图像
    :param threshold: 颜色阈值
    :return: True or False, 坐标 or None
    """
    """检查图像中是否存在大于阈值的色块，并返回其坐标"""
    coordinates = np.argwhere(image_array > threshold)
    if coordinates.size > 0:
        return True, coordinates
    return False, None


def get_in_game():
    """
    判断是否在对局中
    :return: GDV.in_game(True or False)
    """
    start_time = time.time()
    _value = GDV.CACHE["config"]["ingram"]
    _img = take_screenshot(_value)
    res, coordinates = has_large_color_block(_img)
    if res:
        logger.info(f"当前正在对局中, 识别耗时: {time.time() - start_time:.2f}秒")
        GDV.in_game = True
    else:
        logger.info(f"当前未在对局中, 识别耗时: {time.time() - start_time:.2f}秒")
        GDV.in_game = False
    
# def posture_state_identification():
#     """ 判断当前的姿态 """
#     time.sleep(0.3)
#     take_full_screenshot()
#     start_time = time.time()
#     _value = GDV.CACHE["config"]["pose"]["pose"]
#     screenshot = get_specific_regin(GDV.global_screenshot, _value)

def posture_in_car():
    """
    判断当前是否在车内
    :return: GDV.in_car(True or False)
    """
    start_time = time.time()
    lists = [GDV.CACHE["config"]["car"]]
    _value = GDV.CACHE["config"]["car"]
    lists.append([_value[0] - 261, _value[1], _value[2], _value[3]])
    time.sleep(0.1)
    for v in lists:
        _img = take_screenshot(v)
        res, coordinates = has_large_color_block(_img)
        if res:
            logger.info(f"当前在车内, 识别耗时: {time.time() - start_time:.2f}秒")
            GDV.in_car = True
            return
    GDV.in_car = False
    logger.info(f"当前不在车内, 识别耗时: {time.time() - start_time:.2f}秒")
    return

if __name__ == '__main__':
    # weapon_identification()
    # print(GUNS_DATA)
    # print(backpack_identification())
    # print(weapon_position_identification("2"))
    print(current_weapon_identification())
