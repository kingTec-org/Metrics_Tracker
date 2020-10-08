import sys
import DB_connection
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QAction, QLineEdit, QWidget
from PyQt5 import QtCore, QtGui


class Window(QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Aircraft Hours Tracker")
		self.grid_layout = QGridLayout()

		extract_action = QAction("Get to the chopper!!!", self)
		extract_action.setShortcut("Ctrl+Q")
		extract_action.setStatusTip("Leave The App")
		extract_action.triggered.connect(self.close_application)

		self.statusBar()

		main_menu = self.menuBar()
		file_menu = main_menu.addMenu('&File')
		file_menu.addAction(extract_action)

		self.home()

	def home(self):
		quit_btn = QPushButton("Quit", self)
		quit_btn.clicked.connect(self.close_application)
		self.grid_layout.addWidget(quit_btn, 0, 0)

		crew_btn = QPushButton("Add New Crew-member", self)
		crew_btn.clicked.connect(self.add_crew_member)
		self.grid_layout.addWidget(crew_btn, 0, 1)

		global enter_employee_id
		enter_employee_id = QLineEdit(self)
		enter_employee_id.setPlaceholderText("Enter Employee ID#")
		enter_employee_id.setMaxLength(8)
		self.grid_layout.addWidget(enter_employee_id, 0, 2)

		global enter_first_name
		enter_first_name = QLineEdit(self)
		enter_first_name.setPlaceholderText("Enter First Name")
		enter_first_name.setMaxLength(32)
		efn = enter_first_name.text()
		self.grid_layout.addWidget(enter_first_name, 0, 3)

		global enter_middle_name
		enter_middle_name = QLineEdit(self)
		enter_middle_name.setPlaceholderText("Enter Middle Name")
		enter_middle_name.setMaxLength(32)
		emn = enter_middle_name.text()
		self.grid_layout.addWidget(enter_middle_name, 0, 4)

		global enter_last_name
		enter_last_name = QLineEdit(self)
		enter_last_name.setPlaceholderText("Enter Last Name")
		enter_last_name.setMaxLength(32)
		eln = enter_last_name.text()
		self.grid_layout.addWidget(enter_last_name, 0, 5)

		# TODO: Turn this into a drop-down box to select crew positions and ratings
		global enter_crew_position
		enter_crew_position = QLineEdit(self)
		enter_crew_position.setPlaceholderText("Select Crew Position")
		enter_crew_position.setMaxLength(16)
		ecp = enter_crew_position.text()
		self.grid_layout.addWidget(enter_crew_position, 0, 6)

		self.show()

	def add_crew_member(self):
		emp = enter_employee_id.text()
		eln = enter_last_name.text()
		efn = enter_first_name.text()
		emn = enter_middle_name.text()
		ecp = enter_crew_position.text()
		add_new_crew = f"INSERT INTO crew_members VALUES ({emp}, '{eln}', '{efn}', '{emn}', '{ecp}');"
		DB_connection.my_cursor.execute(add_new_crew)
		DB_connection.db_connection.commit()
		print(add_new_crew)

	def close_application(self):
		sys.exit()


def run():
	app = QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())


run()

# TODO: Attach add new crew-member to the button
