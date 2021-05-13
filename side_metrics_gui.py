import operator
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, \
    QTableView, QGridLayout, QLabel, QFormLayout, QLineEdit, QComboBox, QTableWidgetItem

from crew_funcs import *
from flight_funcs import *
from site_funcs import *


# --------------------------------
class site_expand_window(QWidget):
    def __init__(self, site):
        QWidget.__init__(self)
        grid = QGridLayout()

        location = QLabel(f'Location: {site[1]}')
        num_ac = QLabel(f'Number of Aircraft: {site[3]} ')
        aircraft_type = QLabel(f'Aircraft Type: {site[2]}')

        self.site_headers = get_site_query()
        self.site_data = site[7]

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda: self.display_site_main_window(main_window.site_main_window))

        grid.addWidget(location, 1, 0)
        grid.addWidget(num_ac, 2, 0)
        grid.addWidget(aircraft_type, 3, 0)
        grid.addWidget(back_button, 4, 0)

        self.setWindowTitle(f'Site: {site[1]}')
        self.setLayout(grid)

    @Slot()
    def display_site_main_window(self, window):
        window.show()
        # self.hide()
        self.close()


class flight_expand_window(QWidget):
    def __init__(self, flight):
        QWidget.__init__(self)
        grid = QGridLayout()
        grid.setSpacing(12)
        # self.setGeometry(400, 200, 700, 450)

        self.flight = flight

        id_label = QLabel(f'Flight Number: {self.flight[1]}')
        crew_added = QLabel(f'Aircraft Type: {self.flight[2]}')
        pilot_in_command = QLabel(f'Pilot in Command: {self.flight[4]}')
        take_off = QLabel(f'Takeoff: {self.flight[5]}')
        land = QLabel(f'Land: {self.flight[6]}')

        self.crew_headers = get_crew_column_query()
        crew_on_flight = self.flight[3]
        self.crew_data = get_crew_query({'employee_id': {'$in': crew_on_flight}}, {'currencies': 0})
        self.crew_table = self.TableModelCurrencies(self, self.crew_data, self.crew_headers)

        self.table_view = QTableView()
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
        font = QtGui.QFont("Courier New", 12)
        self.table_view.setFont(font)
        self.table_view.setModel(self.crew_table)
        self.table_view.resizeColumnsToContents()
        self.table_view.setSortingEnabled(True)
        self.table_view.hideColumn(0)
        self.table_view.hideColumn(3)
        self.table_view.hideColumn(7)

        back_button = QPushButton('Back')
        back_button.clicked.connect(
            lambda: self.display_flight_main_window(main_window.flight_main_window))

        add_crew_button = QPushButton('Add Crew')
        add_crew_button.clicked.connect(
            lambda: self.display_flight_crew_add_window(self.flight))

        grid.addWidget(self.table_view, 0, 1, 5, 5)
        grid.addWidget(id_label, 0, 0, 1, 1)
        grid.addWidget(take_off, 1, 0, 1, 1)
        grid.addWidget(land, 2, 0, 1, 1)
        grid.addWidget(pilot_in_command, 3, 0, 1, 1)
        grid.addWidget(crew_added, 4, 0, 1, 1)
        grid.addWidget(back_button, 5, 0, 1, 1)
        grid.addWidget(add_crew_button, 5, 1, 1, 1)

        self.setWindowTitle(f'Flight Number: {self.flight[1]}')
        self.setLayout(grid)

    @Slot()
    def display_flight_main_window(self, window):
        window.show()
        # self.hide()
        self.close()

    @Slot()
    def display_flight_crew_add_window(self, flight):
        self.flight_crew_add_window = flight_crew_add_window(flight)
        self.flight_crew_add_window.show()
        self.hide()

    class TableModelCurrencies(QtCore.QAbstractTableModel):
        def __init__(self, parent, the_data, the_h_headers):
            super(TableModelCurrencies, self).__init__(parent)
            self.the_data = the_data
            self.the_h_headers = the_h_headers

        def rowCount(self, parent):
            return len(self.the_data)

        def columnCount(self, parent):
            return len(self.the_data[0])

        def data(self, index, role):
            if not index.isValid():
                return None
            elif role != QtCore.Qt.DisplayRole:
                return None
            return self.the_data[index.row()][index.column()]

        def headerData(self, col, orientation, role):
            if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.the_h_headers[col]

        def sort(self, col, order):
            """sort table by given column number col"""
            self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
            self.the_data = sorted(self.the_data, key=operator.itemgetter(col))
            if order == QtCore.Qt.DescendingOrder:
                self.the_data.reverse()
            self.emit(QtCore.SIGNAL("layoutChanged()"))


