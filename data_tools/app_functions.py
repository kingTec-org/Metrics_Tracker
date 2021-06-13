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

# MAIN FILE
# ///////////////////////////////////////////////////////////////
import operator

from PySide6 import QtCore, QtWidgets, QtGui

from main import *


# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, the_data, the_headers):
        QtCore.QAbstractTableModel.__init__(self)
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

class TableView(QtWidgets.QTableView):
    def __init__(self):
        QtWidgets.QTableView.__init__(self)
        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.setFont(font)
