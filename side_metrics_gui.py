import operator
import sys

from PySide6 import QtCore
from PySide6.QtCore import Slot, Qt, QPersistentModelIndex, QAbstractTableModel
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, \
    QTableView, QGridLayout, QLabel, QFormLayout, QLineEdit, QComboBox, QCheckBox, QVBoxLayout, \
    QAbstractItemView

from flight_funcs import *
from site_funcs import *

# flight_date_format = '%m/%d/%YT%H%M'
flight_date_format = '%Y-%m-%dT%H:%M:00'
currency_date_format = '%d %b, %Y'


# --------------------------------
class site_expand_window(QWidget):
    def __init__(self, site):
        QWidget.__init__(self)
        grid = QGridLayout()
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 600, 150)

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
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 600, 150)

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

        grid.addWidget(self.table_view, 0, 1, 5, 2)
        grid.addWidget(id_label, 0, 0, 1, 1)
        grid.addWidget(take_off, 1, 0, 1, 1)
        grid.addWidget(land, 2, 0, 1, 1)
        grid.addWidget(pilot_in_command, 3, 0, 1, 1)
        grid.addWidget(crew_added, 4, 0, 1, 1)
        grid.addWidget(back_button, 5, 0, 1, 1)
        grid.addWidget(add_crew_button, 5, 1, 1, 2)

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
            super().__init__(parent)
            self.the_data = the_data
            self.the_h_headers = the_h_headers

        def rowCount(self, parent):
            try:
                return len(self.the_data)
            except IndexError:
                return 0

        def columnCount(self, parent):
            try:
                return len(self.the_data[0])
            except IndexError:
                return 0

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
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 640, 360)
        self.setWindowTitle(f'{crew[1]} {crew[6]}: {crew[4]} {crew[5]} {crew[2]} {crew[3]}')

        grid = QGridLayout()
        grid.setSpacing(12)

        name_label = QLabel(f'Name: {crew[4]} {crew[5]} {crew[2]} {crew[3]}')
        id_label = QLabel(f'Employee Number: {crew[1]}')
        crew_pos_label = QLabel(f'Crew Position: {crew[6]}')

        self.crew_headers = get_crew_query({'employee_id': crew[1]})
        self.crew_data = self.crew_headers

        self.crew_h_headers = ['Currency', 'Last', 'Due']

        formatted_data = []

        currency_dates = self.crew_data[0][7]

        for date_set in currency_dates.items():
            for date in date_set[1:2]:
                formatted_data.append((date_set[0],
                                       date['Last'].strftime(currency_date_format),
                                       date['Due'].strftime(currency_date_format)))
        self.crew_data = formatted_data

        self.crew_table_model = self.TableModelCurrencies(self, self.crew_data, self.crew_h_headers)
        self.table_view = QTableView()
        self.table_view.setModel(self.crew_table_model)
        self.table_view.resizeColumnsToContents()

        self.table_view.setSortingEnabled(True)

        # self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.NoSelection)

        self.takeoff = QLineEdit('Add Calendar')
        self.sortie = QLineEdit('Add Calendar')
        self.nose_ir = QLineEdit('Add Calendar')
        self.mts_ir = QLineEdit('Add Calendar')
        self.launch_procedures = QLineEdit('Add Calendar')
        self.landing = QLineEdit('Add Calendar')
        self.instrument_approach = QLineEdit('Add Calendar')
        self.evaluation = QLineEdit('Add Calendar')

        currency_add_form = QFormLayout()
        currency_add_form.addRow(self.tr('Takeoff:'), self.takeoff)
        currency_add_form.addRow(self.tr('Sortie:'), self.sortie)
        currency_add_form.addRow(self.tr('Nose IR:'), self.nose_ir)
        currency_add_form.addRow(self.tr('MTS IR:'), self.mts_ir)
        currency_add_form.addRow(self.tr('Launch Procedures:'), self.launch_procedures)
        currency_add_form.addRow(self.tr('Landing:'), self.landing)
        currency_add_form.addRow(self.tr('Instrument Approach:'), self.instrument_approach)
        currency_add_form.addRow(self.tr('Evaluation:'), self.evaluation)

        submit_button = QPushButton('Submit')

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda: self.display_crew_main_window(main_window.crew_main_window))

        grid.addWidget(name_label, 1, 1, 1, 1)
        grid.addWidget(crew_pos_label, 1, 2, 1, 1)
        grid.addWidget(self.table_view, 2, 1, 1, 1)
        grid.addLayout(currency_add_form, 2, 2, 1, 1)
        grid.addWidget(back_button, 3, 1, 1, 3)

        self.setLayout(grid)

    @Slot()
    def display_crew_main_window(self, window):
        window.show()
        # self.hide()
        self.close()

    def display_crew_currency_add_window(self, crew):
        self.crew_currency_add_window = crew_currency_add_window(crew)
        self.crew_currency_add_window.show()
        self.hide()

    class TableModelCurrencies(QtCore.QAbstractTableModel):
        def __init__(self, parent, the_data, the_headers):
            QtCore.QAbstractTableModel.__init__(self, parent)
            self.the_data = the_data
            self.the_headers = the_headers

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
                return self.the_headers[col]

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
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 700, 450)
        self.setWindowTitle(f'Add Crew to Flight {flight[1]}')

        self.headers = main_window.crew_main_window.crew_headers
        self.data = main_window.crew_main_window.crew_data

        self.table_view = QTableView()
        self.crew_table = self.TableModel(self, self.data, self.headers)
        self.table_view.setModel(self.crew_table)
        # self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSortingEnabled(True)

        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
        self.table_view.resizeColumnsToContents()
        self.table_view.hideColumn(1)
        self.table_view.hideColumn(4)
        self.table_view.hideColumn(6)

        back_button = QPushButton('Back')
        back_button.clicked.connect(
            lambda: self.display_flight_expand_window())

        layout = QVBoxLayout(self)
        layout.addWidget(self.table_view)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def display_flight_expand_window(self):
        self.close()
        main_window.flight_main_window.flight_expand_window.show()

    class TableModel(QtCore.QAbstractTableModel):
        def __init__(self, parent, the_data, the_headers, *args):
            QtCore.QAbstractTableModel.__init__(self, parent, *args)
            self.the_data = the_data
            self.the_headers = the_headers

        def rowCount(self, parent):
            return len(self.the_data)

        def columnCount(self, parent):
            return len(self.the_headers)

        def data(self, index, role):
            if not index.isValid():
                return None
            if index.column() == 0:
                value = self.the_data[index.row()]
            else:
                value = self.the_data[index.row()][index.column()]
            if role == QtCore.Qt.EditRole:
                return value
            elif role == QtCore.Qt.DisplayRole:
                return value
            elif role != QtCore.Qt.DisplayRole:
                return None

            elif role == QtCore.Qt.CheckStateRole:
                if index.column() == 0:
                    if self.the_data[index.row()][index.column()].isChecked():
                        return QtCore.Qt.Checked
                    else:
                        return QtCore.Qt.Unchecked

            return self.the_data[index.row()][index.column()]

        def headerData(self, col, orientation, role):
            if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.the_headers[col]
            return None

        def sort(self, col, order):
            """sort table by given column number col"""
            if col != 0:
                self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
                self.the_data = sorted(self.the_data, key=operator.itemgetter(col))
                if order == QtCore.Qt.DescendingOrder:
                    self.the_data.reverse()
                self.emit(QtCore.SIGNAL("layoutChanged()"))

        def setData(self, index, value, role=Qt.EditRole):
            if not index.isValid():
                return False
            if role == Qt.CheckStateRole:
                self.checks[QPersistentModelIndex(index)] = value
                return True
            return False

        def flags(self, index):
            flags = QAbstractTableModel.flags(self, index)
            if index.column() == 0:
                flags |= Qt.ItemIsEditable | Qt.ItemIsUserCheckable
            return flags