class crew_expand_window(QWidget):
    def __init__(self, crew):
        QWidget.__init__(self)
        self.setGeometry(400, 200, 700, 450)
        self.setWindowTitle(f'{crew[1]} {crew[6]}: {crew[4]} {crew[5]} {crew[2]} {crew[3]}')

        grid = QGridLayout()
        grid.setSpacing(12)

        name_label = QLabel(f'Name: {crew[4]} {crew[5]} {crew[2]} {crew[3]}')
        id_label = QLabel(f'Employee Number: {crew[1]}')
        crew_pos_label = QLabel(f'Crew Position: {crew[6]}')

        self.crew_headers = get_crew_query({'employee_id': crew[1]})
        self.crew_data = self.crew_headers

        self.crew_h_headers = ['Currency', 'Last', 'Due']

        a_format = '%d %b, %Y'

        formatted_data = []

        currency_dates = self.crew_data[0][7]

        for date_set in currency_dates.items():
            for date in date_set[1:2]:
                formatted_data.append((date_set[0], date['Last'].strftime(a_format), date['Due'].strftime(a_format)))
        self.crew_data = formatted_data
        print(self.crew_data)

        self.crew_table_model = self.TableModelCurrencies(self, self.crew_data, self.crew_h_headers)
        self.table_view = QTableView()
        self.table_view.setModel(self.crew_table_model)
        font = QtGui.QFont("Courier New", 12)

        self.table_view.setFont(font)
        self.table_view.resizeColumnsToContents()

        self.table_view.setSortingEnabled(True)

        # self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.NoSelection)

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda: self.display_crew_main_window(main_window.crew_main_window))

        grid.addWidget(self.table_view, 0, 1, 3, 3)
        grid.addWidget(id_label, 0, 0)
        grid.addWidget(name_label, 1, 0)
        grid.addWidget(crew_pos_label, 2, 0)
        grid.addWidget(back_button, 3, 0)

        self.setLayout(grid)

    @Slot()
    def display_crew_main_window(self, window):
        window.show()
        # self.hide()
        self.close()

    class TableModelCurrencies(QtCore.QAbstractTableModel):
        def __init__(self, parent, the_data, the_h_headers):
            super(TableModelCurrencies, self).__init__(parent)
            self.the_data = the_data
            self.the_h_headers = the_h_headers

        def rowCount(self, parent):
            return len(self.the_data)

        def columnCount(self, parent):
            return len(self.the_data[0])

        def data(self, index, role):
            if not index.isValid():
                return None
            elif role != QtCore.Qt.DisplayRole:
                return None
            return self.the_data[index.row()][index.column()]

        def headerData(self, col, orientation, role):
            if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.the_h_headers[col]

        def sort(self, col, order):
            """sort table by given column number col"""
            self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
            self.the_data = sorted(self.the_data, key=operator.itemgetter(col))
            if order == QtCore.Qt.DescendingOrder:
                self.the_data.reverse()
            self.emit(QtCore.SIGNAL("layoutChanged()"))


# --------------------------------
class site_edit_window(QWidget):
    pass


class flight_edit_window(QWidget):
    pass


class crew_edit_window(QWidget):
    pass


# --------------------------------
class site_flight_add_window(QWidget):
    pass


