# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'state.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QWidget)

class Ui_StateMainWindow(object):
    def setupUi(self, StateMainWindow):
        if not StateMainWindow.objectName():
            StateMainWindow.setObjectName(u"StateMainWindow")
        StateMainWindow.resize(750, 20)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StateMainWindow.sizePolicy().hasHeightForWidth())
        StateMainWindow.setSizePolicy(sizePolicy)
        StateMainWindow.setMinimumSize(QSize(750, 20))
        StateMainWindow.setMaximumSize(QSize(750, 20))
        self.centralwidget = QWidget(StateMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 750, 20))
        self.widget.setMinimumSize(QSize(750, 20))
        self.widget.setMaximumSize(QSize(750, 20))
        self.widget.setStyleSheet(u"#widget{\n"
"	border: 1px solid rgba(214,214,214, 50);\n"
"	background-color: rgba(173, 173, 173,100);\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"Line{\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 20))
        self.frame.setMaximumSize(QSize(16777215, 20))
        self.frame.setStyleSheet(u"#frame{\n"
"	border: none;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setStyleSheet(u"#label{\n"
"	\n"
"	color: rgb(220, 220, 220);\n"
"	font: 500 7pt;\n"
"\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 15))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 20))
        self.frame_2.setMaximumSize(QSize(16777215, 20))
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	border: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"#label_2{\n"
"	\n"
"	color: rgb(220, 220, 220);\n"
"	font: 500 7pt;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_2)

        StateMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StateMainWindow)

        QMetaObject.connectSlotsByName(StateMainWindow)
    # setupUi

    def retranslateUi(self, StateMainWindow):
        StateMainWindow.setWindowTitle(QCoreApplication.translate("StateMainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
    # retranslateUi

