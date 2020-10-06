import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction
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

		self.show()




	def close_application(self):
		sys.exit()

def run():
	app = QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()

# TODO: Attach add new crewmember to the button
