# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowzseXTY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import pyautogui
import pandas as pd
from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QSize, Qt, QSortFilterProxyModel)
from PySide2.QtGui import (QCursor, QFont,
                           QIcon)
from PySide2.QtWidgets import *
from ClientsTableView import TableModel
from Backend.Domain.Client import Client
from Backend.Repository import FileRepository
from Backend.Service import Service

from screeninfo import get_monitors

repository = FileRepository("test.csv", Client.read_from_file, Client.write_to_file)
service = Service(repository)

# os.system('Pyrcc5 resourses.qrc -o resourses_rc.py')


width_display, height_display = pyautogui.size()


class Ui_Main(object):

    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(718, 453)
        Main.setMinimumSize(QSize(2018, 1053))

        Main.setStyleSheet(u"")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")

        self.centralwidget.setMinimumSize(QSize(2018, 1053))

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topbar_menu = QFrame(self.centralwidget)
        self.topbar_menu.setObjectName(u"topbar_menu")
        self.topbar_menu.setMinimumSize(QSize(20, 148))
        self.topbar_menu.setMaximumSize(QSize(16777215, 148))
        self.topbar_menu.setCursor(QCursor(Qt.ArrowCursor))
        self.topbar_menu.setStyleSheet(u"background-color: black;")
        self.topbar_menu.setFrameShape(QFrame.WinPanel)
        self.topbar_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topbar_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slideMenuFrame = QFrame(self.topbar_menu)
        self.slideMenuFrame.setObjectName(u"slideMenuFrame")
        self.slideMenuFrame.setMinimumSize(QSize(156, 160))
        self.slideMenuFrame.setMaximumSize(QSize(1999, 1999))
        self.slideMenuFrame.setStyleSheet(u"background-color: black;")
        self.slideMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.slideMenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.slideMenuFrame)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 6, 6, 6)
        self.slideMenuButton = QPushButton(self.slideMenuFrame)
        self.slideMenuButton.setObjectName(u"slideMenuButton")
        self.slideMenuButton.setMinimumSize(QSize(153, 100))
        self.slideMenuButton.setMaximumSize(QSize(400, 500))
        self.slideMenuButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.slideMenuButton.setStyleSheet(u"QPushButton{\n"
                                           "	border-radius: 16px;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "	background-color: rgb(208, 116, 53);\n"
                                           "}\n"
                                           "\n"
                                           "")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/Menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.slideMenuButton.setIcon(icon)
        self.slideMenuButton.setIconSize(QSize(70, 70))

        self.horizontalLayout_3.addWidget(self.slideMenuButton)

        self.horizontalLayout_2.addWidget(self.slideMenuFrame, 0, Qt.AlignLeft)

        self.titlleFrame = QFrame(self.topbar_menu)
        self.titlleFrame.setObjectName(u"titlleFrame")
        self.titlleFrame.setStyleSheet(u"margin-left: 20%;")
        self.titlleFrame.setFrameShape(QFrame.StyledPanel)
        self.titlleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.titlleFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 6, 0, -1)
        self.titleLabel = QLabel(self.titlleFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"color: #bd6e38;\n"
                                      "")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.titleLabel)

        self.horizontalLayout_2.addWidget(self.titlleFrame)

        self.window_buttons = QFrame(self.topbar_menu)
        self.window_buttons.setObjectName(u"window_buttons")
        self.window_buttons.setStyleSheet(u"border: none;\n"
                                          "margin-right: 5%;\n"
                                          "")
        self.window_buttons.setFrameShape(QFrame.WinPanel)
        self.window_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.window_buttons)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 9)
        self.minimazeButton = QPushButton(self.window_buttons)
        self.minimazeButton.setObjectName(u"minimazeButton")
        self.minimazeButton.setMinimumSize(QSize(90, 90))
        self.minimazeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimazeButton.setStyleSheet(u"QPushButton:hover{\n"
                                          "	background-color: rgb(154, 154, 154);\n"
                                          "}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/Minimaze-Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimazeButton.setIcon(icon1)
        self.minimazeButton.setIconSize(QSize(41, 41))

        self.horizontalLayout.addWidget(self.minimazeButton)

        self.maximazeButton = QPushButton(self.window_buttons)
        self.maximazeButton.setObjectName(u"maximazeButton")
        self.maximazeButton.setMinimumSize(QSize(95, 95))
        self.maximazeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximazeButton.setStyleSheet(u"QPushButton:hover{\n"
                                          "	background-color: rgb(154, 154, 154);\n"
                                          "}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/MaximazeButton_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximazeButton.setIcon(icon2)
        self.maximazeButton.setIconSize(QSize(56, 56))

        self.horizontalLayout.addWidget(self.maximazeButton)

        self.closeButton = QPushButton(self.window_buttons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(100, 100))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"QPushButton:hover{\n"
                                       "	background-color: rgb(170, 0, 0);\n"
                                       "}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/WindowCloseButton.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QSize(52, 52))

        self.horizontalLayout.addWidget(self.closeButton)

        self.horizontalLayout_2.addWidget(self.window_buttons, 0, Qt.AlignRight | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.topbar_menu)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.left_side_menu = QFrame(self.centralwidget)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(170, 0))
        self.left_side_menu.setMaximumSize(QSize(170, 16777215))
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
                                          "	background-color: black;\n"
                                          "}\n"
                                          "QPushButton{\n"
                                          "	background: transparent;\n"
                                          "	color: white;\n"
                                          "}")
        self.left_side_menu.setFrameShape(QFrame.WinPanel)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.left_menu_buttons = QFrame(self.left_side_menu)
        self.left_menu_buttons.setObjectName(u"left_menu_buttons")
        self.left_menu_buttons.setStyleSheet(u"margin-top: 10%;\n")
        self.left_menu_buttons.setFrameShape(QFrame.StyledPanel)
        self.left_menu_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu_buttons)
        self.verticalLayout_2.setSpacing(55)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 28, 0, 20)
        self.homeButton = QPushButton(self.left_menu_buttons)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setStyleSheet(u"margin-left: 0%;")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/New-Home-Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon4)
        self.homeButton.setIconSize(QSize(88, 88))

        self.verticalLayout_2.addWidget(self.homeButton)

        self.listButton = QPushButton(self.left_menu_buttons)
        self.listButton.setObjectName(u"listButton")
        self.listButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.listButton.setStyleSheet(u"margin-left: 0%;")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/New-Search-Icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.listButton.setIcon(icon5)
        self.listButton.setIconSize(QSize(85, 85))

        self.verticalLayout_2.addWidget(self.listButton)

        self.addButton = QPushButton(self.left_menu_buttons)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"margin-left: 0%;")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Icons/New_Add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon6)
        self.addButton.setIconSize(QSize(85, 85))

        self.verticalLayout_2.addWidget(self.addButton)

        self.removeButton = QPushButton(self.left_menu_buttons)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.removeButton.setStyleSheet(u"margin-left: 0%;")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Icons/New_Delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.removeButton.setIcon(icon7)
        self.removeButton.setIconSize(QSize(85, 85))

        self.verticalLayout_2.addWidget(self.removeButton)

        self.verticalLayout_3.addWidget(self.left_menu_buttons, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.versionLabel = QLabel(self.left_side_menu)
        self.versionLabel.setMinimumSize(QSize(100, 100))
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setStyleSheet(u"color: white;\n"
                                        "margin-left: 10%;\n"
                                        "font-size: 30px;\n")

        self.verticalLayout_3.addWidget(self.versionLabel, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.gridLayout.addWidget(self.left_side_menu, 0, 0, 2, 1)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 40))
        self.footer.setMaximumSize(QSize(16777215, 40))
        self.footer.setStyleSheet(u"background-color: black;\n"
                                  "")
        self.footer.setFrameShape(QFrame.WinPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.footer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(40, 30))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.size_grip, 0, Qt.AlignRight | Qt.AlignBottom)

        self.gridLayout.addWidget(self.footer, 1, 1, 1, 1)

        self.content_menu = QFrame(self.centralwidget)
        self.content_menu.setObjectName(u"content_menu")
        self.content_menu.setMinimumSize(QSize(30, 60))
        self.content_menu.setStyleSheet(u"background-color: #333;")
        self.content_menu.setFrameShape(QFrame.WinPanel)
        self.content_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.containerPages = QStackedWidget(self.content_menu)
        self.containerPages.setObjectName(u"containerPages")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setPointSize(30)
        self.containerPages.setFont(font1)
        self.containerPages.setStyleSheet(u"background: #333;\n"
                                          "QcheckBox{\n"
                                          "	font: 12pt \"Bahnschript\";\n"
                                          "	font-style: italic;\n"
                                          "	color: white;\n"
                                          "}")
        self.HomeWWidget = QWidget()
        self.HomeWWidget.setObjectName(u"HomeWWidget")
        self.HomeWWidget.setStyleSheet(u"border-image: url(:/Icons/Icons/new_background.svg)")
        self.verticalLayout_11 = QVBoxLayout(self.HomeWWidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.homeTitleLabel = QLabel(self.HomeWWidget)
        self.homeTitleLabel.setObjectName(u"homeTitleLabel")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift")
        font2.setPointSize(60)
        font2.setBold(True)
        font2.setWeight(75)
        self.homeTitleLabel.setFont(font2)
        self.homeTitleLabel.setStyleSheet(u"border-image: none;\n"
                                          "background: transparent;\n"
                                          "color: white;")
        self.homeTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.homeTitleLabel)

        self.homeintroLabel = QLabel(self.HomeWWidget)
        self.homeintroLabel.setObjectName(u"homeintroLabel")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift")
        font3.setPointSize(12)
        self.homeintroLabel.setFont(font3)
        self.homeintroLabel.setStyleSheet(u"border-image: none;\n"
                                          "background: transparent;\n"
                                          "color: white;\n"
                                          )
        self.homeintroLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.homeintroLabel, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.containerPages.addWidget(self.HomeWWidget)
        self.SearchWidget = QWidget()
        self.SearchWidget.setObjectName(u"SearchWidget")
        self.verticalLayout_9 = QVBoxLayout(self.SearchWidget)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 5, 5)
        self.searchbarFrame = QFrame(self.SearchWidget)
        self.searchbarFrame.setObjectName(u"searchbarFrame")
        self.searchbarFrame.setFrameShape(QFrame.StyledPanel)
        self.searchbarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.searchbarFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.searchbarLineEdit = QLineEdit(self.searchbarFrame)
        self.searchbarLineEdit.setObjectName(u"searchbarLineEdit")
        self.searchbarLineEdit.setStyleSheet(u"color: white;\n"
                                             "border: 1px solid white;\n"
                                             "border-radius: 30%;\n"
                                             "font-size: 45px;\n")
        self.searchbarLineEdit.setMinimumHeight(70)
        self.searchbarLineEdit.setPlaceholderText("Căutați aici...")
        self.searchbarLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.searchbarLineEdit)

        self.verticalLayout_9.addWidget(self.searchbarFrame)

        self.FilterCheckBoxFrame = QFrame(self.SearchWidget)
        self.FilterCheckBoxFrame.setObjectName(u"FilterCheckBoxFrame")
        self.FilterCheckBoxFrame.setStyleSheet(u"QRadioButton{\n"
                                               "	font: 9pt \"Bahnschript\";\n"
                                               "	font-style: italic;\n"
                                               "	color: white;\n"
                                               "}")
        self.FilterCheckBoxFrame.setFrameShape(QFrame.StyledPanel)
        self.FilterCheckBoxFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.FilterCheckBoxFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.recentDateOrderRadioButton = QRadioButton(self.FilterCheckBoxFrame)
        self.recentDateOrderRadioButton.setObjectName(u"recentDateOrderRadioButton")

        self.horizontalLayout_9.addWidget(self.recentDateOrderRadioButton, 0, Qt.AlignHCenter)

        self.oldDateOrderRadioButton = QRadioButton(self.FilterCheckBoxFrame)
        self.oldDateOrderRadioButton.setObjectName(u"oldDateOrderRadioButton")

        self.horizontalLayout_9.addWidget(self.oldDateOrderRadioButton, 0, Qt.AlignHCenter)

        self.alphabeticalOrderRadioButton = QRadioButton(self.FilterCheckBoxFrame)
        self.alphabeticalOrderRadioButton.setObjectName(u"alphabeticalOrderRadioButton")

        self.horizontalLayout_9.addWidget(self.alphabeticalOrderRadioButton, 0, Qt.AlignHCenter)

        self.verticalLayout_9.addWidget(self.FilterCheckBoxFrame)

        self.tableFrame = QFrame(self.SearchWidget)
        self.tableFrame.setObjectName(u"tableFrame")
        self.tableFrame.setStyleSheet(u"border: 1px solid white;\n"
                                      "border-radius: 4px;\n"
                                      "margin-right:20%;\n"
                                      "margin-left:20%;\n"
                                      )
        self.tableFrame.setFrameShape(QFrame.StyledPanel)
        self.tableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.tableFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.clientsDataTableView = QTableView(self.SearchWidget)

        data = pd.DataFrame(service.repository,
                            columns=['Nume', 'ID', 'Creat la', 'Expiră la'])
        self.model = TableModel(data)
        # filter proxy model
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(-1)  # -1 is for searching in all columns

        self.clientsDataTableView.setModel(self.filter_proxy_model)
        self.clientsDataTableView.verticalHeader().hide()  # REMOVE VERTICAL HEADER
        self.clientsDataTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.clientsDataTableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.clientsDataTableView.horizontalHeader().setStretchLastSection(True)
        self.clientsDataTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.clientsDataTableView.setSelectionBehavior(QTableView.SelectRows)

        self.clientsDataTableView.setObjectName(u"clientsDataTableView")
        self.clientsDataTableView.setStyleSheet(u"border: none;\n"
                                                "margin-right:0%;\n"
                                                "margin-left:0%;\n"
                                                "font: 9pt 'Bahnschript';\n"
                                                "font-style: bold italic;\n"
                                                )

        self.verticalLayout_12.addWidget(self.clientsDataTableView)

        self.verticalLayout_9.addWidget(self.tableFrame)

        self.ViewClientButton = QPushButton(self.SearchWidget)
        self.ViewClientButton.setObjectName(u"ViewClientButton")
        self.ViewClientButton.setMinimumSize(QSize(100, 50))
        self.ViewClientButton.setCursor(QCursor(Qt.PointingHandCursor))
        font4 = QFont()
        font4.setPointSize(15)
        self.ViewClientButton.setFont(font4)
        self.ViewClientButton.setStyleSheet(u"QPushButton{\n"
                                            "   background-color: #bd6e38;\n"
                                            "   color: white;\n"
                                            "   border: 4px solid white;\n"
                                            "   border-radius: 15px;\n"
                                            "   margin-bottom: 5%;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "   background-color: black;\n"
                                            "   border-color: #bd6e38;\n"
                                            "}\n"
                                            )

        self.verticalLayout_9.addWidget(self.ViewClientButton, 0, Qt.AlignHCenter)

        self.containerPages.addWidget(self.SearchWidget)
        self.ViewClientWidget = QWidget()
        self.ViewClientWidget.setObjectName(u"ViewClientWidget")
        self.verticalLayout_13 = QVBoxLayout(self.ViewClientWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.ClientViewFrame = QFrame(self.ViewClientWidget)
        self.ClientViewFrame.setObjectName(u"ClientViewFrame")
        self.ClientViewFrame.setStyleSheet(u"QLabel{\n"
                                           "	font: 12pt \"Bahnschript\";\n"
                                           "	font-style: italic;\n"
                                           "	color: white;\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit{\n"
                                           "	border-right: none;\n"
                                           "	border-top: none;\n"
                                           "	border-left: none;\n"
                                           "	border-bottom: 1px solid white;\n"
                                           "}")
        self.ClientViewFrame.setFrameShape(QFrame.StyledPanel)
        self.ClientViewFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.ClientViewFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 15, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(35)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setContentsMargins(20, -1, 20, -1)
        self.NameLabel = QLabel(self.ClientViewFrame)
        self.NameLabel.setObjectName(u"NameLabel")

        self.gridLayout_4.addWidget(self.NameLabel, 0, 0, 1, 1)

        self.nameLineEdit = QLineEdit(self.ClientViewFrame)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setStyleSheet(u"	font: 12pt \"Bahnschript\";\n"
                                        "	font-style: italic;\n"
                                        "	color: white;")
        self.nameLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.nameLineEdit, 0, 1, 1, 1)

        self.CreationDateLabel = QLabel(self.ClientViewFrame)
        self.CreationDateLabel.setObjectName(u"CreationDateLabel")

        self.gridLayout_4.addWidget(self.CreationDateLabel, 0, 2, 1, 1)

        self.crationDateLineEdit = QLineEdit(self.ClientViewFrame)
        self.crationDateLineEdit.setObjectName(u"creationDateLineEdit")
        self.crationDateLineEdit.setStyleSheet(u"	font: 12pt \"Bahnschript\";\n"
                                               "	font-style: italic;\n"
                                               "	color: white;")
        self.crationDateLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.crationDateLineEdit, 0, 3, 1, 1)

        self.IdLabel = QLabel(self.ClientViewFrame)
        self.IdLabel.setObjectName(u"IdLabel")

        self.gridLayout_4.addWidget(self.IdLabel, 1, 0, 1, 1)

        self.IdLineEdit = QLineEdit(self.ClientViewFrame)
        self.IdLineEdit.setObjectName(u"IdLineEdit")
        self.IdLineEdit.setStyleSheet(u"	font: 12pt \"Bahnschript\";\n"
                                      "	font-style: italic;\n"
                                      "	color: white;")
        self.IdLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.IdLineEdit, 1, 1, 1, 1)

        self.ExpirationDateLabel = QLabel(self.ClientViewFrame)
        self.ExpirationDateLabel.setObjectName(u"ExpirationDateLabel")

        self.gridLayout_4.addWidget(self.ExpirationDateLabel, 1, 2, 1, 1)

        self.expirationDateLineEdit = QLineEdit(self.ClientViewFrame)
        self.expirationDateLineEdit.setObjectName(u"expirationDateLineEdit")
        self.expirationDateLineEdit.setStyleSheet(u"	font: 12pt \"Bahnschript\";\n"
                                                  "	font-style: italic;\n"
                                                  "	color: white;")
        self.expirationDateLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.expirationDateLineEdit, 1, 3, 1, 1)

        self.verticalLayout_14.addLayout(self.gridLayout_4)

        self.Valid_InvalidLabel = QLabel(self.ClientViewFrame)
        self.Valid_InvalidLabel.setObjectName(u"Valid_InvalidLabel")
        font5 = QFont()
        font5.setFamily(u"Bahnschript")
        font5.setPointSize(25)
        font5.setBold(False)
        font5.setItalic(True)
        font5.setWeight(50)
        self.Valid_InvalidLabel.setFont(font5)
        self.Valid_InvalidLabel.setStyleSheet(u"font: 25pt \"Bahnschript\";\n"
                                              "font-style: italic;\n"
                                              "color: white;")
        self.Valid_InvalidLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.Valid_InvalidLabel)

        self.PrintButton = QPushButton(self.ClientViewFrame)
        self.PrintButton.setObjectName(u"PrintButton")
        self.PrintButton.setMinimumSize(QSize(180, 130))
        self.PrintButton.setCursor(QCursor(Qt.PointingHandCursor))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setWeight(75)
        self.PrintButton.setFont(font6)
        self.PrintButton.setStyleSheet(u"QPushButton{\n"
                                       "background-color: #bd6e38;\n"
                                       "color: white;\n"
                                       "border: 4px solid white;\n"
                                       "border-radius: 30%;\n"
                                       "margin-bottom: 40%;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "   background-color: black;\n"
                                       "   border-color: #bd6e38;\n"
                                       "}\n"
                                       )

        self.verticalLayout_14.addWidget(self.PrintButton, 0, Qt.AlignHCenter)

        self.verticalLayout_13.addWidget(self.ClientViewFrame)

        self.containerPages.addWidget(self.ViewClientWidget)
        self.AddWidget = QWidget()
        self.AddWidget.setObjectName(u"AddWidget")
        self.verticalLayout_6 = QVBoxLayout(self.AddWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.addTextFrame = QFrame(self.AddWidget)
        self.addTextFrame.setObjectName(u"addTextFrame")
        self.addTextFrame.setStyleSheet(u"border-bottom: 1px solid #bd6e38;\n"
                                        "border-top: 2px solid #bd6e38;")
        self.addTextFrame.setFrameShape(QFrame.StyledPanel)
        self.addTextFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.addTextFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.addTextLabel = QLabel(self.addTextFrame)
        self.addTextLabel.setObjectName(u"addTextLabel")
        font7 = QFont()
        font7.setFamily(u"Bahnschrift")
        font7.setPointSize(15)
        font7.setItalic(True)
        self.addTextLabel.setFont(font7)
        self.addTextLabel.setStyleSheet(u"color: white;\n"
                                        "border: none;")
        self.addTextLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.addTextLabel)

        self.verticalLayout_6.addWidget(self.addTextFrame)

        self.InsertNameFrame = QFrame(self.AddWidget)
        self.InsertNameFrame.setObjectName(u"InsertNameFrame")
        self.InsertNameFrame.setFrameShape(QFrame.StyledPanel)
        self.InsertNameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.InsertNameFrame)
        self.horizontalLayout_5.setSpacing(13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addNameLabel = QLabel(self.InsertNameFrame)
        self.addNameLabel.setObjectName(u"addNameLabel")
        font8 = QFont()
        font8.setFamily(u"Bahnschrift")
        font8.setPointSize(17)
        font8.setItalic(True)
        self.addNameLabel.setFont(font8)
        self.addNameLabel.setStyleSheet(u"color: white;\n"
                                        "margin-left:  70%;\n"
                                        "margin-bottom: 10%;\n"
                                        "")
        self.addNameLabel.setAlignment(Qt.AlignCenter)
        self.addNameLabel.setMargin(0)

        self.horizontalLayout_5.addWidget(self.addNameLabel)

        self.addLineEdit = QLineEdit(self.InsertNameFrame)
        self.addLineEdit.setObjectName(u"addLineEdit")
        self.addLineEdit.setMinimumSize(QSize(50, 0))
        font9 = QFont()
        font9.setFamily(u"Bahnschrift")
        font9.setPointSize(17)
        self.addLineEdit.setFont(font9)
        self.addLineEdit.setStyleSheet(u"margin-right: 70%;\n"
                                       "color: white;\n"
                                       "border-top: none;\n"
                                       "border-left: none;\n"
                                       "border-right: none;\n"
                                       "border-bottom: 1px solid white;\n"
                                       "\n"
                                       "")
        self.addLineEdit.setAlignment(Qt.AlignCenter)
        self.addLineEdit.setDragEnabled(False)

        self.horizontalLayout_5.addWidget(self.addLineEdit)

        self.verticalLayout_6.addWidget(self.InsertNameFrame)

        self.addButtonsFrame = QFrame(self.AddWidget)
        self.addButtonsFrame.setObjectName(u"addButtonsFrame")
        self.addButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.addButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.addButtonsFrame)
        self.horizontalLayout_6.setSpacing(40)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addPushBUtton = QPushButton(self.addButtonsFrame)
        self.addPushBUtton.setObjectName(u"addPushBUtton")
        self.addPushBUtton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addPushBUtton.setMinimumSize(QSize(0, 30))
        font10 = QFont()
        font10.setFamily(u"Bahnschrift")
        font10.setPointSize(14)
        self.addPushBUtton.setFont(font10)
        self.addPushBUtton.setStyleSheet(u"QPushButton{\n"
                                         "  background-color: #bd6e38;\n"
                                         "  color: white;\n"
                                         "  border: 4px solid white;\n"
                                         "  border-radius: 15px;\n"
                                         "  margin-left: 70%;\n"
                                         "  margin-right: 50%;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "      background-color: black;\n"
                                         "      border-color: #bd6e38;\n "
                                         "}\n"
                                         )

        self.horizontalLayout_6.addWidget(self.addPushBUtton)

        self.quitPushButton = QPushButton(self.addButtonsFrame)
        self.quitPushButton.setObjectName(u"quitPushButton")
        self.quitPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.quitPushButton.setMinimumSize(QSize(0, 34))
        self.quitPushButton.setFont(font10)
        self.quitPushButton.setStyleSheet(u"QPushButton{\n"
                                          "  background-color: #bd6e38;\n"
                                          "  color: white;\n"
                                          "  border: 4px solid white;\n"
                                          "  border-radius: 15px;\n"
                                          "  margin-left: 70%;\n"
                                          "  margin-right: 50%;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "   background-color: black;\n"
                                          "   border-color: #bd6e38;\n "
                                          "}\n"
                                          )

        self.horizontalLayout_6.addWidget(self.quitPushButton)

        self.verticalLayout_6.addWidget(self.addButtonsFrame)

        self.containerPages.addWidget(self.AddWidget)
        self.RemoveWidget = QWidget()
        self.RemoveWidget.setObjectName(u"RemoveWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.RemoveWidget)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 2, 2, 3)
        self.removeElementsFrame = QFrame(self.RemoveWidget)
        self.removeElementsFrame.setObjectName(u"removeElementsFrame")
        self.verticalLayout_16 = QVBoxLayout(self.removeElementsFrame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.removeTextFrame = QFrame(self.removeElementsFrame)
        self.removeTextFrame.setObjectName(u"removeTextFrame")
        self.removeTextFrame.setStyleSheet(u"border-right: 4px solid #bd6e38;\n"
                                           "border-bottom: 4px solid #bd6e38;\n"
                                           "border: 4px solid #bd6e38;\n"
                                           "border-top-right-radius: 5%;\n"
                                           "border-bottom-right-radius: 5%;\n"
                                           "border-left: none;\n"
                                           )
        self.removeTextFrame.setFrameShape(QFrame.StyledPanel)
        self.removeTextFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.removeTextFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.removeLabel = QLabel(self.removeTextFrame)
        self.removeLabel.setObjectName(u"removeLabel")
        self.removeLabel.setFont(font7)
        self.removeLabel.setStyleSheet(u"color: white;\n"
                                       "border: none;")
        self.removeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.removeLabel)

        self.verticalLayout_15.addWidget(self.removeTextFrame, 0, Qt.AlignLeft | Qt.AlignTop)

        self.removeSearchbarFrame = QFrame(self.removeElementsFrame)
        self.removeSearchbarFrame.setObjectName(u"removeSearchbarFrame")
        self.removeSearchbarFrame.setStyleSheet(u"")
        self.removeSearchbarFrame.setFrameShape(QFrame.StyledPanel)
        self.removeSearchbarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.removeSearchbarFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.removeSearchbarLineEdit = QLineEdit(self.removeSearchbarFrame)
        self.removeSearchbarLineEdit.setObjectName(u"removeSearchbarLineEdit")
        self.removeSearchbarLineEdit.setStyleSheet(u"color: white;\n"
                                                   "border: 1px solid white;\n"
                                                   "border-radius: 30%;\n"
                                                   "font: 15pt 'BahnSchrift'\n")
        self.removeSearchbarLineEdit.setPlaceholderText("Căutați aici...")
        self.removeSearchbarLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.removeSearchbarLineEdit)

        self.verticalLayout_15.addWidget(self.removeSearchbarFrame, 0, Qt.AlignTop)

        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.removeButtonsFrame = QFrame(self.removeElementsFrame)
        self.removeButtonsFrame.setObjectName(u"removeButtonsFrame")
        self.removeButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.removeButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.removeButtonsFrame)
        self.horizontalLayout_7.setSpacing(40)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.removePushButton = QPushButton(self.removeButtonsFrame)
        self.removePushButton.setObjectName(u"removePushButton")
        self.removePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.removePushButton.setMinimumSize(QSize(0, 34))
        self.removePushButton.setFont(font10)
        self.removePushButton.setStyleSheet(u"QPushButton{\n"
                                            "   background-color: #bd6e38;\n"
                                            "   color: white;\n"
                                            "   border: 4px solid white;\n"
                                            "   border-radius: 15px;\n"
                                            "   margin-right: 20%;\n"
                                            "   margin-left:40%;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "   background-color: black;\n"
                                            "   border-color: #bd6e38;\n"
                                            "}\n"
                                            )

        self.horizontalLayout_7.addWidget(self.removePushButton)

        self.quitPushButton_2 = QPushButton(self.removeButtonsFrame)
        self.quitPushButton_2.setObjectName(u"quitPushButton_2")
        self.quitPushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.quitPushButton_2.setMinimumSize(QSize(0, 34))
        self.quitPushButton_2.setFont(font10)
        self.quitPushButton_2.setStyleSheet(u"QPushButton{\n"
                                            "   background-color: #bd6e38;\n"
                                            "   color: white;\n"
                                            "   border: 4px solid white;\n"
                                            "   border-radius: 15px;\n"
                                            "   margin-right: 20%;\n"
                                            "   margin-left: 20%;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "   background-color: black;\n"
                                            "   border-color: #bd6e38;\n"
                                            "}\n"
                                            )

        self.horizontalLayout_7.addWidget(self.quitPushButton_2)

        self.verticalLayout_16.addWidget(self.removeButtonsFrame, 0, Qt.AlignBottom)

        self.horizontalLayout_11.addWidget(self.removeElementsFrame, 0, Qt.AlignLeft)

        self.removeTableFrame = QFrame(self.RemoveWidget)
        self.removeTableFrame.setObjectName(u"removeTableFrame")
        self.removeTableFrame.setStyleSheet(u"border: 1px solid white;\n"
                                            "border-radius: 4px;\n"
                                            )
        self.removeTableFrame.setFrameShape(QFrame.StyledPanel)
        self.removeTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.removeTableFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.removetableView = QTableView(self.removeTableFrame)

        self.remove_model = TableModel(data)

        self.remove_filter_proxy_model = QSortFilterProxyModel()
        self.remove_filter_proxy_model.setSourceModel(self.remove_model)
        self.remove_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.remove_filter_proxy_model.setFilterKeyColumn(-1)

        self.removetableView.setModel(self.remove_filter_proxy_model)
        self.removetableView.verticalHeader().hide()  # REMOVE VERTICAL HEADER
        self.removetableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.removetableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.removetableView.horizontalHeader().setStretchLastSection(True)
        self.removetableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.removetableView.setSelectionBehavior(QTableView.SelectRows)

        self.removetableView.setObjectName(u"removetableView")
        self.removetableView.setStyleSheet(u"border: none;\n"
                                           "margin-right:0%;\n"
                                           "margin-left:0%;\n"
                                           "font: 9pt 'Bahnschript';\n"
                                           "font-style: bold italic;\n"
                                           )

        self.verticalLayout_8.addWidget(self.removetableView)

        self.horizontalLayout_11.addWidget(self.removeTableFrame)

        self.containerPages.addWidget(self.RemoveWidget)

        self.horizontalLayout_4.addWidget(self.containerPages)

        self.gridLayout.addWidget(self.content_menu, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.containerPages.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Main)

    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.slideMenuButton.setText("")
        self.titleLabel.setText(
            QCoreApplication.translate("Main", u"<html><head/><body><p>STIHL SERVER</p></body></html>", None))
        self.minimazeButton.setText("")
        self.maximazeButton.setText("")
        self.closeButton.setText("")

        self.versionLabel.setText(QCoreApplication.translate("Main", u"v 1.2", None))
        self.homeTitleLabel.setText(QCoreApplication.translate("Main", u"HOME", None))
        self.homeintroLabel.setText(QCoreApplication.translate("Main",
                                                               u"<html><head/><body><p><span style=\"background-color:#333;\">Aceasta este aplica\u021bia pentru gestionarea clien\u021bilor.</span></p><p><span style=\"background-color:#333;\">Pentru a vizuliza un client da-\u021bi click pe iconi\u021ba cu lup\u0103.</span></p><p><span style=\"background-color:#333;\">Pentru a filtra datele bifa\u021bi, \u00een func\u021bie de preferin\u021b\u0103, c\u0103su\u021bele de sub bara de c\u0103utare.</span></p><p><span style=\"background-color:#333;\">Pentru a genera un pdf voucher selecta\u021bi clientul dorit, da\u021bi click pe butonul &quot;Vizualizeaz\u0103&quot;</span></p><p><span style=\"background-color:#333;\">dup\u0103 care, ap\u0103sa\u021bi &quot;Printare client&quot;.</span></p><p><span style=\"background-color:#333;\">Pentru a ad\u0103uga/\u0219terge un client ap\u0103sa\u021bi pe iconi\u021ba cu plus, respectiv &quot;x&quot;.</span></p></body></html>",
                                                               None))

        self.recentDateOrderRadioButton.setText(QCoreApplication.translate("Main", u"Dat\u0103 recent\u0103", None))
        self.oldDateOrderRadioButton.setText(QCoreApplication.translate("Main", u"Dat\u0103 vehce", None))
        self.alphabeticalOrderRadioButton.setText(QCoreApplication.translate("Main", u"Ordonare alfabetic\u0103", None))
        self.ViewClientButton.setText(QCoreApplication.translate("Main", u" Vizualizeaz\u0103 ", None))
        self.NameLabel.setText(QCoreApplication.translate("Main", u"Nume:", None))
        self.CreationDateLabel.setText(QCoreApplication.translate("Main", u"Dat\u0103 creare: ", None))
        self.IdLabel.setText(QCoreApplication.translate("Main", u"ID:", None))
        self.ExpirationDateLabel.setText(QCoreApplication.translate("Main", u"Dat\u0103 expirare: ", None))
        self.Valid_InvalidLabel.setText(QCoreApplication.translate("Main", u"Client valid", None))
        self.PrintButton.setText(QCoreApplication.translate("Main", u"  Genereaz\u0103 PDF ", None))
        self.addTextLabel.setText(QCoreApplication.translate("Main",
                                                             u"<html><head/><body><p align=\"center\">Pentru a ad\u0103uga un client nou trebuie </p><p align=\"center\">s\u0103 introduce\u021bi numele:</p></body></html>",
                                                             None))
        self.addNameLabel.setText(QCoreApplication.translate("Main", u"Nume: ", None))
        self.addPushBUtton.setText(QCoreApplication.translate("Main", u"Adaug\u0103", None))
        self.quitPushButton.setText(QCoreApplication.translate("Main", u"Renun\u021b\u0103", None))
        self.removeLabel.setText(QCoreApplication.translate("Main",
                                                            u"<html><head/><body><p align=\"center\">Pentru a \u0219terge un client trebuie s\u0103 </p><p align=\"center\">selecta\u021bi r\u00e2ndul corespunz\u0103tor</p></body></html>",
                                                            None))
        self.removePushButton.setText(QCoreApplication.translate("Main", u"\u0218terge", None))
        self.quitPushButton_2.setText(QCoreApplication.translate("Main", u"Renun\u021b\u0103", None))
    # retranslateUi


if __name__ == "__main__":
    for monitor in get_monitors():
        print(str(monitor))

