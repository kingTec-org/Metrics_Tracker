import operator

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import \
    QMainWindow, QVBoxLayout, \
    QHBoxLayout, \
    QLabel, QApplication, \
    QWidget, QPushButton, \
    QTableView

from crew_funcs import *


# --------------------------------
class site_expand_window(QWidget):
    pass


class flight_expand_window(QWidget):
    pass


class crew_expand_window(QWidget):
    pass

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
    """
     This "window" is a QWidget. If it has no parent,
     it will appear as a free-floating window.
     """

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.label = QLabel("Sites")
        layout.addWidget(self.label)
        self.setLayout(layout)


class flight_main_window(QWidget):
    """
     This "window" is a QWidget. If it has no parent,
     it will appear as a free-floating window.
     """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Flights")
        layout.addWidget(self.label)
        self.setLayout(layout)


class crew_main_window(QWidget):
    def __init__(self, crew_data, crew_headers):
        QWidget.__init__(self)

        self.setWindowTitle('Crews')

        crew_table = TableModel(self, crew_data, crew_headers)
        table_view = QTableView()
        table_view.setModel(crew_table)

        font = QtGui.QFont("Courier New", 14)
        table_view.setFont(font)

        table_view.resizeColumnsToContents()

        table_view.setSortingEnabled(True)
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)

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
        return len(self.crew_data[0])

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
        self.crew_main_window = crew_main_window(crew_data, crew_headers)

        layout = QHBoxLayout()


        main_site_button = QPushButton('Sites')
        main_site_button.clicked.connect(lambda checked: self.display_site_main_window(self.site_main_window))
        layout.addWidget(main_site_button)

        main_flight_button = QPushButton('Flights')
        main_flight_button.clicked.connect(lambda checked: self.display_flight_main_window(self.flight_main_window))
        layout.addWidget(main_flight_button)

        main_crew_button = QPushButton('Crews')
        main_crew_button.clicked.connect(lambda checked: self.display_crew_main_window(self.crew_main_window))
        layout.addWidget(main_crew_button)

        button4 = QPushButton('Quit')
        layout.addWidget(button4)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    # display_anything gets defined in the class that class it
    def display_site_main_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()

    def display_flight_main_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()

    def display_crew_main_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()


excluded_fields = '_id', 'suffix'
crew_headers = get_crew_column_query(excluded_fields)
crew_data = get_crew_query(excluded_fields)

metrics_tracker = QApplication([])
main = InitialWindow()
main.show()
metrics_tracker.exec_()
