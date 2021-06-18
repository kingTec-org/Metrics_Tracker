# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from sys import path

from pdf2image import convert_from_path

from gui.widgets.py_calendar.py_calendar import PyCalendarWidget
from gui.widgets.py_table_view import PyTableView

# below mirror qt_core and removes warnings
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from gui.core.json_themes import Themes

# above mirror qt_core and removes warnings
from data_tools import app_functions
from data_tools.flight_funcs import *


class Ui_MainPages(object):

    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")

        MainPages.resize(659, 596)

        themes = Themes()
        self.themes = themes.items

        self.verticalLayout_2 = QVBoxLayout(MainPages)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")

        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMaximumSize(QSize(300, 150))

        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))

        font = QFont()
        font.setPointSize(14)

        self.welcome_base.setFont(font)
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)

        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)

        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFont(font)
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)

        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(10)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.label_3 = QLabel(self.welcome_base)
        self.label_3.setObjectName(u"label_3")

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView_3 = PyTableView(radius=8,
                                       color=self.themes["app_color"]["text_foreground"],
                                       selection_color=self.themes["app_color"]["context_color"],
                                       bg_color=self.themes["app_color"]["bg_two"],
                                       header_horizontal_color=self.themes["app_color"]["dark_two"],
                                       header_vertical_color=self.themes["app_color"]["bg_three"],
                                       bottom_line_color=self.themes["app_color"]["bg_three"],
                                       grid_line_color=self.themes["app_color"]["bg_one"],
                                       scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
                                       scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
                                       context_color=self.themes["app_color"]["context_color"]
                                       )
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_3.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableView_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_3.setSortingEnabled(True)

        self.crew_headers = get_crew_column_query()
        self.crew_data = get_crew_query()
        self.crew_table_model = app_functions.TableModel(self, self.crew_data, self.crew_headers)
        self.crew_table_model.setObjectName(u"crew_table")
        self.tableView_3.setModel(self.crew_table_model)

        self.gridLayout.addWidget(self.tableView_3, 2, 0, 1, 2)

        self.server_sync_notice = QLabel(self.page_2)
        self.server_sync_notice.setObjectName(u"server_sync_notice")

        self.gridLayout.addWidget(self.server_sync_notice, 0, 1, 1, 1)

        self.calendarWidget = PyCalendarWidget(radius=8,
                                               color=self.themes["app_color"]["text_foreground"],
                                               selection_color=self.themes["app_color"]["context_color"],
                                               bg_color=self.themes["app_color"]["bg_two"],
                                               header_horizontal_color=self.themes["app_color"]["dark_two"],
                                               header_vertical_color=self.themes["app_color"]["bg_three"],
                                               bottom_line_color=self.themes["app_color"]["bg_three"],
                                               grid_line_color=self.themes["app_color"]["bg_one"],
                                               scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
                                               scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
                                               context_color=self.themes["app_color"]["context_color"]
                                               )
        self.calendarWidget.setObjectName(u"calendarWidget")

        def print_date():
            if self.calendarWidget.selectedDate():
                print(self.calendarWidget.selectedDate())
        print(print_date())

        self.gridLayout.addWidget(self.calendarWidget, 1, 0, 1, 1)

        self.tableView_2 = PyTableView(radius=8,
                                       color=self.themes["app_color"]["text_foreground"],
                                       selection_color=self.themes["app_color"]["context_color"],
                                       bg_color=self.themes["app_color"]["bg_two"],
                                       header_horizontal_color=self.themes["app_color"]["dark_two"],
                                       header_vertical_color=self.themes["app_color"]["bg_three"],
                                       bottom_line_color=self.themes["app_color"]["bg_three"],
                                       grid_line_color=self.themes["app_color"]["bg_one"],
                                       scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
                                       scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
                                       context_color=self.themes["app_color"]["context_color"]
                                       )

        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableView_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_2.setSortingEnabled(True)

        self.flight_headers = get_flight_column_query()
        self.flight_data = get_flight_query()
        self.flight_table_model = app_functions.TableModel(self, self.flight_data, self.flight_headers)
        self.flight_table_model.setObjectName(u"flight_table")
        self.tableView_2.setModel(self.flight_table_model)

        self.site_id_label = QLabel(self.page_2)
        self.site_id_label.setObjectName(u"site_id_label")

        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")

        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")

        self.all_flights = PyTableView(radius=8,
                                       color=self.themes["app_color"]["text_foreground"],
                                       selection_color=self.themes["app_color"]["context_color"],
                                       bg_color=self.themes["app_color"]["bg_two"],
                                       header_horizontal_color=self.themes["app_color"]["dark_two"],
                                       header_vertical_color=self.themes["app_color"]["bg_three"],
                                       bottom_line_color=self.themes["app_color"]["bg_three"],
                                       grid_line_color=self.themes["app_color"]["bg_one"],
                                       scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
                                       scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
                                       context_color=self.themes["app_color"]["context_color"]
                                       )

        self.all_flights.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.all_flights.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.all_flights.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.all_flights.setSortingEnabled(True)

        self.flight_headers = get_flight_column_query()
        self.flight_data = get_flight_query()
        self.flight_table_model = app_functions.TableModel(self, self.flight_data, self.flight_headers)
        self.all_flights.setModel(self.flight_table_model)
        self.flight_table_model.setObjectName(u"flight_table")
        self.all_flights.setObjectName(u"all_flights")

        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_4 = QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableView = PyTableView(radius=8,
                                     color=self.themes["app_color"]["text_foreground"],
                                     selection_color=self.themes["app_color"]["context_color"],
                                     bg_color=self.themes["app_color"]["bg_two"],
                                     header_horizontal_color=self.themes["app_color"]["dark_two"],
                                     header_vertical_color=self.themes["app_color"]["bg_three"],
                                     bottom_line_color=self.themes["app_color"]["bg_three"],
                                     grid_line_color=self.themes["app_color"]["bg_one"],
                                     scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
                                     scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
                                     context_color=self.themes["app_color"]["context_color"]
                                     )

        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)

        self.crew_headers = get_crew_column_query()
        self.crew_data = get_crew_query()
        self.crew_table_model = app_functions.TableModel(self, self.crew_data, self.crew_headers)
        self.tableView.setModel(self.crew_table_model)
        self.crew_table_model.setObjectName(u"crew_table")
        self.tableView.setObjectName(u"tableView")

        self.tableView_4 = QFormLayout(self.page_4)

