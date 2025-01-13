#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import sys

from PySide6.QtCore import QTimer
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from app.view.grenade import Ui_Grenade


class GrenadeMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Grenade()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.time_left = 5

        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # 窗口置顶, 无任务栏图标
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        # 设置鼠标穿透
        self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        # self.start_countdown()
        print("手雷窗口初始化完成")

    def start_countdown(self):
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(100)  # 每秒触发一次

    def update_countdown(self):
        if self.time_left > 0.1:
            self.time_left -= 0.1
            self.ui.TitleLabel.setText(str(round(self.time_left, 1)))
        else:
            self.timer.stop()
            self.ui.TitleLabel.setText("0.0")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GrenadeMainWin()
    win.show()
    sys.exit(app.exec())
