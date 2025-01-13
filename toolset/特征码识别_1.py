#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import cv2

from libs.global_variables import GDV
from tools.logs import logger

def SIFT_image_visualization(image1, image2):

    # 转换为灰度图
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 创建SIFT检测器
    sift = cv2.SIFT_create()

    # 检测特征点和计算描述符
    keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

    # 创建BFMatcher对象
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    if descriptors1 is None or descriptors2 is None:
        return 0.0

    # 匹配描述符
    matches = bf.match(descriptors1, descriptors2)

    # 根据匹配结果进行排序
    matches = sorted(matches, key=lambda x: x.distance)

    # 计算相似度
    similarity = 0.0
    if len(keypoints1) > 0:
        matched_count = len(matches)  # 图2中包含的图1 特征点数量
        similarity = matched_count / len(keypoints1)  # 图1 特征点数量作为分母
        return similarity
    else:
        logger.error("图1没有检测到特征点，无法计算相似度。")
        return similarity

def SIFT_folders(binary_image, img):
    """
    遍历文件夹中的图片并进行SIFT处理
    :param binary_image: 需要遍历的文件夹名称
    :param img: 需要匹配的图片
    :return: 最佳匹配图片名称, 最佳匹配图片的相似度
    """
    best_similarity = 0
    best_match = None

    for key, value in GDV.CACHE["images"][binary_image].items():
        similarity = SIFT_image_visualization(value, img)
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = key

    return best_match, best_similarity

def SIFT_process_screenshot(key, value):
    """
    截取指定区域的图片并进行SIFT处理，返回与文件夹中图片的相似度最高的图片名称
    :param key: 需要遍历的文件夹名称
    :param value: 需要截取的区域, 格式为 (left, top, width, height)
    :return: 最佳匹配图片名称, 最佳匹配图片的相似度
    """
    screenshot = take_screenshot(value) # 截取指定区域的图片
    best_match, best_similarity = SIFT_folders(key, screenshot) # 获取最佳匹配图片
    return best_match, best_similarity