class crew_currency_add_window(QWidget):
    def __init__(self, crew_member):
        QWidget.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 700, 450)
        self.setWindowTitle(f'{crew_member[3]}\'s Currency Page')

        self.headers = main_window.crew_main_window.crew_headers
        self.data = main_window.crew_main_window.crew_data

        self.crew_table = self.TableModel(self, self.data, self.headers)
        self.table_view = QTableView()
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setModel(self.crew_table)
        self.table_view.setSortingEnabled(True)

        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
        self.table_view.resizeColumnsToContents()
        self.table_view.hideColumn(1)
        self.table_view.hideColumn(4)
        self.table_view.hideColumn(6)

        back_button = QPushButton('Back')
        back_button.clicked.connect(
            lambda: self.display_flight_expand_window())

        layout = QVBoxLayout(self)
        layout.addWidget(self.table_view)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def display_crew_expand_window(self):
        self.close()
        main_window.crew_main_window.crew_expand_window.show()

    class TableModel(QtCore.QAbstractTableModel):
        def __init__(self, parent, the_data, the_headers, *args):
            QtCore.QAbstractTableModel.__init__(self, parent, *args)
            self.the_data = the_data
            self.the_headers = the_headers

            checkbox = QCheckBox()
            checkbox.setChecked(True)

            self.the_headers.insert(0, ' ')
            for crew_member in self.the_data:
                crew_member.insert(0, checkbox)

        def rowCount(self, parent):
            return len(self.the_data)

        def columnCount(self, parent):
            return len(self.the_headers)

        def data(self, index, role):
            if not index.isValid():
                return None
            if index.column() == 0:
                value = self.the_data[index.row()][index.column()].text()
            else:
                value = self.the_data[index.row()][index.column()]

            if role == QtCore.Qt.EditRole:
                return value
            elif role == QtCore.Qt.DisplayRole:
                return value
            elif role != QtCore.Qt.DisplayRole:
                return None

            elif role == QtCore.Qt.CheckStateRole:
                if index.column() == 0:
                    if self.the_data[index.row()][index.column()].isChecked():
                        return QtCore.Qt.Checked
                    else:
                        return QtCore.Qt.Unchecked

            return self.the_data[index.row()][index.column()]

        def headerData(self, col, orientation, role):
            if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.the_headers[col]
            return None

        def sort(self, col, order):
            """sort table by given column number col"""
            if col != 0:
                self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
                self.the_data = sorted(self.the_data, key=operator.itemgetter(col))
                if order == QtCore.Qt.DescendingOrder:
                    self.the_data.reverse()
                self.emit(QtCore.SIGNAL("layoutChanged()"))

        def flags(self, index):
            if not index.isValid():
                return None
            if index.column() == 0:
                return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable
            else:
                return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

        def setData(self, index, value, role):
            if not index.isValid():
                return False
            if role == QtCore.Qt.CheckStateRole and index.column() == 0:
                print(">>> setData() role = ", role)
                print(">>> setData() index.column() = ", index.column())
                if value == QtCore.Qt.Checked:
                    self.the_data[index.row()][index.column()].setChecked(True)
                else:
                    self.the_data[index.row()][index.column()].setChecked(False)
            else:
                print(">>> setData() role = ", role)
                print(">>> setData() index.column() = ", index.column())

            print(">>> setData() index.row = ", index.row())
            print(">>> setData() index.column = ", index.column())
            self.dataChanged.emit(index, index)
            return True


