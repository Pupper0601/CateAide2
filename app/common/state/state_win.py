#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from PySide6.QtGui import Qt, QPainter, QBrush, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsBlurEffect, QWidget, QVBoxLayout
from PySide6.QtCore import QPoint
from BlurWindow.blurWindow import GlobalBlur

from app.view.state import Ui_StateMainWindow


class StateMainWin(QMainWindow):
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

    def center_on_top(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # 获取屏幕大小
        screen_center = screen_geometry.center()  # 获取屏幕中心点
        frame_geometry = self.frameGeometry()  # 获取窗口大小
        frame_geometry.moveCenter(screen_center)
        frame_geometry.moveTop(0)  # 将窗口移动到屏幕顶部
        self.move(frame_geometry.topLeft())

    def init_slot(self):
        pass

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