class flight_crew_add_window(QWidget):
    def __init__(self, flight):
        QWidget.__init__(self)
        self.setGeometry(400, 200, 700, 450)
        self.setWindowTitle(f'Add Crew to Flight {flight[1]}')
        grid = QGridLayout()
        grid.setSpacing(12)

        self.headers = main_window.crew_main_window.crew_headers
        self.data = main_window.crew_main_window.crew_data

        self.crew_table = self.TableModel(self, self.crew_data, self.crew_headers)
        print(self.crew_table)

        self.table_view = QTableView()
        self.table_view.setModel(self.crew_table)
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
        font = QtGui.QFont("Courier New", 12)
        self.table_view.setFont(font)
        self.table_view.resizeColumnsToContents()
        self.table_view.setSortingEnabled(True)
        self.table_view.hideColumn(0)
        self.table_view.hideColumn(3)
        self.table_view.hideColumn(7)

        select_box = QTableWidgetItem()
        select_box.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        select_box.setCheckState(QtCore.Qt.Unchecked)

        back_button = QPushButton('Back')
        back_button.clicked.connect(
            lambda: self.display_flight_expand_window())

        grid.addWidget(self.table_view, 0, 0, 1, 1)
        grid.addWidget(back_button, 1, 0, 1, 1)

        self.setLayout(grid)

    def display_flight_expand_window(self):
        self.close()
        main_window.flight_main_window.flight_expand_window.show()

    class TableModel(QtCore.QAbstractTableModel):
        def __init__(self, parent, the_data, the_headers):
            QtCore.QAbstractTableModel.__init__(self, parent)
            self.the_data = the_data
            self.the_headers = the_headers

        def data(self, index, role):
            if not index.isValid():
                return None
            elif role != QtCore.Qt.DisplayRole:
                return None
            return self.the_data[index.row()][index.column()]

        def rowCount(self, parent):
            return len(self.the_data)

        def columnCount(self, parent):
            return len(self.the_headers)

        def headerData(self, col, orientation, role):
            if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.the_headers[col]
            return None

        def sort(self, col, order):
            """sort table by given column number col"""
            self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
            self.the_data = sorted(self.the_data, key=operator.itemgetter(col))
            if order == QtCore.Qt.DescendingOrder:
                self.the_data.reverse()
            self.emit(QtCore.SIGNAL("layoutChanged()"))


class crew_currency_add_window(QWidget):
    pass


# --------------------------------
class site_add_window(QWidget):
    pass


class flight_add_window(QWidget):
    pass


class crew_add_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # success popup

        grid = QGridLayout()

        details = gen_random_crew()
        print(details[3])

        self.emp_id = QLineEdit(str(details[4]))
        self.last_name = QLineEdit(details[2])
        self.first_name = QLineEdit(details[0])
        self.middle_name = QLineEdit(details[1])
        self.suffix = QLineEdit(details[3])
        self.crew_pos_list = ['P', 'SO', 'IP', 'ISO', 'EP', 'ESO']
        self.crew_position = QComboBox()
        self.crew_position.addItems(self.crew_pos_list)

        crew_add_form = QFormLayout()
        crew_add_form.addRow(self.tr('Employee Number:'), self.emp_id)
        crew_add_form.addRow(self.tr('&First Name:'), self.first_name)
        crew_add_form.addRow(self.tr('&Last Name:'), self.last_name)
        crew_add_form.addRow(self.tr('&Suffix:'), self.suffix)
        crew_add_form.addRow(self.tr('&Middle Name:'), self.middle_name)
        crew_add_form.addRow(self.tr('&Crew Position:'), self.crew_position)

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda: self.display_crew_main_window(main_window.crew_main_window))

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(lambda: self.add_crew())

        grid.addLayout(crew_add_form, 1, 1)
        grid.addWidget(back_button, 2, 1, )
        grid.addWidget(submit_button, 2, 2)

        self.setWindowTitle('Add New Crewmember')
        self.setLayout(grid)

    def add_crew(self):
        f_name = self.first_name.text()
        m_name = self.middle_name.text()
        l_name = self.last_name.text()
        suffix = self.suffix.text()
        employee_id = self.emp_id.text()
        crew_position = self.crew_position.currentText()

        value = [f_name, m_name, l_name, suffix, employee_id, crew_position]
        add_crew_members(value)

        self.emp_id.clear()
        self.last_name.clear()
        self.first_name.clear()
        self.middle_name.clear()
        self.suffix.clear()

    def display_crew_main_window(self, window):
        window.show()
        self.close()


