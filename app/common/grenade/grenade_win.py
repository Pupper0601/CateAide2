#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import sys

from PySide6.QtCore import QTimer, Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from app.view.grenade import Ui_Grenade
from libs.common import is_mouse_button_down
from libs.config import VK_LBUTTON
from libs.global_variables import GDV


class GrenadeMainWin(QMainWindow):
    ShowGrenadeSignal = Signal()
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

        self.init_slot()
        self.timer.timeout.connect(self.update_countdown)

    def init_slot(self):
        self.ShowGrenadeSignal.connect(self.ui_show)

    def start_countdown(self):
        if self.timer.isActive():
            self.timer.stop()
        self.time_left = 5  # 重置倒计时时间
        self.timer.start(92)  # 每秒触发一次

    def update_countdown(self):
        if self.time_left > 0.1:
            self.time_left -= 0.1
            self.ui.TitleLabel.setText(str(round(self.time_left, 1)))
            if not is_mouse_button_down(VK_LBUTTON):
                self.stop_timer()
        else:
            self.stop_timer()

    def stop_timer(self):
        self.timer.stop()
        self.ui.TitleLabel.setText("0.0")
        self.time_left = 5
        self.close()

    def ui_show(self):
        if GDV.grenade_state:
            self.show()
            self.start_countdown()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GrenadeMainWin()
    win.ShowGrenadeSignal.emit()

    sys.exit(app.exec())
