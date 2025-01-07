#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from qfluentwidgets import Dialog



def dialog(title, content, yes_text="确定", cancel_text="取消", yes_hide=False, cancel_hide=False):
    """
    提示框, 有确定和取消按钮
    :param title:  标题
    :param content: 内容
    :param yes_text: 确定按钮文本
    :param cancel_text:  取消按钮文本
    :param yes_hide:  确定按钮隐藏
    :param cancel_hide:  取消按钮隐藏
    :return:
    """
    w = Dialog(title, content, None)
    w.yesButton.setText(yes_text)
    w.cancelButton.setText(cancel_text)

    if yes_hide:
        w.yesButton.hide()
        w.buttonLayout.insertStretch(0, 1)

    if cancel_hide:
        w.cancelButton.hide()
        w.buttonLayout.insertStretch(1)

    w.exec()