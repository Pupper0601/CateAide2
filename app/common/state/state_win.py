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
from libs.global_variables import GDV
from libs.config import debug
from tools.logs import logger


class StateMainWin(QMainWindow):
    Right_PressedSignal = Signal()  # 定义信号
    Left_StateSignal = Signal()
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
        self.Left_StateSignal.connect(self.update_shooting_state)
        self.Right_PressedSignal.connect(self.update_window_info)
        self.ui.label.setStyleSheet("font-size: 12px; color: rgb(237,237,239); letter-spacing: 1.5px; font-family: "
                                    "'Microsoft YaHei UI'; ")
        self.ui.label.setText("👏 欢迎使用 CateAide2")
        self.ui.label_2.setStyleSheet("font-size: 12px; color: rgb(237,237,239); letter-spacing: 1.5px; font-family: "
                                      "'Microsoft YaHei UI'; ")
        self.ui.label_2.setText("使用中有任何问题在QQ群反馈: 679556431")

    def update_window_info(self):
        _str = ""
        _gun_info = None
        if len(GDV.guns_data) == 0:
            self.update_shooting_state()
            return

        key = GDV.current_weapon
        if GDV.guns_data[key]["weapon"][1] != "weapon_none":
            _gun_info = GDV.guns_data[key]
        elif GDV.guns_data["1" if key == "2" else "2"]["weapon"][1] != "weapon_none":
            _gun_info = GDV.guns_data["1" if key == "2" else "2"]
            GDV.current_weapon = "1" if key == "2" else "2"
        else:
            self.update_shooting_state()
            return

        for _key, _value in _gun_info.items():
            if _key == "weapon":
                _str += f"武器: [{_value[0]}]"
            elif "无" not in _value[0]:
                _str += f", {_value[0]}"
        self.ui.label_2.setText(_str)
        GDV.current_weapon_info = _gun_info

        self.update_shooting_state()

    def update_shooting_state(self):
        _str = GDV.state_left_info

        if GDV.in_car:
            _str += ", <车内>"
        else:
            if GDV.posture_state == "zhan":
                _str += ", <站姿>"
            elif GDV.posture_state == "dun":
                _str += ", <蹲姿>"
            elif GDV.posture_state == "pa":
                _str += ", <趴姿>"

        if GDV.shooting_state:
            _str += ", [压枪]"
        else:
            _str += ", [暂停]"
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
