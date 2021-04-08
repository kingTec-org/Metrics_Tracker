import PySimpleGUI as sg
from mysql_connector import *

sg.theme('DefaultNoMoreNagging')


# initial window on opening
def main_window():
	layout = [
		[sg.Button('View Crew', size=(10, 1), key='view_crew_window'),
		 sg.Button('View Site', size=(10, 1), key='view_site_window')],
		[sg.Button('Exit', size=(24, 1))]]

	return sg.Window('Metrics', layout, finalize=True)


# main crew window, leading to edit crew window
def view_crew_window():
	layout = [[sg.Button('Edit Crew', size=(7, 1), key='edit_crew_window')],
			  [sg.Text('View Crew Here')],
			  [sg.Table(values=get_crew_query(),
						headings=get_crew_column_query(),
						auto_size_columns=True,
						display_row_numbers=True,
						justification="left",
						alternating_row_color='LightGray',
						enable_events=False,
						bind_return_key=False,
						key=None
						)],
			  [sg.Button('Ok', size=(7, 1)), sg.Button('Close', size=(7, 1))]]
	return sg.Window('View Crewmembers', layout, finalize=True)


# main site windows leads to edit site window
def view_site_window():
	layout = [[sg.Button('Edit Site', size=(7, 1), key='edit_site_window')],
			  [sg.Text('View Site Here')],
			  [sg.Table(values=get_site_query(),
						headings=get_site_column_query(),
						auto_size_columns=True,
						display_row_numbers=True,
						justification="left",
						alternating_row_color='LightGray',
						enable_events=False,
						bind_return_key=False,
						key=None
						)],
			  [sg.Button('Ok', size=(7, 1)), sg.Button('Close', size=(7, 1))]]
	return sg.Window('View Site', layout, finalize=True)


# main crew edit window, leads to add/deletion/alter options
def edit_crew_window():
	layout = [
		[sg.Text('Select crew member to edit')],
		[sg.Button('Add Crew', key='add_crew_window', size=(10, 1))],
		[sg.Button('Close', size=(10, 1))]]
	return sg.Window('Crew Profiles', layout, finalize=True)


# main add crew window
def add_crew_window():
	layout = [
		[sg.Text('First Name', size=(15, 1)), sg.InputText('First')],
		[sg.Text('Middle Name', size=(15, 1)), sg.InputText('Middle')],
		[sg.Text('Last Name', size=(15, 1)), sg.InputText('Last')],
		[sg.Text('Suffix', size=(15, 1)), sg.InputText('Suffix')],
		[sg.Text('Employee Number', size=(15, 1)), sg.InputText('Employee Number')],
		[sg.Text('Crew Position', size=(15, 1)), sg.InputText('Crew Position')],
		[sg.Submit(size=(7, 1))], [sg.Button('Close', size=(7, 1))]]
	return sg.Window('Add New Crew Member', layout, finalize=True)


# main site edit window, leads to add/deletion/alter options
def edit_site_window():
	layout = [
		[sg.Text('Select site to edit')],
		[sg.Button('Add Site', key='add_site_main_btn', size=(10, 1)),
		 sg.Button('Close', size=(10, 1))]]
	return sg.Window('Site Profiles', layout, finalize=True)


# main add site window
def add_site_window():
	layout = [
		[sg.Text('Site Name')],
		[sg.Text('Country')],
		[sg.Text('State')],
		[sg.Button('Add Site', size=(10, 1))],
		[sg.Button('Exit', size=(10, 1)), sg.Button('Close', size=(10, 1))]]
	return sg.Window('Site Profiles', layout, finalize=True)


window1 = main_window()
window2 = None
window3 = None
window4 = None
window5 = None
window6 = None
window7 = None

# window loop
while True:
	window, event, values = sg.read_all_windows()

	if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
		break

	if window == window1:  # main_window
		if event == 'view_crew_window':
			window1.hide()
			window2 = view_crew_window()
		elif event == 'view_site_window':
			window1.hide()
			window3 = view_site_window()

	if window == window2:  # view_crew_window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close'):
			window2.close()
			window1.un_hide()
		elif event in ('edit_crew_window'):
			window2.hide()
			window4 = edit_crew_window()

	if window == window3:  # view_site_window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close'):
			window3.close()
			window1.un_hide()
		elif event in ('edit_site_window'):
			window3.hide()
			window5 = edit_site_window()

	if window == window4:  # edit_crew_window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close', 'Cancel'):
			window4.close()
			window2.un_hide()
		elif event in ('add_crew_window'):
			window4.hide()
			window6 = add_crew_window()

	if window == window5:  # edit_site_window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close'):
			window5.close()
			window3.un_hide()
		if event in ('add_site_window'):
			window5.hide()
			window7 = add_site_window()

	if window == window6:  # add_crew_window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close'):
			window6.close()
			window4.un_hide()
		elif event in (''):
			pass

	if window == window7:  # add_site_window
		if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, 'Close'):
			window7.close()
			window5.un_hide()
		elif event in '':
			pass

# end of program
window.close()

# TODO Site and Crew DB, connection and inputs

# TODO feed the MySQL tabular data to a real time DL model,
#  and learn a web framework to deploy the draft version for
#  feedback.
