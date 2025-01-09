# app/common/login/login_win.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from pathlib import Path

from PySide6.QtGui import QDesktopServices, Qt, QPainter, QBrush, QColor
from PySide6.QtWidgets import QMainWindow, QGraphicsBlurEffect, QWidget, QVBoxLayout
from PySide6.QtCore import QPoint, QUrl
from BlurWindow.blurWindow import GlobalBlur
from qfluentwidgets import Dialog

from app.common.common import click_qq_group
from app.common.login.login import code_verification, code_verify, email_verification
from app.view.login import Ui_LoginMainWindow
from libs.config import config_file_path
from libs.dialog import dialog
from tools.files import load_file, write_config


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
        self.login_ui.PushButton_2.clicked.connect(click_qq_group)
        self.login_ui.PushButton.clicked.connect(self.shopping_code)
        self.read_config()

    def login_flow(self):
        email = self.login_ui.LineEdit.text()
        login_code = self.login_ui.PasswordLineEdit.text()
        if email and login_code:
            if not email_verification(email):
                dialog("⚠️提示", "请输入正确格式的📬邮箱 !!!", cancel_hide=True)
                return False
            if not code_verification(login_code):
                dialog("⚠️提示", "🛅激活码 错误 或 已经过期, 请确认.", cancel_hide=True)
                return False
            if code_verify(email, login_code):
                write_config(f'{{"email": "{email}", "login_code": "{login_code}"}}')
                return True
        else:
            dialog("⚠️提示", "📬邮箱 或 🛅激活码 不能为空 !!!", cancel_hide=True)
            return False

    def read_config(self):
        if Path(config_file_path).exists():
            config = load_file(config_file_path)
            if config:
                self.login_ui.LineEdit.setText(config["email"])
                self.login_ui.PasswordLineEdit.setText(config["login_code"])

    def shopping_code(self):
        url = QUrl("https://pupperc.com")
        if not url.isValid():
            print("URL无效")
            return
        QDesktopServices.openUrl(url)

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
