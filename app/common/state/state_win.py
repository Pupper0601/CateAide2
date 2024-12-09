#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import asyncio

from PySide6.QtGui import Qt, QPainter, QBrush, QColor
from PySide6.QtWidgets import QApplication, QGraphicsDropShadowEffect, QMainWindow, QGraphicsBlurEffect, QWidget, \
    QVBoxLayout
from PySide6.QtCore import QPoint
from BlurWindow.blurWindow import GlobalBlur
from PySide6.QtCore import Signal

from app.view.state import Ui_StateMainWindow
import libs.global_variables as gv
from libs.config import debug
from tools.logs import logger


class StateMainWin(QMainWindow):
    keyPressedSignal = Signal(str)  # 定义信号
    shootingSignal = Signal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_StateMainWindow()
        self.ui.setupUi(self)

        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # 窗口置顶, 无任务栏图标
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        # 设置鼠标穿透
        self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        # # ----------- 窗口拖动 -----------
        # self.dragging = False
        # self.offset = QPoint()

        # 将窗口置于屏幕顶部居中
        self.center_on_top()
        self.init_slot()

    def center_on_top(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # 获取屏幕大小
        screen_center = screen_geometry.center()  # 获取屏幕中心点
        frame_geometry = self.frameGeometry()  # 获取窗口大小
        frame_geometry.moveCenter(screen_center)
        frame_geometry.moveTop(0)  # 将窗口移动到屏幕顶部
        self.move(frame_geometry.topLeft())

    def init_slot(self):
        # 连接信号到槽
        self.shootingSignal.connect(self.update_shooting_state)
        self.keyPressedSignal.connect(self.update_window_info)
        self.ui.label.setStyleSheet("font-size: 12px; color: white; letter-spacing: 1.5px; ")
        self.ui.label_2.setStyleSheet("font-size: 12px; color: white; letter-spacing: 1.5px; ")

    def update_window_info(self, key):
        _str = ""
        _gun_info = None
        if len(gv.GUNS_DATA) <= 0:
            self.ui.label_2.setText("未获取到枪械信息")
            gv.shooting_state = False
            return

        if debug:
            logger.info(f"当前武器为 {gv.CURRENT_WEAPON}")

        if key not in ("1", "2"):
            if gv.GUNS_DATA[gv.CURRENT_WEAPON]["weapon"][1] != "weapon_none":
                _gun_info = gv.GUNS_DATA[gv.CURRENT_WEAPON]
            elif gv.GUNS_DATA["1" if gv.CURRENT_WEAPON == "2" else "2"]["weapon"][1] != "weapon_none":
                _gun_info = gv.GUNS_DATA["1" if gv.CURRENT_WEAPON == "2" else "2"]
                gv.CURRENT_WEAPON = "1" if gv.CURRENT_WEAPON == "2" else "2"
            else:
                self.ui.label_2.setText("未获取到枪械信息")
                gv.shooting_state = False
                return
        else:
            if gv.GUNS_DATA[key]["weapon"][1] != "weapon_none":
                _gun_info = gv.GUNS_DATA[key]
                gv.CURRENT_WEAPON = key
            elif gv.GUNS_DATA["1" if key == "2" else "2"]["weapon"][1] != "weapon_none":
                _gun_info = gv.GUNS_DATA["1" if key == "2" else "2"]
                gv.CURRENT_WEAPON = "1" if key == "2" else "2"
            else:
                self.ui.label_2.setText("未获取到枪械信息")
                gv.shooting_state = False
                return

        for _key, _value in _gun_info.items():
            if _key == "weapon":
                _str += f"[{_value[0]}]"
            elif "无" not in _value[0]:
                _str += f", {_value[0]}"
        self.ui.label_2.setText(_str)
        gv.shooting_state = True
        self.ui.label.setText("枪械识别已经完成, 开始压枪")

    def update_shooting_state(self, _str):
        self.ui.label.setText(_str)


    # # ----------- 窗口拖动 -----------
    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.dragging = True
    #         self.offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
    #     return super().mousePressEvent(event)
    #
    # def mouseMoveEvent(self, event):
    #     if self.dragging:
    #         self.move(event.globalPosition().toPoint() - self.offset)
    #     return super().mouseMoveEvent(event)
    #
    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.dragging = False
    #     return super().mouseReleaseEvent(event)