# --------------------------------
class site_add_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        grid = QGridLayout()
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 600, 150)
        self.setWindowTitle('Add New Site')
        # success popup

        details = gen_random_site()

        self.location = QLineEdit(details[0])
        self.aircraft_type = QLineEdit(details[1])
        self.aircraft_assigned = QLineEdit(details[2])
        self.required_staff = QLineEdit(details[3])
        self.present_staff = QLineEdit(details[4])

        self.site_add_form = QFormLayout()

        self.site_add_form.addRow(self.tr('Location:'), self.location)
        self.site_add_form.addRow(self.tr('Aircraft Type:'), self.aircraft_type)
        self.site_add_form.addRow(self.tr('Assets:'), self.aircraft_assigned)
        self.site_add_form.addRow(self.tr('Required Staff:'), self.required_staff)
        self.site_add_form.addRow(self.tr('Present Staff:'), self.present_staff)

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda: self.display_site_main_window(main_window.site_main_window))

        random_button = QPushButton('Random')
        random_button.clicked.connect(lambda: self.randomize())

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(lambda: self.add_site())

        grid.addLayout(self.site_add_form, 1, 1, 1, 3)
        grid.addWidget(back_button, 2, 1, 1, 1)
        grid.addWidget(random_button, 2, 2, 1, 1)
        grid.addWidget(submit_button, 2, 3, 1, 1)

        self.setLayout(grid)

    @Slot()
    def randomize(self):
        self.close()
        site_main_window.site_add_window = site_add_window()
        site_main_window.site_add_window.show()

    def add_site(self):
        location = self.location.text()
        aircraft_type = self.aircraft_type.text()
        assets = self.assets.text()
        present_staff = self.present_staff.text()
        required_staff = self.crew_position.currentText()

        value = [location, aircraft_type, assets, present_staff, required_staff]
        add_site(value)

        self.emp_id.clear()
        self.last_name.clear()
        self.first_name.clear()
        self.middle_name.clear()
        self.suffix.clear()

    def display_site_main_window(self, window):
        window.show()
        self.close()


