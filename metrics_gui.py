import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')

site_list = ['Item 1 on Site List']
member_list = ['1st Crewmember']

layout = [[sg.Ok(), sg.Cancel()]]  # ok and cancel buttons


def main_window():
	layout = [[sg.Button('Edit Site', size=(7.5,1), key='edit_site_window'),
			   sg.Button('Edit Crew', size=(7.5,1), key='edit_crew_window')],
			  [sg.Button('Exit',size=(18,1))]]

	return sg.Window('Metrics', layout, finalize=True)


def edit_crew_window():
	layout = [[sg.Text('Edit Crew')],
			  [sg.Button('Add Crew', key='add_crew_main_btn', size=(10, 1)), sg.Button('Close', size=(10, 1))]]

	return sg.Window('Crew Profiles', layout, finalize=True)


def add_crew_window():
	layout = [[sg.Text('Please enter your First Name, Last Name, E-Mail')],
			  [sg.Text('First Name', size=(15, 1)), sg.InputText('First')],
			  [sg.Text('Middle Name', size=(15, 1)), sg.InputText('Middle')],
			  [sg.Text('Last Name', size=(15, 1)), sg.InputText('Last')],
			  [sg.Text('Suffix', size=(15, 1)), sg.InputText('Suffix')],
			  [sg.Text('Employee Number', size=(15, 1)), sg.InputText('Employee Number')],
			  [sg.Text('Crew Position', size=(15, 1)), sg.InputText('Crew Position')],
			  [sg.Submit(), sg.Cancel()]]

	return sg.Window('Add New Crew Member', layout, finalize=True)


def edit_site_window():
	layout = [[sg.Text('Edit Site')],
			  [sg.Button('Add New Site', key='add_site_main_btn', size=(10, 1)), sg.Button('Close', size=(10, 1))]]

	return sg.Window('Site Profiles', layout, finalize=True)


def add_site_window():
	layout = [[sg.Text('Sites')],
			  [sg.Text('State?')],
			  [sg.Text('Country?')],
			  [sg.Button('Add Site', size=(10,1))],
			  [sg.Button('Exit', size=(10,1)), sg.Button('Close', size=(10,1))]]

	return sg.Window('Site Profiles', layout, finalize=True)

window1, window2, window3, window4, window5 = main_window(), None, None, None, None

while True:
	window, event, values = sg.read_all_windows()
	if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
		break

	if window == window1: # Main Window
		if event == 'edit_crew_window':
			window1.hide()
			window2 = edit_crew_window()
		elif event == 'edit_site_window':
			window1.hide()
			window3 = edit_site_window()

	if window == window2: # Edit Crew Window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close'):
			window2.close()
			window1.un_hide()
		elif event in ('add_crew_main_btn'):
			window2.hide()
			window4 = add_crew_window()

	if window == window3: # Edit Site Window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close'):
			window3.close()
			window1.un_hide()
		elif event in ('add_site_main_btn'):
			window3.hide()
			window5 = add_site_window()

	if window == window4: # Add Crew Window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close','Cancel'):
			window4.close()
			window2.un_hide()

	if window == window5: # Add Site Window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close'):
			window5.close()
			window3.un_hide()

window.close()
# TODO Site and Crew DB, connection and inputs

# TODO feed the MySQL tabular data to a real time DL model,
#  and learn a web framework to deploy the draft version for
#  feedback.
