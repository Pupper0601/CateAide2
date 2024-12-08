#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import asyncio
import threading

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pynput import mouse

from libs.common import Worker
from libs.identification import start_weapon_identification, weapon_identification

import libs.global_variables as gv


class MouseMonitor:
    def __init__(self, window):
        self.monitoring = False
        self.listener = None
        self.window = window

    def start(self):
        self.monitoring = True
        # 初始化并启动鼠标监听器
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def stop(self):
        self.monitoring = False
        # 停止监听器
        if self.listener:
            self.listener.stop()

    def on_click(self, x, y, button, pressed):
        if self.monitoring:
            if pressed and button == mouse.Button.right and  gv.MOUSE_RIGHT_IDENTIFICATION:
                self.start_thread("right")


    def start_thread(self, key):
        # 创建一个工作对象
        worker = Worker(target_function=start_weapon_identification)
        # 连接`finished`信号到需要执行的函数
        worker.finished.connect(lambda: self.window.keyPressedSignal.emit(key))

        # 创建并启动线程
        thread = threading.Thread(target=worker.run)
        thread.start()