class flight_add_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        grid = QGridLayout()
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 380, 100)
        self.setWindowTitle('Add New Flight')
        # success popup

        self.details = gen_random_flight()

        self.flight_number = QLineEdit(str(self.details[0]))
        self.aircraft_type = QLineEdit(self.details[1])
        self.crew_on_flight = []
        self.pilot_in_command = ''
        self.scheduled_takeoff = QLineEdit(str(self.details[2]))
        self.scheduled_land = QLineEdit(str(self.details[3]))

        flight_add_form = QFormLayout()
        flight_add_form.addRow(self.tr('Flight Number:'), self.flight_number)
        flight_add_form.addRow(self.tr('Aircraft Type:'), self.aircraft_type)
        flight_add_form.addRow(self.tr('Scheduled Takeoff:'), self.scheduled_takeoff)
        flight_add_form.addRow(self.tr('Scheduled Land:'), self.scheduled_land)

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda: self.display_flight_main_window(main_window.flight_main_window))

        random_button = QPushButton('Random')
        random_button.clicked.connect(lambda: self.randomize())

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(lambda: self.add_flight())

        grid.addLayout(flight_add_form, 1, 1, 1, 3)
        grid.addWidget(back_button, 2, 1, 1, 1)
        grid.addWidget(random_button, 2, 2, 1, 1)
        grid.addWidget(submit_button, 2, 3, 1, 1)

        self.setLayout(grid)

    @Slot()
    def randomize(self):
        self.close()
        flight_main_window.flight_add_window = flight_add_window()
        flight_main_window.flight_add_window.show()

    @Slot()
    def add_flight(self):
        flight_num = self.flight_number.text()
        aircraft_type = self.aircraft_type.text()
        scheduled_takeoff = self.scheduled_takeoff.text()
        scheduled_land = self.scheduled_land.text()

        scheduled_takeoff = datetime.strptime(scheduled_takeoff.replace(scheduled_takeoff[10], 'T'), flight_date_format)
        scheduled_land = datetime.strptime(scheduled_land.replace(scheduled_land[10], 'T'), flight_date_format)

        value = [flight_num, aircraft_type, self.crew_on_flight,
                 self.pilot_in_command, scheduled_takeoff, scheduled_land]
        add_flight(value)

        self.flight_number.clear()
        self.aircraft_type.clear()
        self.scheduled_takeoff.clear()
        self.scheduled_land.clear()

        self.close()
        flight_main_window.flight_add_window = flight_add_window()
        flight_main_window.flight_add_window.show()

    @Slot()
    def display_flight_main_window(self, window):
        window.show()
        self.close()


