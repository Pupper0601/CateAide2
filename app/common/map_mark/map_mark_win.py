#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com


import sys

from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout
from qfluentwidgets import DisplayLabel, ImageLabel


class MapMarkMainWin(QMainWindow):
    MapMarkShowSignal = Signal()
    MapMarkCloseSignal = Signal()
    MapUpSignal = Signal()
    MapDownSignal = Signal()

    def __init__(self):
        super().__init__()
        self._map = 0

        # 设置窗口大小
        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())

        # 创建中央小部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # 窗口置顶, 无任务栏图标
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        # 设置鼠标穿透
        self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.maps_list = [
            {   "name": "泰戈",
                "box": [(606, 156), (721, 158), (893,260), (1054,227), (586,356), (554,450), (1331,274), (1359,446),(1217,515),(1004,657), (1267,735),(1074,846),(1259,952),(740,854),(548,693)]
            },
            {   "name": "艾伦格",
                "box": [(602, 241), (764,292), (967,260), (1100,87), (1289,270), (614,468), (820,496), (1146,455),(590,733),(781,686), (1039,588),(1317,649),(1006,784),(858,890),(1173,893)]
                },
        ]

        self.init_slot()

    def init_slot(self):
        self.MapMarkShowSignal.connect(self.ui_show)
        self.MapMarkCloseSignal.connect(self.ui_close)
        self.MapUpSignal.connect(self.update_map_up)
        self.MapDownSignal.connect(self.update_map_down)

    def ui_show(self):
        self.update_mark()
        self.show()

    def ui_close(self):
        self.close()

    def update_map_up(self):
        if self._map < len(self.maps_list)-1:
            self._map += 1
            print(self._map)
            self.update_mark()

    def update_map_down(self):
        if self._map > 0:
            self._map -= 1
            print(self._map)
            self.update_mark()

    def update_mark(self):
        # 清除现有的标签
        for widget in self.findChildren(QLabel):
            widget.deleteLater()
        self.close()

        title = DisplayLabel(self)
        title.setText(self.maps_list[self._map]["name"])
        title.setStyleSheet("font-size: 50px; color: rgb(250,6,2); letter-spacing: 2px; font-family: "
                            "'Microsoft YaHei UI'; ")
        title.setMinimumSize(200, 100)
        title.move(10, 50)

        # 循环创建标签并设置位置
        for index, (x, y) in enumerate(self.maps_list[self._map]["box"]):
            image = ImageLabel(self)
            image.setImage(r"F:\Object\GitHub\CateAide2\app\resource\icon\precious.png")
            image.scaledToHeight(20)
            image.move(x-10, y-20)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapMarkMainWin()
    sys.exit(app.exec())
