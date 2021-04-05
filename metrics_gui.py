import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')

site_list = ['Item 1 on Site List']


def main_window():
	layout = [[sg.Text('Select Current Site')],
			  [sg.Input(k='-IN-', enable_events=True)],
			  [sg.Listbox(values=site_list,
						  enable_events=True,
						  size=(40, 20),
						  key='-FILE LIST-')],
			  [sg.Text(size=(20, 1), k='-OUTPUT-')],
			  [sg.Button('Next >'), sg.Button('Exit')],
			  [sg.Button('Add New Site'), sg.Button('Add New Crew')]]

	return sg.Window('Proprietary Metrics Tracker', layout, finalize=True)


def member_window():
	layout = [[sg.Text('Crew')],
			  [sg.Button('< Prev'), sg.Button('Next >')],
			  [sg.Button('Add Member'), sg.Button('Close')]]

	return sg.Window('Crew Profiles', layout, finalize=True)


def site_window():
	layout = [[sg.Text('Sites')],
			  [sg.Text('State?')],
			  [sg.Text('Country?')],
			  [sg.Button('< Prev'), sg.Button('Exit')],
			  [sg.Button('Add Site'), sg.Button('Close')]]

	return sg.Window('Site Profiles', layout, finalize=True)


window1, window2, window3 = main_window(), None, None

while True:
	window, event, values = sg.read_all_windows()
	if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
		break

	if window == window1:
		if event == 'Next >':
			window1.hide()
			window2 = member_window()
		window1['-OUTPUT-'].update(values['-IN-'])

	if window == window2:
		if event == 'Next >':
			window2.hide()
			window3 = site_window()
		elif event in (sg.WIN_CLOSED, '< Prev'):
			window2.close()
			window1.un_hide()
		elif event in ('Close'):
			window2.close()
			window1.un_hide()

	if window == window3:
		if event == ('< Prev'):
			window3.close()
			window2.un_hide()
		elif event in ('Close'):
			window3.close()
			window1.un_hide()

window.close()

# TODO feed the MySQL tabular data to a real time DL model,
# and learn a web framework to deploy the draft version for feedback.
