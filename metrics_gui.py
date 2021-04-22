import PySimpleGUI as sg
from site_funcs import *
from crew_funcs import *
from flight_funcs import *
import names
import random

sg.theme('DefaultNoMoreNagging')


##-----------INITIAL WINDOW------------##


def display_initial_window():
    layout = [
        [sg.Button('View Sites', size=(10, 1), key='-VIEW SITE WINDOW-'),
         sg.Button('View Flights', size=(10, 1), key='-VIEW FLIGHT WINDOW-'),
         sg.Button('View Crews', size=(10, 1), key='-VIEW CREW WINDOW-')],
        [sg.Button('Exit', size=(22, 1), key='-EXIT-')]]

    return sg.Window('Metrics', layout, finalize=True)


##-----------MAIN VIEW WINDOWS---------##

def display_crew_main_window():
    crew_info_values = get_crew_query()
    headings = get_crew_column_query()
    layout = [[sg.Button('View Crew', size=(10, 1), key='-VIEW CREW-'),
               sg.Button('Edit Crew', size=(10, 1), key='-EDIT CREW-'),
               sg.Button('Add Crew', size=(10, 1), key='-ADD CREW-'),
               sg.Button('Delete Crew', size=(10, 1), key='-DELETE CREW-')],
              [sg.Table(values=crew_info_values,
                        headings=headings,
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

def display_flight_main_window():
    flight_info_values = get_flight_query()
    headings = get_flight_column_query()
    layout = [[sg.Button('View Flight', size=(10, 1), key='-VIEW FLIGHT-'),
               sg.Button('Edit Flight', size=(10, 1), key='-EDIT FLIGHT-'),
               sg.Button('Add Flight', size=(10, 1), key='-ADD FLIGHT-'),
               sg.Button('Delete Flight', size=(10, 1), key='-DELETE FLIGHT-')],
              [sg.Table(values=flight_info_values,
                        headings=headings,
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

def display_site_main_window():
    site_info_values = get_site_query()
    headings = get_site_column_query()
    layout = [[sg.Button('View Site', size=(10, 1), key='-VIEW SITE-'),
               sg.Button('Edit Site', size=(10, 1), key='-EDIT SITE-'),
               sg.Button('Add Site', size=(10, 1), key='-ADD SITE-'),
               sg.Button('Delete Site', size=(10, 1), key='-DELETE SITE-')],
              [sg.Table(values=site_info_values,
                        headings=headings,
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


##----------DETAIL WINDOWS------------##
display_layout = []


def display_crew_details_window(window_heading, info):
    win_head = window_heading
    first, middle, last, suf, emp, crew_pos = info

    layout = [
        [sg.Text(f'{last}, {first} {middle} {suf}'), sg.Text('')],

        [sg.Text('7 Day Time', size=(15, 1), justification='left')],

        [sg.Text('30 Day Time', size=(15, 1), justification='left')],

        [sg.Text('90 Day Time', size=(15, 1), justification='left')],

        [sg.Text('Currencies Due', size=(15, 1), justification='left')],

        [sg.Text('Currencies Approaching', size=(15, 1), justification='left')],

        [sg.Button('Back', size=(10, 1), key='-BACK-')]]

    return sg.Window(f'{str(win_head)}', layout, finalize=True)


def display_site_details_window(window_heading, info):
    win_head = window_heading
    site, country, num_ac, staff_present, staff_required = info

    layout = [
        [sg.Text('Site ID', size=(15, 1)), sg.Text(f'{site}')],
        [sg.Text('Country', size=(15, 1)), sg.Text(f'{country}')],
        [sg.Text('A/C', size=(15, 1)), sg.Text(f'{num_ac}')],
        [sg.Text('Present Staff', size=(15, 1)), sg.Text(f'{staff_present}')],
        [sg.Text('Required Staff', size=(15, 1)), sg.Text(f'{staff_required}')],
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]

    return sg.Window(f'{win_head}', layout, finalize=True)


##------------EDIT WINDOWS-------------##

def display_crew_edit_window():
    layout = [
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Edit Crew', layout, finalize=True)


def display_edit_site_window():
    layout = [
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Edit Site', layout, finalize=True)


##------------ADD WINDOWS--------------##

def display_site_add_window():
    layout = [
        [sg.Text('Site ID', size=(15, 1)), sg.InputText('')],
        [sg.Text('Country', size=(15, 1)), sg.InputText('')],
        [sg.Text('A/C', size=(15, 1)), sg.InputText('')],
        [sg.Text('Present Staff', size=(15, 1)), sg.InputText('')],
        [sg.Text('Required Staff', size=(15, 1)), sg.InputText('')],
        [sg.Submit(size=(10, 1), key='-SUBMIT-'), sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Add Site', layout, finalize=True)


def display_flight_add_window():
    def gen_flight():
        flight_number = 'IBICF010112020000**Z'
        aircraft_type = 'KCQ-9'
        pilot_in_command = 'Larry D. Cawley Jr.'
        sched_to = '0000'
        act_to = '0000'
        sched_lt = '0000'
        act_lt = '0000'

        return flight_number, aircraft_type, pilot_in_command, sched_to, act_to, sched_lt, act_lt

    flight_number, aircraft_type, pilot_in_command, sched_to, act_to, sched_lt, act_lt = gen_flight()

    layout = [
        [sg.Text('Flight Number', size=(15, 1)), sg.InputText(f'{flight_number}')],
        [sg.Text('Aircraft Type', size=(15, 1)), sg.InputText(f'{aircraft_type}')],
        [sg.Text('Pilot in Command', size=(15, 1)), sg.InputText(f'{pilot_in_command}')],
        [sg.Text('Scheduled T/O', size=(15, 1)), sg.InputText(f'{sched_to}')],
        [sg.Text('Actual T/O', size=(15, 1)), sg.InputText(f'{act_to}')],
        [sg.Text('Scheduled L/T', size=(15, 1)), sg.InputText(f'{sched_lt}')],
        [sg.Text('Actual L/T', size=(15, 1)), sg.InputText(f'{act_lt}')],
        [sg.Submit(size=(7, 1), key='-SUBMIT-'),
        sg.Button('Back', size=(7, 1), key='-BACK-'),
        sg.Button('Randomize', size=(7, 1), key='-RANDOMIZE-')]]
    return sg.Window('Add Flight', layout, finalize=True)


def display_add_crew_window():
    def gen_crew():
        gender = random.choice(['male', 'female'])
        first = names.get_first_name(gender=gender)
        middle = names.get_first_name(gender=gender)
        last = names.get_last_name()

        emp = random.randint(13370001, 13380000)
        crew_pos = random.choice(['SO', 'P', 'ESO', 'EP'])

        if gender == 'male':
            suf = random.choice(['Jr.', 'Sr.', 'III', 'IV', '', '', '', '', '', '', '', '', '', ''])
        else:
            suf = ''

        return first, middle, last, suf, emp, crew_pos

    first, middle, last, suf, emp, crew_pos = gen_crew()

    layout = [
        [sg.Text('First Name', size=(15, 1)), sg.InputText(f'{first}')],
        [sg.Text('Middle Name', size=(15, 1)), sg.InputText(f'{middle}')],
        [sg.Text('Last Name', size=(15, 1)), sg.InputText(f'{last}')],
        [sg.Text('Suffix', size=(15, 1)), sg.InputText(f'{suf}')],
        [sg.Text('Employee Number', size=(15, 1)), sg.InputText(f'{emp}')],
        [sg.Text('Crew Position', size=(15, 1)), sg.InputText(f'{crew_pos}')],
        [sg.Submit(size=(7, 1), key='-SUBMIT-'),
         sg.Button('Back', size=(7, 1), key='-BACK-'),
         sg.Button('Randomize', size=(7, 1), key='-RANDOMIZE-')]]

    return sg.Window('Add Crew', layout, finalize=True)


initial_window = display_initial_window()

site_main_window = None
site_detail_window = None
site_edit_window = None
site_add_window = None

flight_main_window = None
flight_detail_window = None
flight_edit_window = None
flight_add_window = None

crew_main_window = None
crew_detail_window = None
crew_edit_window = None
crew_add_window = None

# window loop
while True:
    window, event, values = sg.read_all_windows()

    ##-----------------INITIAL WINDOW------------------##

    # initial_window
    if window == initial_window:
        if event in (sg.WIN_CLOSED, '-EXIT-'):
            break
        elif event == '-VIEW SITE WINDOW-':
            initial_window.close()
            site_main_window = display_site_main_window()
        elif event == '-VIEW FLIGHT WINDOW-':
            initial_window.close()
            flight_main_window = display_flight_main_window()
        elif event == '-VIEW CREW WINDOW-':
            initial_window.close()
            crew_main_window = display_crew_main_window()

    ##-----------MAIN VIEW WINDOWS---------------##

    # main_view_site_window
    if window == site_main_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            site_main_window.close()
            initial_window = display_initial_window()
        elif event == '-VIEW SITE-':
            try:
                row = values['-READ TABLE-']
                site_list = get_site_query()
                site = site_list[row[0]]
                print(site)
                window_heading = str(f'{site[1]} - {site[0]}')
                info = f'{site[0]}', f'{site[1]}', f'{site[2]}', f'{site[3]}', f'{site[4]}'
                site_detail_window = display_site_details_window(window_heading, info)
                site_main_window.refresh()
                site_main_window.close()
            except IndexError:
                print('Select A Site')
        elif event == '-ADD SITE-':
            site_main_window.refresh()
            site_main_window.close()
            site_add_window = display_site_add_window()
        elif event == '-DELETE SITE-':
            for idx in values['-READ TABLE-']:
                site_info = get_site_query()

                # identifies which crew to delete
                start = values['-READ TABLE-'][0]
                end = start + 1
                site_id = site_info[start:end][0][0]

                # actual mongo delete command
                delete_site(site_id)
            site_main_window.close()
            site_main_window = display_site_main_window()
        elif event == '-EDIT SITE-':
            site_main_window.refresh()
            site_main_window.close()
            site_edit_window = display_edit_site_window()

    # main_view_flight_window
    if window == flight_main_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            flight_main_window.close()
            initial_window = display_initial_window()
        elif event == '-VIEW FLIGHT-':
            try:
                row = values['-READ TABLE-']
                flight_list = get_flight_query()
                flight = flight_list[row[0]]
                print(flight)
                window_heading = str(f'{flight[1]} - {flight[0]}')
                info = f'{flight[0]}', f'{flight[1]}', f'{flight[2]}', f'{flight[3]}', f'{flight[4]}'
                flight_detail_window = display_flight_details_window(window_heading, info)
                flight_main_window.refresh()
                flight_main_window.close()
            except IndexError:
                print('Select A Flight')
        elif event == '-ADD FLIGHT-':
            flight_main_window.refresh()
            flight_main_window.close()
            flight_add_window = display_flight_add_window()
        elif event == '-DELETE FLIGHT-':
            for idx in values['-READ TABLE-']:
                flight_info = get_flight_query()

                # identifies which crew to delete
                start = values['-READ TABLE-'][0]
                end = start + 1
                flight_id = flight_info[start:end][0][0]

                # actual mongo delete command
                delete_flight(flight_id)
            flight_main_window.close()
            flight_main_window = display_flight_main_window()
        elif event == '-EDIT FLIGHT-':
            flight_main_window.refresh()
            flight_main_window.close()
            flight_edit_window = display_flight_edit_window()

    # main_view_crew_window
    if window == crew_main_window:
        print(crew_main_window.Title)
        if event in (sg.WIN_CLOSED, '-BACK-'):
            crew_main_window.close()
            initial_window = display_initial_window()
        elif event == '-VIEW CREW-':
            try:
                row = values['-READ TABLE-']
                crew_list = get_crew_query()
                crew = crew_list[row[0]]
                print(crew)
                window_heading = str(f'{crew[1]}, {crew[3]} - {crew[5]}')
                info = f'{crew[4]}', f'{crew[3]}', f'{crew[1]}', f'{crew[2]}', f'{crew[0]}', f'{crew[5]}'
                crew_detail_window = display_crew_details_window(window_heading, info)
                crew_main_window.refresh()
                crew_main_window.close()
            except IndexError:
                print('Select A Crewmember')
        elif event == '-ADD CREW-':
            crew_main_window.refresh()
            crew_main_window.close()
            crew_add_window = display_add_crew_window()
        elif event == '-DELETE CREW-':
            for idx in values['-READ TABLE-']:
                crew_info = get_crew_query()

                # identifies which crew to delete
                start = values['-READ TABLE-'][0]
                end = start + 1
                employee_id = crew_info[start:end][0][0]

                # actual mongo delete command
                delete_crew_member(employee_id)
            crew_main_window.close()
            crew_main_window = display_crew_main_window()
        elif event == '-EDIT CREW-':
            crew_main_window.refresh()
            crew_main_window.close()
            crew_edit_window = display_crew_edit_window()


    ##----------DETAIL WINDOWS------------##

    # display_crew_details_window
    if window == crew_detail_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            crew_detail_window.close()
            crew_main_window = display_crew_main_window()
        elif event == '-SEE-':
            print(window_heading)

    # display_site_details_window
    if window == site_detail_window:

        if event in (sg.WIN_CLOSED, '-BACK-'):
            site_detail_window.close()
            site_main_window = display_site_main_window()

        elif event == '-SEE-':
            print(window_heading)

    ##--------------EDIT WINDOWS---------------##

    # edit_crew_window
    if window == crew_edit_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            crew_edit_window.close()
            crew_main_window = display_crew_main_window()

    # edit_site_window
    if window == site_edit_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            site_edit_window.close()
            site_main_window = display_site_main_window()

    ##------------ADD WINDOWS---------------##

    # add_site_window
    if window == site_add_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            site_add_window.refresh()
            site_add_window.close()
            site_main_window = display_site_main_window()
        elif event == '-SUBMIT-':
            site_add_window.refresh()
            add_site(values)
        elif event == '-RANDOMIZE-':
            pass

    if window == flight_add_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            flight_add_window.refresh()
            flight_add_window.close()
            site_main_window = display_site_main_window()
        elif event == '-SUBMIT-':
            flight_add_window.refresh()
            add_flight(values)
        elif event == '-RANDOMIZE-':
            pass

    # add_crew_window
    if window == crew_add_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            crew_add_window.refresh()
            crew_add_window.close()
            crew_main_window = display_crew_main_window()
        elif event == '-SUBMIT-':
            crew_add_window.refresh()
            add_crew_members(values)
            crew_add_window.close()
            crew_add_window = display_add_crew_window()
        elif event == '-RANDOMIZE-':
            crew_add_window.refresh()
            crew_add_window.close()
            crew_add_window = display_add_crew_window()


# end of program
window.close()

# TODO dynamically building of site+crew db, based on specific site doc in site collection
# TODO feed the Mongo tabular data to a real time DL model
# TODO web framework
