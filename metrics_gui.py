import PySimpleGUI as sg
from site_funcs import *
from crew_funcs import *
from flight_funcs import *

sg.theme('DefaultNoMoreNagging')


##-----------INITIAL WINDOW------------##
def display_initial_window():
    layout = [
        [sg.Button('Sites', size=(10, 1), key='-VIEW SITE WINDOW-'),
         sg.Button('Flights', size=(10, 1), key='-VIEW FLIGHT WINDOW-'),
         sg.Button('Crews', size=(10, 1), key='-VIEW CREW WINDOW-')],
        [sg.Button('Exit', size=(22, 1), key='-EXIT-')]]

    return sg.Window('Metrics', layout, finalize=True)


##-----------MAIN VIEW WINDOWS---------##
def display_site_main_window():
    excluded_fields = ['_id']
    layout = [[sg.Button('View Site', size=(10, 1), key='-VIEW SITE-'),
               sg.Button('Add Site', size=(10, 1), key='-ADD SITE-')],
              [sg.Table(values=get_site_query(excluded_fields),
                        headings=get_site_column_query(excluded_fields),
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification="left",
                        alternating_row_color='LightGray',
                        enable_events=True,
                        bind_return_key=False,
                        key='-READ TABLE-'
                        )],
              [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Sites', layout, finalize=True)


def display_flight_main_window():
    excluded_fields = ['_id', 'crew_on_flight', 'pilot_in_command']
    layout = [[sg.Button('View Flight', size=(10, 1), key='-VIEW FLIGHT-'),
               sg.Button('Add Flight', size=(10, 1), key='-ADD FLIGHT-')],
              [sg.Table(values=get_flight_query(excluded_fields),
                        headings=get_flight_column_query(excluded_fields),
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification="left",
                        alternating_row_color='LightGray',
                        enable_events=True,
                        bind_return_key=False,
                        key='-READ TABLE-'
                        )],
              [sg.Button('Back', size=(10, 1), key='-BACK-')]
              ]
    return sg.Window('Flights', layout, finalize=True)


def display_crew_main_window():
    excluded_fields = ['_id', 'suffix']
    layout = [[sg.Button('View Crew', size=(10, 1), key='-VIEW CREW-'),
               sg.Button('Add Crew', size=(10, 1), key='-ADD CREW-')],
              [sg.Table(values=get_crew_query(excluded_fields),
                        headings=get_crew_column_query(excluded_fields),
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification="left",
                        alternating_row_color='LightGray',
                        enable_events=True,
                        bind_return_key=False,
                        key='-READ TABLE-'
                        )],
              [sg.Button('Back', size=(10, 1), key='-BACK-')]
              ]
    return sg.Window('Aircrew', layout, finalize=True)


##----------DETAIL WINDOWS------------##
def display_site_expand_window():
    site = get_site_query()[values['-READ TABLE-'][0]]
    global site_id
    site_id = get_site_query()[values['-READ TABLE-'][0]][0]
    column_list = get_site_column_query()
    layout = [[sg.Text(f'{column_list[i]}', size=(15, 1)),
               sg.Text(f'{site[i]}', justification='right')] for i in range(len(column_list))]
    layout += [[sg.Button('Back', size=(10, 1), key='-BACK-'),
                sg.Button('Add Flight to Site', size=(10, 1), key='-ADD FLIGHT-'),
                sg.Button('Edit Site', size=(10, 1), key='-EDIT SITE-'),
                sg.Button('Delete Site', size=(10, 1), key='-DELETE SITE-')]]

    return sg.Window(f'Site ID: {site[0]}', layout, finalize=True)


def display_flight_expand_window():
    global flight_number
    flight_number = (get_flight_query()[values['-READ TABLE-'][0]][0])

    # add database fields to exclude here #TODO convert to dropdown selector list
    excluded_fields = ['_id']
    flight_list = get_flight_query(excluded_fields)[values['-READ TABLE-'][0]]
    column_list = get_flight_column_query(excluded_fields)
    layout = [[sg.Text(f'{column_list[i]}', size=(15, 1)),
               sg.Text(f'{flight_list[i]}', justification='right')] for i in range(len(column_list))]
    layout += [[sg.Button('Back', size=(10, 1), key='-BACK-'),
                sg.Button('Add Crew To Flight', size=(10, 1), key='-ADD CREW-'),
                sg.Button('Edit Flight', size=(10, 1), key='-EDIT FLIGHT-'),
                sg.Button('Delete Flight', size=(10, 1), key='-DELETE FLIGHT-')
                ]]

    return sg.Window(f'Flight Number: {flight_list[1]} - {flight_list[0]}', layout, finalize=True)


def display_crew_expand_window():
    crew = get_crew_query()[values['-READ TABLE-'][0]]
    global employee_id
    employee_id = (get_crew_query()[values['-READ TABLE-'][0]][0])
    column_list = get_crew_column_query()

    layout = [[sg.Text(f'{column_list[i]}', size=(15, 1)),
               sg.Text(f'{crew[i]}', justification='right')] for i in range(len(column_list))]

    layout += [[sg.Button('Back', size=(10, 1), key='-BACK-'),
                sg.Button('Edit Crew', size=(10, 1), key='-EDIT CREW-'),
                sg.Button('Delete Crew', size=(10, 1), key='-DELETE CREW-'),
                sg.Button('Add To Flight', size=(10, 1), key='-ADD-')]]

    return sg.Window(f'{crew[0]}', layout, finalize=True)


##------------EDIT WINDOWS-------------##
def display_site_edit_window():
    layout = [
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Edit Site', layout, finalize=True)


def display_flight_edit_window():
    layout = [
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Edit Flight', layout, finalize=True)


def display_crew_edit_window():
    layout = [
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Edit Crew', layout, finalize=True)


##------------ADD WINDOWS--------------##
def display_site_add_window():
    random_site = gen_random_site()
    layout = [
        [sg.Text('Site ID', size=(15, 1)), sg.InputText(f'{random_site[0]}')],
        [sg.Text('Country', size=(15, 1)), sg.InputText(f'{random_site[1]}')],
        [sg.Text('A/C Type', size=(15, 1)), sg.InputText(f'{random_site[2]}')],
        [sg.Text('A/C #', size=(15, 1)), sg.InputText(f'{random_site[3]}')],
        [sg.Text('Present Staff', size=(15, 1)), sg.InputText(f'{random_site[4]}')],
        [sg.Text('Required Staff', size=(15, 1)), sg.InputText(f'{random_site[5]}')],
        [sg.Submit(size=(10, 1), key='-SUBMIT-'),
         sg.Button('Back', size=(10, 1), key='-BACK-'),
         sg.Button('Randomize', size=(7, 1), key='-RANDOMIZE-')]]
    return sg.Window('Add Site', layout, finalize=True)


def display_flight_add_window():
    random_flight = gen_random_flight()
    layout = [
        [sg.Text('Flight Number', size=(15, 1)), sg.InputText(f'{random_flight[0]}')],
        [sg.Text('Aircraft Type', size=(15, 1)), sg.InputText(f'{random_flight[1]}')],
        [sg.Text('Scheduled T/O', size=(15, 1)), sg.InputText(f'{random_flight[2]}')],
        [sg.Text('Scheduled L/T', size=(15, 1)), sg.InputText(f'{random_flight[3]}')],
        [sg.Submit(size=(7, 1), key='-SUBMIT-'),
         sg.Button('Back', size=(7, 1), key='-BACK-'),
         sg.Button('Randomize', size=(7, 1), key='-RANDOMIZE-')]]
    return sg.Window('Add Flight', layout, finalize=True)


def display_crew_add_window():
    random_crew = gen_random_crew()
    layout = [
        [sg.Text('First Name', size=(15, 1)), sg.InputText(f'{random_crew[0]}')],
        [sg.Text('Middle Name', size=(15, 1)), sg.InputText(f'{random_crew[1]}')],
        [sg.Text('Last Name', size=(15, 1)), sg.InputText(f'{random_crew[2]}')],
        [sg.Text('Suffix', size=(15, 1)), sg.InputText(f'{random_crew[3]}')],
        [sg.Text('Employee Number', size=(15, 1)), sg.InputText(f'{random_crew[4]}')],
        [sg.Text('Crew Position', size=(15, 1)), sg.InputText(f'{random_crew[5]}')],
        [sg.Submit(size=(7, 1), key='-SUBMIT-'),
         sg.Button('Back', size=(7, 1), key='-BACK-'),
         sg.Button('Randomize', size=(7, 1), key='-RANDOMIZE-')]]

    return sg.Window('Add Crew', layout, finalize=True)


##---------ADD CREW FLIGHTS TO FLIGHTS SITES-------##
def display_flight_crew_add_window(flight_number):


    excluded_fields = ['_id', 'suffix']
    layout = [[
        sg.Table(values=get_crew_query(excluded_fields),
                 headings=get_crew_column_query(excluded_fields),
                 auto_size_columns=True,
                 display_row_numbers=True,
                 justification="left",
                 alternating_row_color='LightGray',
                 enable_events=True,
                 bind_return_key=False,
                 key='-READ TABLE-'),
        sg.Table(values=get_crew_from_flight(excluded_fields),
                 headings=get_crew_column_query(excluded_fields),
                 auto_size_columns=True,
                 display_row_numbers=True,
                 justification="left",
                 alternating_row_color='LightGray',
                 enable_events=True,
                 bind_return_key=False,
                 key='-READ TABLE2-')],
        [sg.Submit(size=(7, 1), key='-SUBMIT-'),sg.Button('Remove', size=(7, 1), key='-REMOVE-'), sg.Button('Back', size=(7, 1), key='-BACK-')
         ]]

    return sg.Window('Populate Flight', layout, finalize=True)


def display_site_flight_add_window():
    layout = [
        [sg.Table(values=['Test3', 'Test4'], headings=['Test Column2']),
         sg.Submit(size=(7, 1), key='-SUBMIT-'), sg.Button('Back', size=(7, 1), key='-BACK-')]]

    return sg.Window('Populate Site', layout, finalize=True)


initial_window = display_initial_window()

site_main_window = None
site_expand_window = None
site_edit_window = None
site_add_window = None
site_flight_add_window = None

flight_main_window = None
flight_expand_window = None
flight_edit_window = None
flight_add_window = None
flight_crew_add_window = None

crew_main_window = None
crew_expand_window = None
crew_edit_window = None
crew_add_window = None

# window loop
while True:
    window, event, values = sg.read_all_windows()
    print(event, values)

    # initial_window
    if window == initial_window:
        if event in (sg.WIN_CLOSED, '-EXIT-'):
            break
        elif event == '-VIEW SITE WINDOW-':
            site_main_window = display_site_main_window()
            initial_window.hide()
        elif event == '-VIEW FLIGHT WINDOW-':
            flight_main_window = display_flight_main_window()
            initial_window.hide()
        elif event == '-VIEW CREW WINDOW-':
            crew_main_window = display_crew_main_window()
            initial_window.hide()

    # site_main
    if window == site_main_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            initial_window.un_hide()
            site_main_window.hide()
        elif event in ('-VIEW SITE-'):
            try:
                site_expand_window = display_site_expand_window()
                site_main_window.hide()
            except IndexError:
                # TODO make popup
                print('Select A Site')
        elif event in ('-ADD SITE-'):
            site_add_window = display_site_add_window()
            site_main_window.close()

    # flight_main
    if window == flight_main_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            initial_window.un_hide()
            flight_main_window.hide()
        elif event in ('-VIEW FLIGHT-'):
            try:
                flight_expand_window = display_flight_expand_window()
                flight_main_window.hide()
            except IndexError:
                # TODO make popup
                print('Select A Flight')
        elif event in ('-ADD FLIGHT-'):
            flight_add_window = display_flight_add_window()
            flight_main_window.close()

    # crew_main
    if window == crew_main_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            initial_window.un_hide()
            crew_main_window.hide()
        elif event in ('-VIEW CREW-'):
            try:
                crew_expand_window = display_crew_expand_window()
                crew_main_window.hide()
            except IndexError:
                # TODO make popup
                print('Select A Crewmember')
        elif event in ('-ADD CREW-'):
            crew_add_window = display_crew_add_window()
            crew_main_window.close()

    # site_expand
    if window == site_expand_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            site_main_window.un_hide()
            site_expand_window.hide()
        elif event in ('-DELETE SITE-'):
            answer = sg.PopupYesNo(f'Are you sure you want to delete {site_id}?')
            if answer == 'No':
                answer.close()
            if answer == 'Yes':
                delete_site(site_id=site_id)
                site_expand_window.close()
                site_main_window.close()
                site_main_window = display_site_main_window()
        elif event in ('-EDIT SITE-'):
            site_expand_window.hide()
            site_edit_window = display_site_edit_window()
        elif event in ('-ADD FLIGHT-'):
            site_expand_window.hide()
            site_flight_add_window = display_site_flight_add_window()

    # flight_expand
    if window == flight_expand_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            flight_main_window.un_hide()
            flight_expand_window.hide()
        elif event in ('-DELETE FLIGHT-'):
            answer = sg.PopupYesNo(f'Are you sure you want to delete {flight_number}?')
            if answer == 'No':
                answer.close()
            if answer == 'Yes':
                delete_flight(flight_number)
                flight_expand_window.close()
                flight_main_window.close()
                flight_main_window = display_flight_main_window()
        elif event in ('-EDIT FLIGHT-'):
            flight_expand_window.hide()
            flight_edit_window = display_flight_edit_window()
        elif event in ('-ADD CREW-'):
            flight_expand_window.hide()
            flight_crew_add_window = display_flight_crew_add_window(flight_number)

    # crew_expand
    if window == crew_expand_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            crew_main_window.un_hide()
            crew_expand_window.hide()
        elif event in ('-DELETE CREW-'):
            answer = sg.PopupYesNo(f'Are you sure you want to delete {employee_id}?')
            if answer == 'No':
                answer.close()
            if answer == 'Yes':
                delete_crew(employee_id=employee_id)
                crew_expand_window.close()
                crew_main_window.close()
                crew_main_window = display_crew_main_window()
        elif event in ('-EDIT CREW-'):
            crew_expand_window.hide()
            crew_edit_window = display_crew_edit_window()

    # site_edit
    if window == site_edit_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            site_expand_window.un_hide()
            site_edit_window.close()

    # flight_edit
    if window == flight_edit_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            flight_expand_window.un_hide()
            flight_edit_window.close()

    # crew_edit
    if window == crew_edit_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            crew_expand_window.un_hide()
            crew_edit_window.close()

    # site_add
    if window == site_add_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            site_add_window.refresh()
            site_add_window.close()
            site_main_window = display_site_main_window()
        elif event == '-SUBMIT-':
            add_site(values)
            site_add_window.close()
            site_add_window = display_site_add_window()
        elif event == '-RANDOMIZE-':
            site_add_window.close()
            site_add_window = display_site_add_window()

    # flight_add
    if window == flight_add_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            flight_add_window.close()
            flight_main_window = display_flight_main_window()
        elif event == '-SUBMIT-':
            add_flight(values)
            flight_add_window.close()
            flight_add_window = display_flight_add_window()
        elif event == '-RANDOMIZE-':
            flight_add_window.close()
            flight_add_window = display_flight_add_window()

    # crew_add
    if window == crew_add_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            crew_add_window.refresh()
            crew_add_window.close()
            crew_main_window = display_crew_main_window()
        elif event == '-SUBMIT-':
            add_crew_members(values)
            crew_add_window.close()
            crew_add_window = display_crew_add_window()
        elif event == '-RANDOMIZE-':
            crew_add_window.close()
            crew_add_window = display_crew_add_window()

    # site_flight_add
    if window == site_flight_add_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            site_expand_window.un_hide()
            site_flight_add_window.close()
        elif event in ('-SUBMIT-'):
            print('Pass')

    # flight_crew_add
    if window == flight_crew_add_window:
        if event == sg.WIN_CLOSED:
            break
        elif event in ('-BACK-'):
            flight_expand_window.un_hide()
            flight_crew_add_window.close()
        elif event in ('-REMOVE-'):
            employee_id2 = (get_crew_query()[values['-READ TABLE2-'][0]][0])
            flight_number = flight_number
            remove_crew_from_flight(flight_number, employee_id2)
            flight_crew_add_window.close()
            flight_crew_add_window = display_flight_crew_add_window(flight_number)
        elif event in ('-SUBMIT-'):
            employee_id = (get_crew_query()[values['-READ TABLE-'][0]][0])
            flight_number = flight_number
            add_crew_to_flight(flight_number, employee_id)
            flight_crew_add_window.close()
            flight_crew_add_window = display_flight_crew_add_window(flight_number)

# end of program
window.close()

# TODO add engineering photo view for mx uploads
# TODO Change close to unhides to keep window persistent but refresh when needed, change 'x window' to break the loop...back is back, not x
# TODO dynamically building of site+crew db, based on specific site doc in site collection
# TODO feed the Mongo tabular data to a real time DL model
# TODO web framework
