
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import pyautogui
import resourses_rc

width_display, height_display = pyautogui.size()


class Ui_errorWindow(object):

    def setupUi(self, errorWindow, message):
        self._message = message
        if not errorWindow.objectName():
            errorWindow.setObjectName(u"errorWindow")
        errorWindow.resize(406, 294)
        errorWindow.setMinimumSize(QSize(width_display/2.42, height_display/3.03))
        errorWindow.setStyleSheet(u"background-color: rgb(51, 51, 51);")
        self.verticalLayout = QVBoxLayout(errorWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MenuFrame = QFrame(errorWindow)
        self.MenuFrame.setObjectName(u"MenuFrame")
        self.MenuFrame.setStyleSheet(u"border-left: 10px solid black;\n"
                                     "border-right: 10px solid black;\n"
                                     "border-bottom: 10px solid black;\n"
                                     )
        self.MenuFrame.setFrameShape(QFrame.StyledPanel)
        self.MenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MenuFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, height_display / 36)
        self.topbar_menu = QFrame(self.MenuFrame)
        self.topbar_menu.setObjectName(u"topbar_menu")
        self.topbar_menu.setMinimumSize(QSize(height_display / 90, height_display / 30))
        self.topbar_menu.setMaximumSize(QSize(16777215, height_display / 30))
        self.topbar_menu.setCursor(QCursor(Qt.ArrowCursor))
        self.topbar_menu.setStyleSheet(u"background-color: black;")
        self.topbar_menu.setFrameShape(QFrame.WinPanel)
        self.topbar_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topbar_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.closeButton = QPushButton(self.topbar_menu)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(height_display / 90, height_display / 90))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"QPushButton:hover{\n"
                                       "	background-color: rgb(170, 0, 0);\n"
                                       "}")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/WindowCloseButton.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QSize(height_display / 60, height_display / 60))

        self.horizontalLayout_2.addWidget(self.closeButton, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.topbar_menu)

        self.errorInfoLabel = QLabel(self.MenuFrame)
        self.errorInfoLabel.setObjectName(u"errorInfoLabel")
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(11)
        self.errorInfoLabel.setFont(font)
        self.errorInfoLabel.setMinimumSize(QSize(width_display / 2.5, height_display / 4))
        self.errorInfoLabel.setStyleSheet(u"color: white;\n"
                                          "border-top: none;\n"
                                          "border-bottom: none;\n"
                                          "border-left: none;\n"
                                          "border-right: none;\n"
                                          "margin-bottom: 85%;\n"
                                          "margin-left: 1%;\n"
                                          "margin-right: 1%;\n"
                                          )

        self.verticalLayout_2.addWidget(self.errorInfoLabel, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.OKButton = QPushButton(self.MenuFrame)
        self.OKButton.setObjectName(u"OKButton")
        self.OKButton.setMinimumSize(QSize(width_display / 15.23, height_display / 25.35))
        self.OKButton.setCursor(QCursor(Qt.PointingHandCursor))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.OKButton.setFont(font1)
        self.OKButton.setStyleSheet(u"QPushButton{\n"
                                    "background-color: #bd6e38;\n"
                                    "color: white;\n"
                                    "border: 4px solid white;\n"
                                    "border-radius: 15px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "   background-color: black;\n"
                                    "   border-color: #bd6e38;\n"
                                    "}\n")

        self.verticalLayout_2.addWidget(self.OKButton, 0, Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.MenuFrame)

        self.retranslateUi(errorWindow)

        QMetaObject.connectSlotsByName(errorWindow)

    # setupUi

    def retranslateUi(self, errorWindow):
        errorWindow.setWindowTitle(QCoreApplication.translate("errorWindow", u"Form", None))
        self.closeButton.setText("")
        self.errorInfoLabel.setText(QCoreApplication.translate("errorWindow",
                                                               u"<html><head/><body><p align=\"center\">" + self._message + "</p></body></html>",
                                                               None))
        self.OKButton.setText(QCoreApplication.translate("errorWindow", u"OK", None))
    # retranslateUi