#        self.gridLayout_4.addWidget(self.tableView_4, 1, 1, 1, 1)

        self.name = QLabel(self.page_4)

#       Q Url.fromLocalFile(path)

        self.name.setObjectName(u"name")

        self.server_update = QLabel(self.page_4)
        self.server_update.setObjectName(u"server_update")

        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_2_layout = QVBoxLayout(self.page_5)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_5)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 639, 576))
        self.contents.setStyleSheet(u"background: transparent;")

        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.scroll_area.setWidget(self.contents)

        self.verticalLayout.addWidget(self.title_label)
        self.verticalLayout.addWidget(self.description_label)
        self.verticalLayout.addLayout(self.row_1_layout)
        self.verticalLayout.addLayout(self.row_2_layout)
        self.verticalLayout.addLayout(self.row_3_layout)
        self.verticalLayout.addLayout(self.row_4_layout)
        self.verticalLayout.addLayout(self.row_5_layout)

        self.page_2_layout.addWidget(self.scroll_area)

        self.center_page_layout.addWidget(self.logo)
        self.center_page_layout.addWidget(self.label_3)

        self.verticalLayout_7.addWidget(self.welcome_base)

        self.gridLayout.addWidget(self.tableView_2, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.site_id_label, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.all_flights, 1, 0, 1, 2)

        self.gridLayout_4.addWidget(self.name, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.tableView, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.server_update, 0, 1, 1, 1)

        self.pages.addWidget(self.page_1)
        self.pages.addWidget(self.page_2)
        self.pages.addWidget(self.page_3)
        self.pages.addWidget(self.page_4)
        self.pages.addWidget(self.page_5)

        self.verticalLayout_2.addWidget(self.pages)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(4)

        QMetaObject.connectSlotsByName(MainPages)

    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Metrics Tracker", None))
        self.server_sync_notice.setText(QCoreApplication.translate("MainPages", u"Current as of: ", None))
        self.site_id_label.setText(QCoreApplication.translate("MainPages", u"Site:", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.name.setText(QCoreApplication.translate("MainPages", u"Name:", None))
        self.server_update.setText(QCoreApplication.translate("MainPages", u"Last Sync", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages",
                                                                  u"Here will be all the custom widgets, they will be added over time on this page.\n"
                                                                  "I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.",
                                                                  None))
    # retranslateUi
