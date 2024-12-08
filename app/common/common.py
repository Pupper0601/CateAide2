#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import os

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QIcon
from PySide6.QtWidgets import QApplication, QMessageBox
from qfluentwidgets import Dialog, window

from libs.config import qq
from tools.logs import logger
from tools.paths import get_project_root, join_paths, object_join_path


def click_qq_group():
    # 发送 GET 请求
    url = QUrl(qq)
    QDesktopServices.openUrl(url)

    clipboard = QApplication.clipboard()  # 复制内容到剪切板
    clipboard.setText("679556431")

    w = Dialog("✅复制成功", "🐧QQ群号(679556431)已复制到剪切板", None)

    w.yesButton.setText("💃来啦老弟")
    w.cancelButton.setText("🤔我拒绝🤺")

    w.exec()


def get_gun_pressure_script():
    try:
        _script_path = object_join_path("script.lua")
        # 检查文件是否存在
        if not os.path.exists(_script_path):
            logger.error(f"Lua 文件不存在: {_script_path}")
            return None

        # 读取 Lua 文件内容
        with open(_script_path, 'r', encoding='utf-8') as file:
            lua_content = file.read()

        # 获取剪切板对象
        clipboard = QApplication.clipboard()
        # 将 Lua 文件内容复制到剪切板
        clipboard.setText(lua_content)

        # 可选：显示成功消息
        w = Dialog("✅复制成功", f"Lua 文件内容已复制到剪切板", None)
        w.yesButton.setText("请在罗技驱动中粘贴")
        w.cancelButton.hide()
        w.buttonLayout.insertStretch(1)

        w.exec()

    except Exception as e:
        # 处理异常
        w = Dialog("❌复制失败", f"无法读取 Lua 文件: {str(e)}", None)
        w.exec()
