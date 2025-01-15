# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'distance.ui'
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

class Ui_Distance(object):
    def setupUi(self, Distance):
        if not Distance.objectName():
            Distance.setObjectName(u"Distance")
        Distance.resize(120, 30)
        Distance.setMinimumSize(QSize(120, 30))
        Distance.setMaximumSize(QSize(120, 30))
        Distance.setStyleSheet(u"#Distance{\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(Distance)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 120, 30))
        self.widget.setMinimumSize(QSize(120, 30))
        self.widget.setMaximumSize(QSize(120, 30))
        self.widget.setStyleSheet(u"#widget{\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgba(214,214,214, 50);\n"
"	background-color: rgba(77, 90, 101,150);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleLabel = TitleLabel(self.widget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setMinimumSize(QSize(120, 30))
        self.TitleLabel.setMaximumSize(QSize(120, 30))
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.TitleLabel.setFont(font)
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
"	color: rgb(255, 0, 0);\n"
"	letter-spacing: 1px;\n"
"	font: 600;\n"
"}")
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.TitleLabel)

        Distance.setCentralWidget(self.centralwidget)

        self.retranslateUi(Distance)

        QMetaObject.connectSlotsByName(Distance)
    # setupUi

    def retranslateUi(self, Distance):
        Distance.setWindowTitle(QCoreApplication.translate("Distance", u"MainWindow", None))
        self.TitleLabel.setText(QCoreApplication.translate("Distance", u"9999.99", None))
    # retranslateUi