# --------------------------------
class site_main_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.site_add_window = site_add_window()

        grid = QGridLayout()
        grid.setSpacing(12)
        self.setGeometry(400, 200, 700, 450)
        self.setWindowTitle('Sites')

        self.site_headers = get_site_column_query()
        self.site_data = get_site_query()
        self.site_table = self.TableModel(self, self.site_data, self.site_headers)

        self.table_view = QTableView()
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
        font = QtGui.QFont("Courier New", 12)
        self.table_view.setFont(font)
        self.table_view.setModel(self.site_table)
        self.table_view.resizeColumnsToContents()
        self.table_view.setSortingEnabled(True)
        self.table_view.hideColumn(0)
        self.table_view.hideColumn(5)
        self.table_view.hideColumn(7)
        self.table_view.hideColumn(8)

        view_site_button = QPushButton('View Site')
        view_site_button.clicked.connect(lambda: self.display_site_expand_window())

        add_site_button = QPushButton('Add Site')
        add_site_button.clicked.connect(lambda: self.display_site_add_window(self.site_add_window))

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda checked: self.display_main_window(main_window))

        test_button = QPushButton('Test')
        test_button.clicked.connect(lambda: print(self.site_table.the_data[self.table_view.currentIndex().row()]))
        grid.addWidget(test_button, 4, 1, 1, 2)

        grid.addWidget(view_site_button, 1, 1, 1, 1)
        grid.addWidget(add_site_button, 1, 2, 1, 1)
        grid.addWidget(self.table_view, 2, 1, 1, 2)
        grid.addWidget(back_button, 3, 1, 1, 2)

        self.setLayout(grid)

    @Slot()
    def display_main_window(self, window):
        window.show()
        self.hide()

    @Slot()
    def display_site_expand_window(self):
        self.site = self.site_table.the_data[self.table_view.currentIndex().row()]
        self.site_expand_window = site_expand_window(self.site)
        self.site_expand_window.show()
        self.hide()

    @Slot()
    def display_site_add_window(self, window):
        window.show()
        self.hide()

    class TableModel(QtCore.QAbstractTableModel):
        def __init__(self, parent, the_data, the_headers):
            QtCore.QAbstractTableModel.__init__(self, parent)
            self.the_data = the_data
            self.the_headers = the_headers

        def data(self, index, role):
            if not index.isValid():
                return None
            elif role != QtCore.Qt.DisplayRole:
                return None
            return self.the_data[index.row()][index.column()]

        def rowCount(self, parent):
            return len(self.the_data)

        def columnCount(self, parent):
            return len(self.the_headers)

        def headerData(self, col, orientation, role):
            if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.the_headers[col]
            return None

        def sort(self, col, order):
            """sort table by given column number col"""
            self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
            self.the_data = sorted(self.the_data, key=operator.itemgetter(col))
            if order == QtCore.Qt.DescendingOrder:
                self.the_data.reverse()
            self.emit(QtCore.SIGNAL("layoutChanged()"))


