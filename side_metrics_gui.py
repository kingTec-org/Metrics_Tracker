import operator
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Slot
from PySide6.QtWidgets import \
    QMainWindow, QVBoxLayout, \
    QApplication, \
    QWidget, QPushButton, \
    QTableView, QGridLayout

from flight_funcs import *
from site_funcs import *


# --------------------------------
class site_expand_window(QWidget):
    pass


class flight_expand_window(QWidget):
    pass


class crew_expand_window(QWidget):
    def __init__(self, crew_member=None):
        QWidget.__init__(self)
        self.crew_member = crew_member

        grid = QGridLayout()
        self.setWindowTitle('Personnel Information')

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda: self.display_crew_main_window(main_window.crew_main_window))

        print_button = QPushButton('Print')
        print_button.clicked.connect(lambda: print(self.crew_member))

        grid.addWidget(back_button, 0, 0)
        grid.addWidget(print_button, 1, 0)

        self.setLayout(grid)

    @Slot()
    def crew_expand_label(self):
        pass

    @Slot()
    def display_crew_main_window(self, window):
        window.show()
        self.hide()


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
    pass


class crew_currency_add_window(QWidget):
    pass


# --------------------------------
class site_add_window(QWidget):
    pass


class fight_add_window(QWidget):
    pass


class crew_add_window(QWidget):
    pass


# --------------------------------
class site_main_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(400, 200, 700, 450)
        self.setWindowTitle('Sites')

        excluded_fields = None
        site_headers = get_site_column_query(excluded_fields)
        site_data = get_site_query(excluded_fields)

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda checked: self.display_main_window(main_window))

        site_table = TableModel(self, site_data, site_headers)
        table_view = QTableView()
        table_view.setModel(site_table)

        font = QtGui.QFont("Courier New", 14)
        table_view.setFont(font)

        table_view.resizeColumnsToContents()

        table_view.setSortingEnabled(True)
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        layout.addWidget(back_button)
        self.setLayout(layout)

    def display_main_window(self, window):
        window.show()
        self.hide()


class flight_main_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(400, 200, 900, 450)
        self.setWindowTitle('Flights')

        excluded_fields = '_id', 'crew_on_flight'
        flight_headers = get_flight_column_query(excluded_fields)
        flight_data = get_flight_query(excluded_fields)

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda checked: self.display_main_window(main_window))

        flight_table = TableModel(self, flight_data, flight_headers)
        table_view = QTableView()
        table_view.setModel(flight_table)

        font = QtGui.QFont("Courier New", 14)
        table_view.setFont(font)

        table_view.resizeColumnsToContents()

        table_view.setSortingEnabled(True)
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        layout.addWidget(back_button)
        self.setLayout(layout)

    def display_main_window(self, window):
        window.show()
        self.hide()


class crew_main_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.crew_add_window = crew_add_window()

        grid = QGridLayout()
        grid.setSpacing(10)
        self.setGeometry(400, 200, 700, 450)
        self.setWindowTitle('Crews')

        crew_headers = get_crew_column_query()
        crew_data = get_crew_query()
        crew_table = TableModel(self, crew_data, crew_headers)

        table_view = QTableView()
        table_view.setSelectionBehavior(table_view.SelectRows)
        table_view.setSelectionMode(table_view.ContiguousSelection)
        font = QtGui.QFont("Courier New", 14)
        table_view.setFont(font)
        table_view.setModel(crew_table)
        table_view.resizeColumnsToContents()
        table_view.setSortingEnabled(True)
        table_view.hideColumn(0)
        table_view.hideColumn(3)
        table_view.adjustSize()
        table_view.sizeAdjustPolicy()


        #
        #
        #
        #
        #
        # issue is that idx is running when the instance is created, being assinged -1 and passing that to the expand window instead of actual idx
        self.idx = table_view.currentIndex().row()
        self.crew = crew_table.crew_data[self.idx]

        self.crew_expand_window = crew_expand_window(self.crew)

        view_crew_button = QPushButton('View Crew')
        view_crew_button.clicked.connect(lambda: print(self.idx))
        view_crew_button.clicked.connect(lambda: self.display_crew_expand_window(self.crew_expand_window))

        add_crew_button = QPushButton('Add Crew')
        add_crew_button.clicked.connect(lambda: self.display_crew_add_window(self.crew_add_window))

        back_button = QPushButton('Back')
        back_button.clicked.connect(lambda: self.display_main_window(main_window))

        test_button = QPushButton('Test')
        test_button.clicked.connect(lambda: print(crew_table.crew_data[table_view.currentIndex().row()]))

        grid.addWidget(test_button, 4, 1, 1, 2)

        grid.addWidget(view_crew_button, 1, 1, 1, 1)
        grid.addWidget(add_crew_button, 1, 2, 1, 1)
        grid.addWidget(table_view, 2, 1, 1, 2)
        grid.addWidget(back_button, 3, 1, 1, 2)

        self.setLayout(grid)

    @Slot()
    def display_main_window(self, window):
        window.show()
        self.hide()

    @Slot()
    def display_crew_expand_window(self, window):
        window.show()
        self.hide()

    @Slot()
    def display_crew_add_window(self, window):
        window.show()
        self.hide()


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, crew_data, crew_headers):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.crew_data = crew_data
        self.crew_headers = crew_headers

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.crew_data[index.row()][index.column()]

    def rowCount(self, parent):
        return len(self.crew_data)

    def columnCount(self, parent):
        return len(self.crew_headers)

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.crew_headers[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        self.crew_data = sorted(self.crew_data, key=operator.itemgetter(col))
        if order == QtCore.Qt.DescendingOrder:
            self.crew_data.reverse()
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
