#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import math
import sys

from PySide6.QtCore import Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from app.view.distance import Ui_Distance
from libs.common import is_mouse_button_down
from libs.config import VK_LBUTTON
from libs.global_variables import GDV


class DistanceMainWin(QMainWindow):
    UpdateCoordinateSignal = Signal(tuple)
    EnlargeSignal = Signal(int)
    ShowDistanceSignal = Signal()
    CloneDistanceSignal = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Distance()
        self.ui.setupUi(self)
        self.coefficient_lists = [0.135, 0.283, 0.54, 1.08, 2.16]
        self.enlarge = 0
        self.coordinate_list = []

        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # 窗口置顶, 无任务栏图标
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        # 设置鼠标穿透
        self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.init_slot()

    def center_on_top(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # 获取屏幕大小
        screen_center = screen_geometry.center()  # 获取屏幕中心点
        frame_geometry = self.frameGeometry()  # 获取窗口大小
        frame_geometry.moveCenter(screen_center)    # 将窗口移动到屏幕中心
        frame_geometry.moveTop(300)  # 将窗口移动到屏幕顶部
        self.move(frame_geometry.topLeft()) # 移动窗口

    def init_slot(self):
        self.ShowDistanceSignal.connect(self.ui_show)
        self.CloneDistanceSignal.connect(self.ui_clone)
        self.EnlargeSignal.connect(self.update_enlarge)
        self.UpdateCoordinateSignal.connect(self.update_coordinate)

    def update_coordinate(self, coordinate):
        self.coordinate_list.append(coordinate)

    def ui_show(self):
        if len(self.coordinate_list) > 1:
            point1 = self.coordinate_list[0]
            point2 = self.coordinate_list[-1]
            distance = round(self.calculate_distance(point1, point2) / self.coefficient_lists[self.enlarge])
            self.ui.TitleLabel.setText(f'{distance}米')
            self.show()

    def ui_clone(self):
        self.coordinate_list.clear()
        self.is_showing = False  # 重置标志位
        self.close()

    @staticmethod
    def calculate_distance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def update_enlarge(self, dy):
        if dy > 0:
            if self.enlarge < 4:
                self.enlarge = self.enlarge + 1
        else:
            if self.enlarge > 0:
                self.enlarge = self.enlarge - 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DistanceMainWin()
    win.ShowDistanceSignal.emit()

    sys.exit(app.exec())
