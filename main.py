import ctypes
import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from app.common.login.login_win import LoginMainWin
from app.common.home.home_win import HomeMainWin

def run_as_admin():
    """
    检查当前脚本是否已以管理员权限运行。如果未以管理员权限运行，
    则重新以管理员权限启动脚本。
    """
    try:
        # 检查是否具有管理员权限
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False

    if not is_admin:
        # 如果没有管理员权限，则重新启动脚本并要求以管理员身份运行
        try:
            # 获取当前脚本的路径
            script = sys.executable
            params = " ".join([f'"{arg}"' for arg in sys.argv])
            # 使用 ShellExecuteEx 方法启动管理员权限的进程
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", script, params, None, 1
            )
        except Exception as e:
            print("运行需要管理员权限！", e)
        # 程序退出以避免后续代码被非管理员权限执行
        sys.exit()


# 应用管理员检测
run_as_admin()


class MainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login_win = LoginMainWin()
        self.login_win.show()
        self.home_win = HomeMainWin()

        self.init_slot()

    def init_slot(self):
        self.login_win.login_ui.PrimaryPushButton.clicked.connect(self.show_home)

    def show_home(self):
        if self.login_win.login_flow():
            self.home_win.show()
            self.login_win.close()

run_as_admin()
app = QApplication(sys.argv)
window = MainWin()
sys.exit(app.exec())
