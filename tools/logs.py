#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import sys

from loguru import logger as loguru_logger
import os

from tools.paths import get_current_file_path, join_paths


class Log:
    def __init__(self, log_file='app.log'):
        # 创建 logs 目录（如果不存在）
        current_path = get_current_file_path()
        log_path = join_paths(current_path, 'logs')

        if not os.path.exists(log_path):
            os.makedirs(log_path)

        log_path = os.path.join(log_path, log_file)

        # 配置 loguru
        loguru_logger.add(
            log_path,
            level="ERROR",
            rotation="1 day",
            retention="7 days",
            encoding='utf-8'
        )

    @staticmethod
    def debug(message):
        loguru_logger.debug(message)

    @staticmethod
    def info(message):
        loguru_logger.info(message)

    @staticmethod
    def warning(message):
        loguru_logger.warning(message)

    @staticmethod
    def error(message):
        loguru_logger.error(message)

    @staticmethod
    def critical(message):
        loguru_logger.critical(message)


logger = Log()

if __name__ == "__main__":
    log = Log()  # 创建 Log 实例

    log.debug("这是一个调试消息")
    log.info("这是一个信息消息")
    log.warning("这是一个警告消息")
    log.error("这是一个错误消息")
    log.critical("这是一个严重错误消息")
