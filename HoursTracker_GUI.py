import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Aircraft Hours Tracker")
		new_crew_button = QPushButton("Create New Crew Member")
		self.setCentralWidget(new_crew_button)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