class flight_main_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(400, 200, 700, 450)
        self.setWindowTitle('Flights')
        grid = QGridLayout()
        grid.setSpacing(12)

        self.flight_headers = get_flight_column_query()
        self.flight_data = get_flight_query()

        a_format = '%d%b%Y - %H%M'

        formatted_dates = []
        flight_times = [flight[5:7] for flight in self.flight_data]
        for flight in flight_times:
            for times in flight:
                times = times.strftime(a_format)
                formatted_dates.append(times)

        self.flight_data[0][5] = formatted_dates[0]
        self.flight_data[0][6] = formatted_dates[1]

        self.flight_table = self.TableModel(self, self.flight_data, self.flight_headers)

        self.table_view = QTableView()
        self.table_view.setModel(self.flight_table)
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
        font = QtGui.QFont("Courier New", 12)
        self.table_view.setFont(font)
        self.table_view.resizeColumnsToContents()
        self.table_view.setSortingEnabled(True)
        self.table_view.hideColumn(0)
        self.table_view.hideColumn(3)
        self.table_view.hideColumn(4)

        view_flight_button = QPushButton('View Flight')
        view_flight_button.clicked.connect(
            lambda: self.display_flight_expand_window())

        add_flight_button = QPushButton('Add Flight')
        add_flight_button.clicked.connect(
            lambda: self.display_flight_add_window())

        back_button = QPushButton('Back')
        back_button.clicked.connect(
            lambda: self.display_main_window(main_window))

        test_button = QPushButton('Test')
        test_button.clicked.connect(
            lambda: print(self.flight_table.the_data[self.table_view.currentIndex().row()]))

        grid.addWidget(view_flight_button, 1, 1, 1, 1)
        grid.addWidget(add_flight_button, 1, 2, 1, 1)
        grid.addWidget(self.table_view, 2, 1, 1, 2)
        grid.addWidget(back_button, 3, 1, 1, 2)
        grid.addWidget(test_button, 4, 1, 1, 2)

        self.setLayout(grid)

    @Slot()
    def display_main_window(self, window):
        window.show()
        self.hide()

    @Slot()
    def display_flight_expand_window(self):
        self.flight = self.flight_table.the_data[self.table_view.currentIndex().row()]
        self.flight_expand_window = flight_expand_window(self.flight)
        self.flight_expand_window.show()
        self.hide()

    @Slot()
    def display_flight_add_window(self):
        self.flight_add_window = flight_add_window()
        self.flight_add_window.show()
        self.hide()

    class TableModel(QtCore.QAbstractTableModel):
        def __init__(self, parent, the_data, the_headers):
            QtCore.QAbstractTableModel.__init__(self, parent)
            self.the_data = the_data
            self.the_headers = the_headers

        def data(self, index, role):
            if not index.isValid():
                return None
            elif role != QtCore.Qt.DisplayRole:
                return None
            return self.the_data[index.row()][index.column()]

        def rowCount(self, parent):
            return len(self.the_data)

        def columnCount(self, parent):
            return len(self.the_headers)

        def headerData(self, col, orientation, role):
            if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.the_headers[col]
            return None

        def sort(self, col, order):
            """sort table by given column number col"""
            self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
            self.the_data = sorted(self.the_data, key=operator.itemgetter(col))
            if order == QtCore.Qt.DescendingOrder:
                self.the_data.reverse()
            self.emit(QtCore.SIGNAL("layoutChanged()"))


