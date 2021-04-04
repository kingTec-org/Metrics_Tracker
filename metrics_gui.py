import PySimpleGUI as sg
import site_profiles
import crew_profiles
sg.theme('DefaultNoMoreNagging')
site_list = site_profiles.site_profile
add_site_layout = site_profiles.add_site_layout

crew_list = crew_profiles.crew_profile
add_crew_member_layout = crew_profiles.add_crew_member_layout

main_layout = [[sg.Text('Select Current Site.')],
			   [sg.Text('In "settings", you can add or edit additional sites.')],
			   [sg.Button('Add New Site')],
			   [sg.Button('Add New Crew')],
			   [sg.Button('Quit')],
			   [sg.Listbox(values=site_list,
					  enable_events=True,
					  size=(40, 20),
					  key='-FILE LIST-')]]


#Windows
main_window = sg.Window('Proprietary Metrics Tracker', main_layout)
add_site_window = sg.Window('Add A New Training Site', add_site_layout)
add_crew_member_window = sg.Window('Add A New Training Site', add_crew_member_layout)
crew_details_window = ''
site_details_window = ''


#create event loop
while True:
	main_window_event, main_window_values = main_window.read()

	if main_window_event == 'Add New Site':
		add_site_event, add_site_values = add_site_window.read()

		if add_site_event == sg.WIN_CLOSED or add_site_event == 'Close':
			break

		break

	if main_window_event == 'Add New Crew':
		add_crew_event, add_crew_values = add_crew_member_window.read()

		if add_crew_event == sg.WIN_CLOSED or add_crew_event == 'Close':
			break

		break

	if main_window_event == 'Quit' or main_window_event == sg.WIN_CLOSED:
		break

main_window.close()

#TODO feed the MySQL tabular data to a real time DL model,
# and learn a web framework to deploy the draft version for feedback.