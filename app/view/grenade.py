# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grenade.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QWidget)

from qfluentwidgets import TitleLabel

class Ui_Grenade(object):
    def setupUi(self, Grenade):
        if not Grenade.objectName():
            Grenade.setObjectName(u"Grenade")
        Grenade.resize(94, 30)
        Grenade.setMinimumSize(QSize(50, 30))
        Grenade.setMaximumSize(QSize(94, 30))
        Grenade.setStyleSheet(u"#Grenade{\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(Grenade)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(50, 30))
        self.centralwidget.setMaximumSize(QSize(50, 30))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(150, 150, 50, 30))
        self.widget.setMinimumSize(QSize(50, 30))
        self.widget.setMaximumSize(QSize(50, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleLabel = TitleLabel(self.centralwidget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(0, 0, 50, 30))
        self.TitleLabel.setMinimumSize(QSize(50, 30))
        self.TitleLabel.setMaximumSize(QSize(50, 30))
        self.TitleLabel.setStyleSheet(u"FluentLabelBase {\n"
"    color: black;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#000000}\n"
"\n"
"#TitleLabel{\n"
"	border: none;\n"
"	color: rgb(255, 64, 0);\n"
"}")
        self.TitleLabel.setAlignment(Qt.AlignCenter)
        Grenade.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grenade)

        QMetaObject.connectSlotsByName(Grenade)
    # setupUi

    def retranslateUi(self, Grenade):
        Grenade.setWindowTitle(QCoreApplication.translate("Grenade", u"MainWindow", None))
        self.TitleLabel.setText(QCoreApplication.translate("Grenade", u"5.5", None))
    # retranslateUi

