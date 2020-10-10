import sys
import DB_connection
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QAction, QLineEdit, QWidget, \
	QMessageBox, QLabel
from PyQt5 import QtCore, QtGui, QtSql

sites = ["Arkansas", "New Jersey", "Washington", "Nevada"]

class Crew_Edit_Window(QWidget):
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

		#TODO: Turn this into a drop-down box to select crew positions and ratings
		global enter_crew_position
		enter_crew_position = QLineEdit(self)
		enter_crew_position.setPlaceholderText("Select Crew Position")
		enter_crew_position.setMaxLength(16)

		add_crew_btn = QPushButton("Add New Crew-member", self)
		add_crew_btn.clicked.connect(self.add_crew_member)

		#TODO: Create function to edit crew-member table in MySQL DB
		edit_crew_btn = QPushButton("Edit Crew-member", self)
		edit_crew_btn.clicked.connect(self.edit_crew_member)

		#TODO: Create function to remove crew-member from MySQL DB
		remove_crew_btn = QPushButton("Remove Crew-member", self)
		remove_crew_btn.clicked.connect(self.remove_crew_member)

		grid.addWidget(enter_employee_id, 1, 0, 1, 3)
		grid.addWidget(enter_first_name, 2, 0, 1, 3)
		grid.addWidget(enter_middle_name, 3, 0, 1, 3)
		grid.addWidget(enter_last_name, 4, 0, 1, 3)
		grid.addWidget(enter_crew_position, 5, 0, 1, 3)
		grid.addWidget(add_crew_btn, 6, 0)
		grid.addWidget(edit_crew_btn, 6, 1)
		grid.addWidget(remove_crew_btn, 6, 2)

		grid.addWidget(self.label)
		self.setLayout(grid)

	def add_crew_member(self):
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

	def edit_crew_member(self):
		pass

	def remove_crew_member(self):
		pass

class Window(QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		#self.setGeometry(50, 50, 500, 500)
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
		self.w = Crew_Edit_Window()
		self.w.show()

	def close_application(self):
		sys.exit()








def run():
	app = QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())


run()

# TODO: Attach add new crew-member to the button
