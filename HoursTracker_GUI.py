import sys
import DB_connection
from PyQt5.QtWidgets import QApplication, QComboBox, QGridLayout, QMainWindow, QPushButton, QAction, QLineEdit, \
													 QWidget, QMessageBox, QLabel
from PyQt5 import QtCore, QtGui, QtSql


class CrewEditWindow(QWidget):
	"""
	This Widget(QWidget) creates a new window. Since it has no parent, it
	appears as a free-floating window.
	"""

	def __init__(self):
		super().__init__()
		grid = QGridLayout()

		self.title = "Add/Remove/Edit Crew-member"
		self.setWindowTitle(self.title)

		global enter_employee_id
		enter_employee_id = QLineEdit(self)
		enter_employee_id.setPlaceholderText("Enter Employee ID#")
		enter_employee_id.setMaxLength(8)

		global enter_first_name
		enter_first_name = QLineEdit(self)
		enter_first_name.setPlaceholderText("Enter First Name")
		enter_first_name.setMaxLength(32)

		global enter_middle_name
		enter_middle_name = QLineEdit(self)
		enter_middle_name.setPlaceholderText("Enter Middle Name")
		enter_middle_name.setMaxLength(32)

		global enter_last_name
		enter_last_name = QLineEdit(self)
		enter_last_name.setPlaceholderText("Enter Last Name")
		enter_last_name.setMaxLength(32)

		# TODO: Turn this into a drop-down box to select crew positions and ratings
		global enter_crew_position
		enter_crew_position = QLineEdit(self)
		enter_crew_position.setPlaceholderText("Select Crew Position")
		enter_crew_position.setMaxLength(16)

		crew_positions = ['P', 'SO', 'IP', 'ISO', 'EP', 'ESO']


		#TODO Replace enter_crew_position function
		global crew_position_selector
		crew_position_selector = QComboBox(self)
		crew_position_selector.addItems(crew_positions)

		add_crew_btn = QPushButton("Add New Crew-member", self)
		add_crew_btn.clicked.connect(self.add_crew_member)

		# TODO: Create function to edit crew-member table in MySQL DB
		edit_crew_btn = QPushButton("Edit Crew-member", self)
		edit_crew_btn.clicked.connect(self.edit_crew_member)

		# TODO: Create function to remove crew-member from MySQL DB
		remove_crew_btn = QPushButton("Remove Crew-member", self)
		remove_crew_btn.clicked.connect(self.remove_crew_member)

		grid.addWidget(enter_employee_id, 1, 0, 1, 3)
		grid.addWidget(enter_first_name, 2, 0, 1, 3)
		grid.addWidget(enter_middle_name, 3, 0, 1, 3)
		grid.addWidget(enter_last_name, 4, 0, 1, 3)
		grid.addWidget(enter_crew_position, 5, 0, 1, 3)
		grid.addWidget(crew_position_selector, 0, 0, 1, 3)
		grid.addWidget(add_crew_btn, 6, 0)
		grid.addWidget(edit_crew_btn, 6, 1)
		grid.addWidget(remove_crew_btn, 6, 2)



		self.setLayout(grid)

	def add_crew_member():
		try:
			emp = enter_employee_id.text()
			eln = enter_last_name.text()
			efn = enter_first_name.text()
			emn = enter_middle_name.text()
			ecp = enter_crew_position.text()
			add_new_crew = f"INSERT INTO crew_members VALUES ({emp}, '{eln}', '{efn}', '{emn}', '{ecp}');"
			DB_connection.my_cursor.execute(add_new_crew)
			DB_connection.db_connection.commit()
			print(add_new_crew)
		except:
			print("Something is missing")

	# TODO change or get rid of this function after proof of concept
	def view_employee_details():
		# The view_deets variable send the correct instruction
		view_details = "SELECT * FROM crew_members;"
		DB_connection.my_cursor.execute(view_details)
		what_to_return = DB_connection.my_cursor.fetchall()
		columns = DB_connection.my_cursor.column_names
		print(columns)
		column_count = len(DB_connection.my_cursor.column_names)
		print(column_count)
		row_count = DB_connection.my_cursor.rowcount
		print(row_count)

	def change_employee_details(self):
		#TODO create new popup window for edit and removal of crewmembers
		set_first_name = alter_first_name.text()
		set_middle_name = alter_middle_name.text()
		set_last_name = alter_last_name.text()

		# for reference
		f"INSERT INTO crew_members VALUES ({emp}, '{eln}', '{efn}', '{emn}', '{ecp}');"

		#TODO create a table selector
		#TODO create databases for sights, aircraft, dynamic table for state/end dates for administrative usage


		alter_employee_entry = f"UPDATE `flight_hours_db`.`crew_members` SET `last_name` = '{set_last_name}' WHERE(" \
							   f"`employee_number` = '{emp}');"

		#UPDATE `flight_hours_db`.`crew_members` SET `first_name` = 'Keisha'
		#WHERE(`employee_number` = '12345678');

		#UPDATE `flight_hours_db`.`crew_members` SET
		#`last_name` = 'Player', `first_name` = 'The', `middle_name` = 'Best'
		#WHERE(`employee_number` = '22222222');

		#UPDATE `flight_hours_db`.`crew_members` SET `crew_position` = 'IP'
		#WHERE(`employee_number` = '33333333');



	def edit_crew_member():
		pass

	def remove_crew_member():
		pass


class Window(QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Aircraft Hours Tracker")

		extract_action = QAction("Exit", self)
		extract_action.setShortcut("Ctrl+Q")
		extract_action.triggered.connect(self.close_application)

		self.statusBar()

		main_menu = self.menuBar()
		file_menu = main_menu.addMenu('&File')
		file_menu.addAction(extract_action)

		self.grid = QGridLayout()
		widget = QWidget()
		widget.setLayout(self.grid)
		self.setCentralWidget(widget)

		self.home()

	def home(self):
		crew_functions = QPushButton("Crew-member Functions", self)
		self.grid.addWidget(crew_functions, 6, 0)
		crew_functions.clicked.connect(self.show_crew_edit_window)

		quit_btn = QPushButton("Quit", self)
		self.grid.addWidget(quit_btn, 7, 0)
		quit_btn.clicked.connect(self.close_application)

		self.show()

	def show_crew_edit_window(self):
		self.w = CrewEditWindow()
		self.w.show()

	# noinspection PyMethodMayBeStatic
	def close_application(self):
		sys.exit()


CrewEditWindow.view_employee_details()


def run():
	app = QApplication(sys.argv)
	gui = Window()
	sys.exit(app.exec_())


run()
