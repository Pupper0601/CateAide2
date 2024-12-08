#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pynput import mouse

from libs.identification import weapon_identification

import libs.global_variables as gv


class MouseMonitor:
    def __init__(self):
        self.monitoring = False
        self.listener = None

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
                weapon_identification()


