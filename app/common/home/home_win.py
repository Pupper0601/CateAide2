#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from PySide6.QtGui import QDesktopServices, QIcon, Qt, QPainter, QBrush, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsBlurEffect, QMessageBox, QWidget, QVBoxLayout
from PySide6.QtCore import QPoint, QUrl
from BlurWindow.blurWindow import GlobalBlur

from app.common.common import click_qq_group, get_gun_pressure_script
from app.view.home import Ui_HomeMainWindow
from app.common.state.state_win import StateMainWin
import resource_rc
from libs.keyboard import KeyboardMonitor
from libs.mouse import MouseMonitor
from tools.logs import logger
from tools.paths import object_join_path


class HomeMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomeMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("CuteAide")
        self.start_win = StateMainWin()

        self.keyboard_monitor = KeyboardMonitor(self.start_win)
        self.mouse_monitor = MouseMonitor(self.start_win)

        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ----------- 窗口拖动 -----------
        self.dragging = False
        self.offset = QPoint()

        # 添加毛玻璃效果
        GlobalBlur(self.winId(), Dark=True, QWidget=self)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0)")

        self.show_state()
        self.init_slot()

    def init_slot(self):
        self.ui.SwitchButton_3.checkedChanged.connect(self.show_state)
        self.ui.PushButton_2.clicked.connect(click_qq_group)
        self.ui.PushButton_3.clicked.connect(get_gun_pressure_script)
        self.ui.PushButton.clicked.connect(self.identification_control)

    def identification_control(self):
        # 识别控制
        if self.ui.PushButton.text() == " 开始压枪识别":
            self.ui.PushButton.setText(" 停止压枪识别")
            self.ui.PushButton.setIcon(QIcon(object_join_path("app/resource/icon/stop.png")))

            # 启动监控
            self.keyboard_monitor.start()
            self.mouse_monitor.start()
            logger.info("鼠标、键盘监控已启动")
        else:
            self.ui.PushButton.setText(" 开始压枪识别")
            self.ui.PushButton.setIcon(QIcon(object_join_path("app/resource/icon/start.png")))

            # 停止监控
            self.keyboard_monitor.stop()
            self.mouse_monitor.stop()
            logger.info("鼠标、键盘监控已停止")

    def show_state(self):
        # 显示/隐藏状态窗口
        if self.ui.SwitchButton_3.isChecked():
            self.start_win.show()
        else:
            self.start_win.close()

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
