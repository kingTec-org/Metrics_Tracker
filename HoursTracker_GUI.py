import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QLineEdit
from PyQt5 import QtCore, QtGui

import crewmember_functions


class Window(QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Aircraft Hours Tracker")

		extractAction = QAction("Get to the chopper!!!", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip("Leave The App")
		extractAction.triggered.connect(self.close_application)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)

		self.home()


	def home(self):
		btn = QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0, 0)

		crew_btn = QPushButton("Add New Crewmember", self)
		crew_btn.clicked.connect(crewmember_functions.add_crew_member)
		crew_btn.resize(crew_btn.minimumSizeHint())
		crew_btn.move(75, 0)

		enter_employee_id = QLineEdit(self)
		enter_employee_id.setPlaceholderText("Enter Employee ID#")
		enter_employee_id.setMaxLength(8)
		enter_employee_id.setGeometry(100,100,150,20)
		enter_employee_id.move(100,50)

		enter_first_name = QLineEdit(self)
		enter_first_name.setPlaceholderText("Enter First Name")
		enter_first_name.setMaxLength(255)
		enter_first_name.setGeometry(100,100,150,20)
		enter_first_name.move(100,75)

		enter_middle_name = QLineEdit(self)
		enter_middle_name.setPlaceholderText("Enter Middle Name")
		enter_middle_name.setMaxLength(255)
		enter_middle_name.setGeometry(100, 100, 150, 20)
		enter_middle_name.move(100, 100)

		enter_last_name = QLineEdit(self)
		enter_last_name.setPlaceholderText("Enter Last Name")
		enter_last_name.setMaxLength(255)
		enter_last_name.setGeometry(100,100,150,20)
		enter_last_name.move(100, 125)

		#TODO: Turn this into a dropdown box to select crew positions and ratings
		enter_crew_position = QLineEdit(self)
		enter_crew_position.setPlaceholderText("Select Crew Position")
		enter_crew_position.setMaxLength(5)
		enter_crew_position.setGeometry(100,100,150,20)
		enter_crew_position.move(100,150)


		self.show()




	def close_application(self):
		sys.exit()

def run():
	app = QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()

# TODO: Attach add new crewmember to the button