class crew_add_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        grid = QGridLayout()
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 600, 150)
        self.setWindowTitle('Add New Crew')
        # success popup

        details = gen_random_crew()

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
        crew_add_form.addRow(self.tr('First Name:'), self.first_name)
        crew_add_form.addRow(self.tr('Last Name:'), self.last_name)
        crew_add_form.addRow(self.tr('Suffix:'), self.suffix)
        crew_add_form.addRow(self.tr('Middle Name:'), self.middle_name)
        crew_add_form.addRow(self.tr('Crew Position:'), self.crew_position)

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda: self.display_crew_main_window(main_window.crew_main_window))

        random_button = QPushButton('Random')
        random_button.clicked.connect(lambda: self.randomize())

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(lambda: self.add_crew())

        grid.addLayout(crew_add_form, 1, 1, 1, 3)
        grid.addWidget(back_button, 2, 1, 1, 1)
        grid.addWidget(random_button, 2, 2, 1, 1)
        grid.addWidget(submit_button, 2, 3, 1, 1)

        self.setLayout(grid)

    @Slot()
    def randomize(self):
        self.close()
        crew_main_window.crew_add_window = crew_add_window()
        crew_main_window.crew_add_window.show()

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
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 400, 300)
        self.setWindowTitle('Sites')

        self.site_headers = get_site_column_query()
        self.site_data = get_site_query()
        self.site_table = self.TableModel(self, self.site_data, self.site_headers)

        self.table_view = QTableView()
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
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
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 440, 300)
        self.setWindowTitle('Flights')
        grid = QGridLayout()
        grid.setSpacing(12)

        self.flight_headers = get_flight_column_query()
        self.flight_data = get_flight_query()

        for flight in self.flight_data:
            flight[5] = str(flight[5])
            flight[6] = str(flight[6])

        self.flight_table = self.TableModel(self, self.flight_data, self.flight_headers)

        self.table_view = QTableView()
        self.table_view.setModel(self.flight_table)
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
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

        grid.addWidget(view_flight_button, 1, 1, 1, 1)
        grid.addWidget(add_flight_button, 1, 2, 1, 1)
        grid.addWidget(self.table_view, 2, 1, 1, 2)
        grid.addWidget(back_button, 3, 1, 1, 2)

        self.setLayout(grid)

    @Slot()
    def display_main_window(self, window):
        window.show()
        self.hide()

    @Slot()
    def display_flight_expand_window(self):
        flight = self.flight_table.the_data[self.table_view.currentIndex().row()]
        self.flight_expand_window = flight_expand_window(flight)
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
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 440, 520)
        self.setWindowTitle('Crews')

        self.crew_headers = get_crew_column_query({}, {'currencies': 0})
        self.crew_data = get_crew_query({}, {'currencies': 0})
        self.crew_table = self.TableModel(self, self.crew_data, self.crew_headers)

        self.table_view = QTableView()
        self.table_view.setModel(self.crew_table)
        self.table_view.setSelectionBehavior(self.table_view.SelectRows)
        self.table_view.setSelectionMode(self.table_view.ContiguousSelection)
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

        grid.addWidget(view_crew_button, 1, 1, 1, 1)
        grid.addWidget(add_crew_button, 1, 2, 1, 1)
        grid.addWidget(self.table_view, 2, 1, 1, 2)
        grid.addWidget(back_button, 3, 1, 1, 2)

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
        # Custom model

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

        #def insertRows(self):
            #row_count = len(self.the_data)
            #self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
            #empty_data = {key: None for key in self.the_headers if not key == '_id'}
            #document_id =
            #new_data =
            #self.the_data.append(new_data)
            #row_count += 1
            #self.endInsertRows()
            #return True


# main is assigned to the InitialWindow class to begin the application loop
class InitialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Metrics Tracker')
        self.setGeometry(70, 150, 200, 70)

        grid = QGridLayout()
        grid.setSpacing(10)

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

        self.site_main_window = site_main_window()
        self.flight_main_window = flight_main_window()
        self.crew_main_window = crew_main_window()

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
    metrics_tracker.exec()

# TODO create DB for aircraft type and relevant details such as max flight time
