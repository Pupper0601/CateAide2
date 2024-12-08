import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from app.common.login.login_win import LoginMainWin
from app.common.home.home_win import HomeMainWin


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


app = QApplication(sys.argv)
window = MainWin()
sys.exit(app.exec())
