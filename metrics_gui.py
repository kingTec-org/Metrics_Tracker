import PySimpleGUI as sg
import site_profiles

site_list = site_profiles.site_list

main_layout = [[sg.Text('Select Current Site.')],
			   [sg.Text('In "settings", you can add or edit additional sites.')],
			   [sg.Button('OK')],
			   [sg.Listbox(values=site_list,
					  enable_events=True,
					  size=(40, 20),
					  key='-FILE LIST-')]]

add_site_layout = [[sg.Text('Site?')],
				   [sg.Text('Site??')][][]]

add_site_window = sg.Window('Add A New Training Site', )

#creates the initial window
window = sg.Window('Proprietary Metrics Tracker', main_layout)

#create event loop
while True:
	event, values = window.read()
	# Quit program on OK click or exit
	if event == 'OK' or event == sg.WIN_CLOSED:
		break

window.close()

#TODO feed the MySQL tabular data to a real time DL model,
# and learn a web framework to deploy the draft version for feedback.
#Remove/Edit Crew-member"
#r Employee ID#"
#r First Name"
#r Middle Name"
#r Last Name"
#'SO', 'IP', 'ISO', 'EP', 'ESO'
#New Crew-member"
#	add_crew_btn.clicked.connect(self.add_crew_member)
#
#	# TODO: Create function to edit crew-member table in MySQL DB
#	edit_crew_btn = QPushButton("Edit Crew-member", self)
#	edit_crew_btn.clicked.connect(self.edit_crew_member)
#
#	# TODO: Create function to remove crew-member from MySQL DB
#	remove_crew_btn = QPushButton("Remove Crew-member", self)
#	remove_crew_btn.clicked.connect(self.remove_crew_member)
#
#	grid.addWidget(enter_employee_id, 1, 0, 1, 3)
#	grid.addWidget(enter_first_name, 2, 0, 1, 3)
#	grid.addWidget(enter_middle_name, 3, 0, 1, 3)
#	grid.addWidget(enter_last_name, 4, 0, 1, 3)
#	grid.addWidget(enter_crew_position, 5, 0, 1, 3)
#	grid.addWidget(add_crew_btn, 6, 0)
#	grid.addWidget(edit_crew_btn, 6, 1)
#	grid.addWidget(remove_crew_btn, 6, 2)
#
#	self.setLayout(grid)
#
#ef add_crew_member(self):
#	try:
#		emp = enter_employee_id.text()
#		eln = enter_last_name.text()
#		efn = enter_first_name.text()
#		emn = enter_middle_name.text()
#		ecp = enter_crew_position.currentText()
#		add_new_crew = f"INSERT INTO crew_members VALUES ({emp}, '{eln}', '{efn}', '{emn}', '{ecp}');"
#		mql_connector.my_cursor.execute(add_new_crew)
#		mql_connector.conn.commit()
#		print(add_new_crew)
#	except:
#		print("Something is missing")
#
#ef change_employee_details(self):
#	# TODO create new popup window for edit and removal of crew-members
#	set_first_name = alter_first_name.text()
#	set_middle_name = alter_middle_name.text()
#	set_last_name = alter_last_name.text()
#
#	# TODO create a table selector
#	# TODO create databases for sites, aircraft, dynamic table for state/end dates for administrative usage
#
#	alter_employee_entry = f"UPDATE `flight_hours_db`.`crew_members` SET `last_name` = '{set_last_name}' WHERE(" \
#						   f"`employee_number` = '{emp}');"
#
#ef edit_crew_member():
#	pass
#
#ef remove_crew_member():
#	pass
#
#
# Window(QMainWindow):
#
#ef __init__(self):
#	super(Window, self).__init__()
#	self.setGeometry(50, 50, 500, 500)
#	self.setWindowTitle("Aircraft Hours Tracker")
#
#	extract_action = QAction("Exit", self)
#	extract_action.setShortcut("Ctrl+Q")
#	extract_action.triggered.connect(self.close_application)
#
#	self.statusBar()
#
#	main_menu = self.menuBar()
#	file_menu = main_menu.addMenu('&File')
#	file_menu.addAction(extract_action)
#
#	self.grid = QGridLayout()
#	widget = QWidget()
#	widget.setLayout(self.grid)
#	self.setCentralWidget(widget)
#
#	self.home()
#
#ef home(self):
#	self.crew_functions = QPushButton("Crew Profiles", self)
#	self.grid.addWidget(self.crew_functions, 5, 0, 1, 2)
#	self.crew_functions.clicked.connect(self.show_crew_edit_window)
#
#	self.crew_tables = QTableWidget(self)
#	self.grid.addWidget(self.crew_tables, 7, 0, 1, 2)
#	self.crew_tables.setRowCount(7)
#	self.crew_tables.setColumnCount(5)
#
#	self.crew_member_selector = QComboBox(self)
#	self.crew_member_selector.addItems(list_of_names)
#
#	self.grid.addWidget(self.crew_member_selector, 6, 0, 1, 2)
#
#	self.load_btn = QPushButton("Load Data", self)
#	self.grid.addWidget(self.load_btn, 8, 0)
#	self.load_btn.clicked.connect(self.load_data)
#
#	self.quit_btn = QPushButton("Quit", self)
#	self.grid.addWidget(self.quit_btn, 8, 1)
#	self.quit_btn.clicked.connect(self.close_application)
#
#	self.new_site_btn = QPushButton("Add New Site", self)
#	self.grid.addWidget(self.new_site_btn, 9, 0, 1, 2)
#	self.new_site_btn.clicked.connect(self.create_new_site)
#
#	self.show()
#
# TODO change this function to fill table
#ef view_employee_details():
#
#	# MYSQL Commands
#	view_details = 'SELECT * FROM crew_members;'
#	get_names = "SELECT CONCAT(last_name, ' ', first_name) AS full_name FROM crew_members;"
#	query = mql_connector.my_cursor.execute
#	query(get_names)
#
#	names = mql_connector.my_cursor.fetchall()
#	global list_of_names
#	list_of_names = []
#	for name in names:
#		name = str(name)
#		name = name[2:-3]
#		name = name.replace(" ", ", ")
#		list_of_names.append(name)
#
#ef show_crew_edit_window(self):
#	self.w = CrewEditWindow()
#	self.w.show()
#
# noinspection PyMethodMayBeStatic
#ef close_application(self):
#	mql_connector.my_cursor.close()
#	sys.exit()
#
#ef create_new_site(self):
#	new_site_dialog = QMessageBox(self)
#	new_site_dialog.setText("Enter Site Name")
#	self.show()
#
#	#self.cursor.execute("Create")
#
#ef load_data(self):
#	self.cursor = mql_connector.my_cursor
#	self.cursor.execute("SELECT * FROM crew_members")
#	result = self.cursor.fetchall()
#	self.crew_tables.setRowCount(0)
#
#	for row_number, row_data in enumerate(result):
#		self.crew_tables.insertRow(row_number)
#		for column_number, data in enumerate(row_data):
#			self.crew_tables.setItem(row_number, column_number, QTableWidgetItem(str(data)))
#
#w.view_employee_details()
#
#
#un():
#pp = QApplication(sys.argv)
#ui = Window()
#ys.exit(app.exec_())
#
#
