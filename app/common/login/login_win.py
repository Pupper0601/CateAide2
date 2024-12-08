# app/common/login/login_win.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from PySide6.QtGui import Qt, QPainter, QBrush, QColor
from PySide6.QtWidgets import QMainWindow, QGraphicsBlurEffect, QWidget, QVBoxLayout
from PySide6.QtCore import QPoint
from BlurWindow.blurWindow import GlobalBlur

from app.common.common import click_qq_group
from app.view.login import Ui_LoginMainWindow


class LoginMainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login_ui = Ui_LoginMainWindow()
        self.login_ui.setupUi(self)
        self.setWindowTitle("CuteAide")

        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 添加毛玻璃效果
        GlobalBlur(self.winId(), Dark=True, QWidget=self)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0)")

        # ----------- 窗口拖动 -----------
        self.dragging = False
        self.offset = QPoint()

        self.slot()

    def slot(self):
        self.login_ui.PrimaryPushButton.clicked.connect(self.login_flow)
        self.login_ui.PushButton_2.clicked.connect(click_qq_group)

    def login_flow(self):
        return True

    # ----------- 窗口拖动 -----------
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.offset)
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
        return super().mouseReleaseEvent(event)