class crew_main_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        grid = QGridLayout()
        grid.setSpacing(12)
        self.setGeometry(400, 200, 700, 450)
        self.setWindowTitle('Crews')

        self.crew_headers = get_crew_column_query({}, {'currencies': 0})
        self.crew_data = get_crew_query({}, {'currencies': 0})
        self.crew_table = self.TableModel(self, self.crew_data, self.crew_headers)

        self.table_view = QTableView()
        self.table_view.setModel(self.crew_table)
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
        font = QtGui.QFont("Courier New", 12)
        self.table_view.setFont(font)
        self.table_view.resizeColumnsToContents()
        self.table_view.setSortingEnabled(True)
        self.table_view.hideColumn(0)
        self.table_view.hideColumn(3)
        self.table_view.hideColumn(7)

        view_crew_button = QPushButton('View Crew')
        view_crew_button.clicked.connect(
            lambda: self.display_crew_expand_window())

        add_crew_button = QPushButton('Add Crew')
        add_crew_button.clicked.connect(
            lambda: self.display_crew_add_window())

        back_button = QPushButton('Back')
        back_button.clicked.connect(
            lambda: self.display_main_window(main_window))

        test_button = QPushButton('Test')
        test_button.clicked.connect(
            lambda: print(self.crew_table.the_data[self.table_view.currentIndex().row()]))

        grid.addWidget(view_crew_button, 1, 1, 1, 1)
        grid.addWidget(add_crew_button, 1, 2, 1, 1)
        grid.addWidget(self.table_view, 2, 1, 1, 2)
        grid.addWidget(back_button, 3, 1, 1, 2)
        grid.addWidget(test_button, 4, 1, 1, 2)

        self.setLayout(grid)

    @Slot()
    def display_main_window(self, window):
        window.show()
        self.hide()

    @Slot()
    def display_crew_expand_window(self):
        self.crew = self.crew_table.the_data[self.table_view.currentIndex().row()]
        self.crew_expand_window = crew_expand_window(self.crew)
        self.crew_expand_window.show()
        self.hide()

    @Slot()
    def display_crew_add_window(self):
        self.crew_add_window = crew_add_window()
        self.crew_add_window.show()
        self.hide()

    class TableModel(QtCore.QAbstractTableModel):
        def __init__(self, parent, the_data, the_headers):
            QtCore.QAbstractTableModel.__init__(self, parent)
            self.the_data = the_data
            self.the_headers = the_headers

        def data(self, index, role):
            if not index.isValid():
                return None
            elif role != QtCore.Qt.DisplayRole:
                return None
            return self.the_data[index.row()][index.column()]

        def rowCount(self, parent):
            return len(self.the_data)

        def columnCount(self, parent):
            return len(self.the_headers)

        def headerData(self, col, orientation, role):
            if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.the_headers[col]
            return None

        def sort(self, col, order):
            """sort table by given column number col"""
            self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
            self.the_data = sorted(self.the_data, key=operator.itemgetter(col))
            if order == QtCore.Qt.DescendingOrder:
                self.the_data.reverse()
            self.emit(QtCore.SIGNAL("layoutChanged()"))


# main is assigned to the InitialWindow class to begin the application loop
class InitialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.site_main_window = site_main_window()
        self.flight_main_window = flight_main_window()
        self.crew_main_window = crew_main_window()

        grid = QGridLayout()
        grid.setSpacing(10)
        self.setWindowTitle('Metrics Tracker')

        main_site_button = QPushButton('Sites')
        main_site_button.clicked.connect(lambda: self.display_site_main_window(self.site_main_window))

        main_flight_button = QPushButton('Flights')
        main_flight_button.clicked.connect(lambda: self.display_flight_main_window(self.flight_main_window))

        main_crew_button = QPushButton('Crews')
        main_crew_button.clicked.connect(lambda: self.display_crew_main_window(self.crew_main_window))

        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(lambda: self.close())

        grid.addWidget(main_site_button, 1, 1)
        grid.addWidget(main_flight_button, 1, 2)
        grid.addWidget(main_crew_button, 1, 3)
        grid.addWidget(quit_button, 2, 1, 1, 3)

        main_frame = QWidget()

        main_frame.setLayout(grid)
        self.setCentralWidget(main_frame)

    @Slot()
    def display_site_main_window(self, window):
        window.show()
        self.hide()

    @Slot()
    def display_flight_main_window(self, window):
        window.show()
        self.hide()

    @Slot()
    def display_crew_main_window(self, window):
        window.show()
        self.hide()


if __name__ == '__main__':
    # Creates the Metrics Tracker application
    metrics_tracker = QApplication(sys.argv)

    # Create and show the main window, based on the InitialWindow Class
    main_window = InitialWindow()
    main_window.show()

    # Begins the main application loop
    metrics_tracker.exec_()
