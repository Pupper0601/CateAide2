# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (PushButton, RadioButton, StrongBodyLabel, SwitchButton)
import resource_rc

class Ui_HomeMainWindow(object):
    def setupUi(self, HomeMainWindow):
        if not HomeMainWindow.objectName():
            HomeMainWindow.setObjectName(u"HomeMainWindow")
        HomeMainWindow.resize(600, 400)
        HomeMainWindow.setMinimumSize(QSize(600, 400))
        HomeMainWindow.setMaximumSize(QSize(600, 400))
        icon = QIcon()
        icon.addFile(u":/images/resource/images/log.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        HomeMainWindow.setWindowIcon(icon)
        HomeMainWindow.setStyleSheet(u"#HomeMainWindow{\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}")
        HomeMainWindow.setAnimated(False)
        HomeMainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(HomeMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 600, 400))
        self.widget.setMinimumSize(QSize(600, 400))
        self.widget.setMaximumSize(QSize(600, 400))
        self.widget.setStyleSheet(u"#widget{\n"
"	border-radius: 10px;\n"
"	border: 1px solid rbg(0,0,0);\n"
"	background: rgba(255, 255, 255, 0);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setStyleSheet(u"#widget_5{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.widget_5)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setMinimumSize(QSize(0, 40))
        self.frame_16.setStyleSheet(u"#frame_16{\n"
"	border: none;\n"
"	border-top-left-radius: 10px;\n"
"}")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_5 = QPushButton(self.frame_16)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"#pushButton_5{\n"
"	border: none;\n"
"	\n"
"	color: rgb(85, 0, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/app/resource/icon/versrion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(False)

        self.horizontalLayout_7.addWidget(self.pushButton_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_4.addWidget(self.frame_16)

        self.frame_18 = QFrame(self.widget_5)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setMinimumSize(QSize(0, 40))
        self.frame_18.setStyleSheet(u"#frame_18{\n"
"	border: none;\n"
"}")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"#label_18{\n"
"	font: 700 18pt \"\u9ed1\u4f53\";\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"	color: rgb(255, 105, 5);\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_18)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_4.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.widget_5)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy2)
        self.frame_17.setMinimumSize(QSize(0, 40))
        self.frame_17.setStyleSheet(u"#frame_17{\n"
"	border: none;\n"
"	border-top-right-radius:10px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.pushButton_4 = QPushButton(self.frame_17)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(20, 20))
        self.pushButton_4.setMaximumSize(QSize(20, 20))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(4, 51, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/app/resource/icon/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_17)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setMaximumSize(QSize(20, 20))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(4, 51, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/app/resource/icon/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addWidget(self.frame_17)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(8)
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.widget_6.setStyleSheet(u"#widget_6{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_6)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_6)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.widget_2)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy2.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy2)
        self.frame_15.setStyleSheet(u"#frame_15{\n"
"	border: none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_15)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 5, 5, 5)
        self.frame_3 = QFrame(self.frame_15)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 25))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_16 = QSpacerItem(22, 22, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.StrongBodyLabel_7 = StrongBodyLabel(self.frame_3)
        self.StrongBodyLabel_7.setObjectName(u"StrongBodyLabel_7")
        self.StrongBodyLabel_7.setStyleSheet(u"FluentLabelBase {\n"
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
"#StrongBodyLabel_7{\n"
"	color: rgb(255, 112, 16);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")

        self.horizontalLayout_15.addWidget(self.StrongBodyLabel_7)

        self.horizontalSpacer_29 = QSpacerItem(23, 22, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_29)

        self.StrongBodyLabel_8 = StrongBodyLabel(self.frame_3)
        self.StrongBodyLabel_8.setObjectName(u"StrongBodyLabel_8")
        self.StrongBodyLabel_8.setStyleSheet(u"FluentLabelBase {\n"
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
"#StrongBodyLabel_8{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"	color: rgb(255, 67, 34);\n"
"}")

        self.horizontalLayout_15.addWidget(self.StrongBodyLabel_8)

        self.horizontalSpacer_28 = QSpacerItem(22, 22, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_28)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_15)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 1666777))
        self.frame.setStyleSheet(u"#frame{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy5)
        self.frame_8.setMinimumSize(QSize(0, 25))
        self.frame_8.setMaximumSize(QSize(16777215, 32))
        self.frame_8.setStyleSheet(u"#frame_8{\n"
"	border: nome;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.StrongBodyLabel = StrongBodyLabel(self.frame_8)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setStyleSheet(u"FluentLabelBase {\n"
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
"#StrongBodyLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 158, 23);\n"
"}")

        self.horizontalLayout_2.addWidget(self.StrongBodyLabel)

        self.horizontalSpacer_7 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.StrongBodyLabel_2 = StrongBodyLabel(self.frame_8)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        self.StrongBodyLabel_2.setMinimumSize(QSize(120, 0))
        self.StrongBodyLabel_2.setStyleSheet(u"FluentLabelBase {\n"
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
"#StrongBodyLabel_2{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 98, 25);\n"
"}")

        self.horizontalLayout_2.addWidget(self.StrongBodyLabel_2)

        self.horizontalSpacer_38 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_38)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.frame_31 = QFrame(self.frame)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy5.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy5)
        self.frame_31.setMinimumSize(QSize(0, 25))
        self.frame_31.setMaximumSize(QSize(16777215, 32))
        self.frame_31.setStyleSheet(u"#frame_31{\n"
"	border: nome;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.StrongBodyLabel_5 = StrongBodyLabel(self.frame_31)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")
        self.StrongBodyLabel_5.setStyleSheet(u"FluentLabelBase {\n"
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
"#StrongBodyLabel_5{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 158, 23);\n"
"}")

        self.horizontalLayout_3.addWidget(self.StrongBodyLabel_5)

        self.horizontalSpacer_12 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_12)

        self.StrongBodyLabel_6 = StrongBodyLabel(self.frame_31)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        self.StrongBodyLabel_6.setMinimumSize(QSize(120, 0))
        self.StrongBodyLabel_6.setStyleSheet(u"FluentLabelBase {\n"
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
"#StrongBodyLabel_6{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 98, 25);\n"
"}")

        self.horizontalLayout_3.addWidget(self.StrongBodyLabel_6)

        self.horizontalSpacer_63 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_63)


        self.verticalLayout_11.addWidget(self.frame_31)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_5 = QFrame(self.frame_15)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(3)
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 4, 10, 4)
        self.RadioButton_2 = RadioButton(self.frame_5)
        self.RadioButton_2.setObjectName(u"RadioButton_2")
        self.RadioButton_2.setChecked(True)

        self.verticalLayout_2.addWidget(self.RadioButton_2)

        self.RadioButton_4 = RadioButton(self.frame_5)
        self.RadioButton_4.setObjectName(u"RadioButton_4")
        self.RadioButton_4.setChecked(False)

        self.verticalLayout_2.addWidget(self.RadioButton_4)

        self.RadioButton_19 = RadioButton(self.frame_5)
        self.RadioButton_19.setObjectName(u"RadioButton_19")
        self.RadioButton_19.setCheckable(True)
        self.RadioButton_19.setChecked(False)

        self.verticalLayout_2.addWidget(self.RadioButton_19)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMaximumSize(QSize(16777215, 55))
        self.frame_20.setStyleSheet(u"#frame_20{\n"
"	border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.PushButton = PushButton(self.frame_20)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setMinimumSize(QSize(260, 40))
        self.PushButton.setMaximumSize(QSize(260, 16777215))
        self.PushButton.setStyleSheet(u"#PushButton{	\n"
"	font:700 16pt \"\u9ed1\u4f53\";\n"
"	color: rgb(255, 255, 255);\n"
"	background: rgb(0, 159, 170);\n"
"}\n"
"#PushButton:hover{	\n"
"	font:700 16pt \"\u9ed1\u4f53\";\n"
"	color: rgb(255, 255, 255);\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 75, 15), stop:1 rgb(38, 255, 208));\n"
"}\n"
"\n"
"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"PushButton[isPlaceholderText=true] {\n"
"    color: rgba(0, 0, 0, 0.6063);\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6p"
                        "x 36px;\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5px 31px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover, ToolButton:hover, ToggleButton:hover, ToggleToolButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rg"
                        "ba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled {\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    "
                        "border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
"    bor"
                        "der: none;\n"
"    border-radius: 6px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=false] {\n"
"    padding: 6px 12px 6px 12px;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=true] {\n"
"    padding: 6px 12px 6px 36px;\n"
"}\n"
"\n"
"HyperlinkButton:hover {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.43);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"RadioButton {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    background-color: transparent;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"    color: black;\n"
"}\n"
"\n"
"RadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #999999;\n"
"    background-co"
                        "lor: rgba(0, 0, 0, 5);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"RadioButton::indicator:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"RadioButton::indicator:pressed {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(225, 224, 223),\n"
"            stop:1 rgb(225, 224, 223));\n"
"}\n"
"\n"
"RadioButton::indicator:checked {\n"
"    height: 22px;\n"
"    width: 22px;\n"
"    border: none;\n"
"    border-radius: 11px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0"
                        ".5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"RadioButton::indicator:disabled {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RadioButton::indicator:disabled:checked {\n"
"    border: none;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
"            stop:1 rgba(0, 0"
                        ", 0, 0.2169));\n"
"}\n"
"\n"
"TransparentToolButton,\n"
"TransparentToggleToolButton,\n"
"TransparentDropDownToolButton,\n"
"TransparentPushButton,\n"
"TransparentDropDownPushButton,\n"
"TransparentTogglePushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"TransparentToolButton:hover,\n"
"TransparentToggleToolButton:hover,\n"
"TransparentDropDownToolButton:hover,\n"
"TransparentPushButton:hover,\n"
"TransparentDropDownPushButton:hover,\n"
"TransparentTogglePushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:pressed,\n"
"TransparentToggleToolButton:pressed,\n"
"TransparentDropDownToolButton:pressed,\n"
"TransparentPushButton:pressed,\n"
"TransparentDropDownPushButton:pressed,\n"
"TransparentTogglePushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:disabled,\n"
"TransparentToggleToolButton:d"
                        "isabled,\n"
"TransparentDropDownToolButton:disabled,\n"
"TransprentPushButton:disabled,\n"
"TransparentDropDownPushButton:disabled,\n"
"TransprentTogglePushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"PillPushButton,\n"
"PillPushButton:hover,\n"
"PillPushButton:pressed,\n"
"PillPushButton:disabled,\n"
"PillPushButton:checked,\n"
"PillPushButton:checked:hover,\n"
"PillPushButton:checked:pressed,\n"
"PillPushButton:disabled:checked,\n"
"PillToolButton,\n"
"PillToolButton:hover,\n"
"PillToolButton:pressed,\n"
"PillToolButton:disabled,\n"
"PillToolButton:checked,\n"
"PillToolButton:checked:hover,\n"
"PillToolButton:checked:pressed,\n"
"PillToolButton:disabled:checked {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/app/resource/icon/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PushButton.setIcon(icon4)
        self.PushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.PushButton)

        self.horizontalSpacer_2 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.frame_20)

        self.frame_25 = QFrame(self.frame_15)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMinimumSize(QSize(0, 40))
        self.frame_25.setMaximumSize(QSize(16777215, 50))
        self.frame_25.setStyleSheet(u"#frame_25{\n"
"	border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_12.setSpacing(1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 5, 0, 5)
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_25)

        self.PushButton_7 = PushButton(self.frame_25)
        self.PushButton_7.setObjectName(u"PushButton_7")
        icon5 = QIcon()
        icon5.addFile(u":/icon/app/resource/icon/qq.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PushButton_7.setIcon(icon5)

        self.horizontalLayout_12.addWidget(self.PushButton_7)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_26)

        self.PushButton_8 = PushButton(self.frame_25)
        self.PushButton_8.setObjectName(u"PushButton_8")
        self.PushButton_8.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/icon/app/resource/icon/floating.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PushButton_8.setIcon(icon6)
        self.PushButton_8.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.PushButton_8)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_27)


        self.verticalLayout_4.addWidget(self.frame_25)


        self.horizontalLayout_13.addWidget(self.frame_15)

        self.frame_24 = QFrame(self.widget_2)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy2.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy2)
        self.frame_24.setStyleSheet(u"#frame_24{\n"
"	border: none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_24)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 10, 5)
        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy6.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy6)
        self.frame_27.setMinimumSize(QSize(0, 0))
        self.frame_27.setMaximumSize(QSize(16777215, 16777215))
        self.frame_27.setStyleSheet(u"#frame_27{\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame_27)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy7)
        self.frame_28.setStyleSheet(u"#frame_28{\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_53 = QSpacerItem(1, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_53)

        self.RadioButton_13 = RadioButton(self.frame_28)
        self.RadioButton_13.setObjectName(u"RadioButton_13")
        self.RadioButton_13.setChecked(True)

        self.horizontalLayout_24.addWidget(self.RadioButton_13)

        self.horizontalSpacer_54 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_54)

        self.RadioButton_14 = RadioButton(self.frame_28)
        self.RadioButton_14.setObjectName(u"RadioButton_14")

        self.horizontalLayout_24.addWidget(self.RadioButton_14)

        self.horizontalSpacer_55 = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_55)


        self.verticalLayout_6.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy7.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy7)
        self.frame_29.setStyleSheet(u"#frame_29{\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_56 = QSpacerItem(1, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_56)

        self.RadioButton_15 = RadioButton(self.frame_29)
        self.RadioButton_15.setObjectName(u"RadioButton_15")
        self.RadioButton_15.setChecked(True)

        self.horizontalLayout_25.addWidget(self.RadioButton_15)

        self.horizontalSpacer_57 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_57)

        self.RadioButton_16 = RadioButton(self.frame_29)
        self.RadioButton_16.setObjectName(u"RadioButton_16")

        self.horizontalLayout_25.addWidget(self.RadioButton_16)

        self.horizontalSpacer_58 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_58)


        self.verticalLayout_6.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy8)
        self.frame_30.setMaximumSize(QSize(16777215, 40))
        self.frame_30.setStyleSheet(u"#frame_30{\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_59 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_59)

        self.SwitchButton_9 = SwitchButton(self.frame_30)
        self.SwitchButton_9.setObjectName(u"SwitchButton_9")
        self.SwitchButton_9.setChecked(True)

        self.horizontalLayout_26.addWidget(self.SwitchButton_9)

        self.horizontalSpacer_72 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_72)

        self.SwitchButton_8 = SwitchButton(self.frame_30)
        self.SwitchButton_8.setObjectName(u"SwitchButton_8")
        self.SwitchButton_8.setEnabled(True)

        self.horizontalLayout_26.addWidget(self.SwitchButton_8)

        self.horizontalSpacer_60 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_60)

        self.horizontalSpacer_61 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_61)


        self.verticalLayout_6.addWidget(self.frame_30)


        self.verticalLayout_5.addWidget(self.frame_27)

        self.frame_2 = QFrame(self.frame_24)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy6.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy6)
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	border: 1px solid rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setSpacing(1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.frame_32 = QFrame(self.frame_2)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy8.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy8)
        self.frame_32.setMaximumSize(QSize(16777215, 40))
        self.frame_32.setStyleSheet(u"#frame_32{\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_62 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_62)

        self.SwitchButton_10 = SwitchButton(self.frame_32)
        self.SwitchButton_10.setObjectName(u"SwitchButton_10")
        self.SwitchButton_10.setEnabled(False)

        self.horizontalLayout_27.addWidget(self.SwitchButton_10)

        self.horizontalSpacer_64 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_64)

        self.SwitchButton_11 = SwitchButton(self.frame_32)
        self.SwitchButton_11.setObjectName(u"SwitchButton_11")
        self.SwitchButton_11.setEnabled(False)
        self.SwitchButton_11.setChecked(False)

        self.horizontalLayout_27.addWidget(self.SwitchButton_11)

        self.horizontalSpacer_65 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_65)


        self.verticalLayout_10.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_2)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy8.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy8)
        self.frame_33.setMaximumSize(QSize(16777215, 40))
        self.frame_33.setStyleSheet(u"#frame_33{\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_66 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_66)

        self.SwitchButton_12 = SwitchButton(self.frame_33)
        self.SwitchButton_12.setObjectName(u"SwitchButton_12")
        self.SwitchButton_12.setEnabled(False)

        self.horizontalLayout_28.addWidget(self.SwitchButton_12)

        self.horizontalSpacer_67 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_67)

        self.SwitchButton_13 = SwitchButton(self.frame_33)
        self.SwitchButton_13.setObjectName(u"SwitchButton_13")
        self.SwitchButton_13.setEnabled(False)
        self.SwitchButton_13.setChecked(False)

        self.horizontalLayout_28.addWidget(self.SwitchButton_13)

        self.horizontalSpacer_68 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_68)


        self.verticalLayout_10.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_2)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy8.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy8)
        self.frame_34.setMaximumSize(QSize(16777215, 40))
        self.frame_34.setStyleSheet(u"#frame_34{\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_69 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_69)

        self.SwitchButton_14 = SwitchButton(self.frame_34)
        self.SwitchButton_14.setObjectName(u"SwitchButton_14")
        self.SwitchButton_14.setEnabled(False)

        self.horizontalLayout_29.addWidget(self.SwitchButton_14)

        self.horizontalSpacer_70 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_70)

        self.SwitchButton_15 = SwitchButton(self.frame_34)
        self.SwitchButton_15.setObjectName(u"SwitchButton_15")
        self.SwitchButton_15.setEnabled(False)
        self.SwitchButton_15.setChecked(False)

        self.horizontalLayout_29.addWidget(self.SwitchButton_15)

        self.horizontalSpacer_71 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_71)


        self.verticalLayout_10.addWidget(self.frame_34)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy4.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy4)
        self.frame_26.setMaximumSize(QSize(16777215, 55))
        self.frame_26.setStyleSheet(u"#frame_26{\n"
"	border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.PushButton_2 = PushButton(self.frame_26)
        self.PushButton_2.setObjectName(u"PushButton_2")
        self.PushButton_2.setEnabled(False)
        self.PushButton_2.setMinimumSize(QSize(260, 40))
        self.PushButton_2.setMaximumSize(QSize(260, 16777215))
        self.PushButton_2.setStyleSheet(u"#PushButton_2{	\n"
"	font:700 16pt \"\u9ed1\u4f53\";\n"
"	color: rgb(255, 255, 255);\n"
"	background: rgb(0, 159, 170);\n"
"}\n"
"#PushButton_2:hover{	\n"
"	font:700 16pt \"\u9ed1\u4f53\";\n"
"	color: rgb(255, 255, 255);\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 75, 15), stop:1 rgb(38, 255, 208));\n"
"}\n"
"\n"
"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"PushButton[isPlaceholderText=true] {\n"
"    color: rgba(0, 0, 0, 0.6063);\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12p"
                        "x 6px 36px;\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5px 31px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover, ToolButton:hover, ToggleButton:hover, ToggleToolButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px soli"
                        "d rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled {\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
""
                        "    border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
"   "
                        " border: none;\n"
"    border-radius: 6px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=false] {\n"
"    padding: 6px 12px 6px 12px;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=true] {\n"
"    padding: 6px 12px 6px 36px;\n"
"}\n"
"\n"
"HyperlinkButton:hover {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.43);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"RadioButton {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    background-color: transparent;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"    color: black;\n"
"}\n"
"\n"
"RadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #999999;\n"
"    backgroun"
                        "d-color: rgba(0, 0, 0, 5);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"RadioButton::indicator:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"RadioButton::indicator:pressed {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(225, 224, 223),\n"
"            stop:1 rgb(225, 224, 223));\n"
"}\n"
"\n"
"RadioButton::indicator:checked {\n"
"    height: 22px;\n"
"    width: 22px;\n"
"    border: none;\n"
"    border-radius: 11px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radi"
                        "us:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"RadioButton::indicator:disabled {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RadioButton::indicator:disabled:checked {\n"
"    border: none;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
"            stop:1 rgba("
                        "0, 0, 0, 0.2169));\n"
"}\n"
"\n"
"TransparentToolButton,\n"
"TransparentToggleToolButton,\n"
"TransparentDropDownToolButton,\n"
"TransparentPushButton,\n"
"TransparentDropDownPushButton,\n"
"TransparentTogglePushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"TransparentToolButton:hover,\n"
"TransparentToggleToolButton:hover,\n"
"TransparentDropDownToolButton:hover,\n"
"TransparentPushButton:hover,\n"
"TransparentDropDownPushButton:hover,\n"
"TransparentTogglePushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:pressed,\n"
"TransparentToggleToolButton:pressed,\n"
"TransparentDropDownToolButton:pressed,\n"
"TransparentPushButton:pressed,\n"
"TransparentDropDownPushButton:pressed,\n"
"TransparentTogglePushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:disabled,\n"
"TransparentToggleToolButt"
                        "on:disabled,\n"
"TransparentDropDownToolButton:disabled,\n"
"TransprentPushButton:disabled,\n"
"TransparentDropDownPushButton:disabled,\n"
"TransprentTogglePushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"PillPushButton,\n"
"PillPushButton:hover,\n"
"PillPushButton:pressed,\n"
"PillPushButton:disabled,\n"
"PillPushButton:checked,\n"
"PillPushButton:checked:hover,\n"
"PillPushButton:checked:pressed,\n"
"PillPushButton:disabled:checked,\n"
"PillToolButton,\n"
"PillToolButton:hover,\n"
"PillToolButton:pressed,\n"
"PillToolButton:disabled,\n"
"PillToolButton:checked,\n"
"PillToolButton:checked:hover,\n"
"PillToolButton:checked:pressed,\n"
"PillToolButton:disabled:checked {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icon/app/resource/icon/string.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PushButton_2.setIcon(icon7)
        self.PushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.PushButton_2)

        self.horizontalSpacer_15 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)


        self.verticalLayout_5.addWidget(self.frame_26)


        self.horizontalLayout_13.addWidget(self.frame_24)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget_6)

        HomeMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeMainWindow)
        self.pushButton_3.clicked.connect(HomeMainWindow.close)
        self.pushButton_4.clicked.connect(HomeMainWindow.showMinimized)

        self.pushButton_5.setDefault(False)


        QMetaObject.connectSlotsByName(HomeMainWindow)
    # setupUi

    def retranslateUi(self, HomeMainWindow):
        HomeMainWindow.setWindowTitle(QCoreApplication.translate("HomeMainWindow", u"MainWindow", None))
        self.pushButton_5.setText(QCoreApplication.translate("HomeMainWindow", u"v0.23", None))
        self.label_18.setText(QCoreApplication.translate("HomeMainWindow", u"CuteAide2", None))
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("HomeMainWindow", u"VIP \u5230\u671f\u65f6\u95f4: ", None))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("HomeMainWindow", u"2025-01-04 18:32:31", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("HomeMainWindow", u"\u5206  \u8fa8  \u7387:", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("HomeMainWindow", u"1920*1080", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("HomeMainWindow", u"\u9002\u914d\u72b6\u6001:", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("HomeMainWindow", u"\u5df2\u9002\u914d", None))
        self.RadioButton_2.setText(QCoreApplication.translate("HomeMainWindow", u"\u7cfb\u7edf\u63a7\u5236\u9a71\u52a8, \u65e0\u9700\u5b89\u88c5 \u7f57\u6280\u9a71\u52a8", None))
        self.RadioButton_4.setText(QCoreApplication.translate("HomeMainWindow", u"GHUB 2021\u7248\u9a71\u52a8, \u65e0\u811a\u672c", None))
        self.RadioButton_19.setText(QCoreApplication.translate("HomeMainWindow", u"GHUB \u6700\u65b0\u7248\u9a71\u52a8, \u4e0b\u65b9\u83b7\u53d6\u811a\u672c", None))
        self.PushButton.setText(QCoreApplication.translate("HomeMainWindow", u" \u5f00\u59cb\u538b\u67aa\u8bc6\u522b", None))
        self.PushButton_7.setText(QCoreApplication.translate("HomeMainWindow", u"\u52a0\u5165QQ\u7fa4", None))
        self.PushButton_8.setText(QCoreApplication.translate("HomeMainWindow", u"\u83b7\u53d6\u538b\u67aa\u811a\u672c", None))
        self.RadioButton_13.setText(QCoreApplication.translate("HomeMainWindow", u"\u5355\u51fb\u5f00\u955c", None))
        self.RadioButton_14.setText(QCoreApplication.translate("HomeMainWindow", u"\u957f\u6309\u5f00\u955c", None))
        self.RadioButton_15.setText(QCoreApplication.translate("HomeMainWindow", u"C \u952e\u4e0b\u8e72", None))
        self.RadioButton_16.setText(QCoreApplication.translate("HomeMainWindow", u"Ctrl \u952e\u4e0b\u8e72", None))
        self.SwitchButton_9.setOnText(QCoreApplication.translate("HomeMainWindow", u"\u663e\u793a\u60ac\u6d6e\u7a97", None))
        self.SwitchButton_9.setOffText(QCoreApplication.translate("HomeMainWindow", u"\u663e\u793a\u60ac\u6d6e\u7a97", None))
        self.SwitchButton_8.setText(QCoreApplication.translate("HomeMainWindow", u"\u4e22\u96f7\u5012\u8ba1\u65f6", None))
        self.SwitchButton_8.setOnText(QCoreApplication.translate("HomeMainWindow", u"\u4fdd\u5bc6\u5f00\u53d1\u4e2d", None))
        self.SwitchButton_8.setOffText(QCoreApplication.translate("HomeMainWindow", u"\u4e22\u96f7\u5012\u8ba1\u65f6", None))
        self.SwitchButton_10.setText(QCoreApplication.translate("HomeMainWindow", u"\u667a\u80fd\u97f3\u91cf", None))
        self.SwitchButton_10.setOnText(QCoreApplication.translate("HomeMainWindow", u"\u4fdd\u5bc6\u5f00\u53d1\u4e2d", None))
        self.SwitchButton_10.setOffText(QCoreApplication.translate("HomeMainWindow", u"\u667a\u80fd\u97f3\u91cf", None))
        self.SwitchButton_11.setText(QCoreApplication.translate("HomeMainWindow", u"\u8ddd\u79bb\u663e\u793a", None))
        self.SwitchButton_11.setOnText(QCoreApplication.translate("HomeMainWindow", u"\u4fdd\u5bc6\u5f00\u53d1\u4e2d", None))
        self.SwitchButton_11.setOffText(QCoreApplication.translate("HomeMainWindow", u"\u8ddd\u79bb\u663e\u793a", None))
        self.SwitchButton_12.setText(QCoreApplication.translate("HomeMainWindow", u"\u663e\u793a\u5bc6\u5ba4", None))
        self.SwitchButton_12.setOnText(QCoreApplication.translate("HomeMainWindow", u"\u4fdd\u5bc6\u5f00\u53d1\u4e2d", None))
        self.SwitchButton_12.setOffText(QCoreApplication.translate("HomeMainWindow", u"\u663e\u793a\u5bc6\u5ba4", None))
        self.SwitchButton_13.setText(QCoreApplication.translate("HomeMainWindow", u"\u5f00\u542f\u8fde\u70b9", None))
        self.SwitchButton_13.setOnText(QCoreApplication.translate("HomeMainWindow", u"\u4fdd\u5bc6\u5f00\u53d1\u4e2d", None))
        self.SwitchButton_13.setOffText(QCoreApplication.translate("HomeMainWindow", u"\u5f00\u542f\u8fde\u70b9", None))
        self.SwitchButton_14.setText(QCoreApplication.translate("HomeMainWindow", u"\u5feb\u901f\u6ed1\u6b65", None))
        self.SwitchButton_14.setOnText(QCoreApplication.translate("HomeMainWindow", u"\u4fdd\u5bc6\u5f00\u53d1\u4e2d", None))
        self.SwitchButton_14.setOffText(QCoreApplication.translate("HomeMainWindow", u"\u5feb\u901f\u6ed1\u6b65", None))
        self.SwitchButton_15.setText(QCoreApplication.translate("HomeMainWindow", u"\u5feb\u901f\u62fe\u53d6", None))
        self.SwitchButton_15.setOnText(QCoreApplication.translate("HomeMainWindow", u"\u4fdd\u5bc6\u5f00\u53d1\u4e2d", None))
        self.SwitchButton_15.setOffText(QCoreApplication.translate("HomeMainWindow", u"\u5feb\u901f\u62fe\u53d6", None))
        self.PushButton_2.setText(QCoreApplication.translate("HomeMainWindow", u" \u9ad8\u7ea7\u529f\u80fd(\u5f00\u53d1\u4e2d)", None))
    # retranslateUi

