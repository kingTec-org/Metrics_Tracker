import PySimpleGUI as sg
from site_funcs import *
from crew_funcs import *
import names
import random

sg.theme('DefaultNoMoreNagging')


def main_window():
    layout = [
        [sg.Button('View Crew', size=(10, 1), key='-VIEW CREW WINDOW-'),
         sg.Button('View Site', size=(10, 1), key='-VIEW SITE WINDOW-')],
        [sg.Button('Exit', size=(22, 1), key='-EXIT-')]]

    return sg.Window('Metrics', layout, finalize=True)


def main_view_crew_window():
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


def crew_details_window():
    layout = [
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Crew Details', layout, finalize=True)


def edit_crew_window():
    layout = [
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Edit Crew', layout, finalize=True)


def add_crew_window():
    gender = ['male', 'female']
    suffix = ['Jr.', 'Sr.', 'III', 'IV']
    crew_pos = ['SO', 'P', 'ESO', 'EP']
    gender = random.choice(gender)
    layout = [
        [sg.Text('First Name', size=(15, 1)), sg.InputText(f'{names.get_first_name(gender=gender)}')],
        [sg.Text('Middle Name', size=(15, 1)), sg.InputText(f'{names.get_first_name(gender=gender)}')],
        [sg.Text('Last Name', size=(15, 1)), sg.InputText(f'{names.get_last_name()}')],
        [sg.Text('Suffix', size=(15, 1)), sg.InputText(f'{random.choice(suffix)}')],
        [sg.Text('Employee Number', size=(15, 1)), sg.InputText(f'{random.randint(13370001, 13380000)}')],
        [sg.Text('Crew Position', size=(15, 1)), sg.InputText(f'{random.choice(crew_pos)}')],
        [sg.Submit(size=(7, 1), key='-SUBMIT-'), sg.Button('Back', size=(7, 1), key='-BACK-')]]
    return sg.Window('Add Crew', layout, finalize=True)


def main_view_site_window():
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


def site_details_window():
    layout = [
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Site Details', layout, finalize=True)


def edit_site_window():
    layout = [
        [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Edit Site', layout, finalize=True)


def add_site_window():
    layout = [
        [sg.Text('Site ID', size=(15, 1)), sg.InputText('')],
        [sg.Text('Country', size=(15, 1)), sg.InputText('')],
        [sg.Text('A/C', size=(15, 1)), sg.InputText('')],
        [sg.Text('Present Staff', size=(15, 1)), sg.InputText('')],
        [sg.Text('Required Staff', size=(15, 1)), sg.InputText('')],
        [sg.Submit(size=(10, 1), key='-SUBMIT-'), sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('Add Site', layout, finalize=True)


def view_specific_crew():
    # get site name from table
    window_heading = ''
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
    return sg.Window(f'{window_heading}', layout, finalize=True)


def view_specific_site():
    pass


display_main_window = main_window()

display_main_view_crew_window = None
display_detail_crew_window = None
display_edit_crew_window = None
display_add_crew_window = None
display_view_specific_crew_window = None

display_main_view_site_window = None
display_detail_site_window = None
display_edit_site_window = None
display_add_site_window = None
display_view_specific_site_window = None

# window loop
while True:
    window, event, values = sg.read_all_windows()
    print(event, values)

    ##-----------------MAIN WINDOW------------------##

    # main_window
    if window == display_main_window:

        if event in (sg.WIN_CLOSED, '-EXIT-'):
            break
        elif event == '-VIEW CREW WINDOW-':
            display_main_window.close()
            display_main_view_crew_window = main_view_crew_window()
        elif event == '-VIEW SITE WINDOW-':
            display_main_window.close()
            display_main_view_site_window = main_view_site_window()

    ##-----------MAIN VIEW WINDOWS---------------##

    # main_view_crew_window
    if window == display_main_view_crew_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_main_view_crew_window.refresh()
            display_main_view_crew_window.close()
            display_main_window = main_window()
        elif event == '-VIEW CREW-':
            display_main_view_crew_window.refresh()
            display_main_view_crew_window.close()
            display_detail_crew_window = crew_details_window()
        elif event == '-ADD CREW-':
            display_main_view_crew_window.refresh()
            display_main_view_crew_window.close()
            display_add_crew_window = add_crew_window()
        elif event == '-DELETE CREW-':
            for idx in values['-READ TABLE-']:
                crew_info = get_crew_query()

                # identifies which crew to delete
                start = values['-READ TABLE-'][0]
                end = start + 1
                employee_id = crew_info[start:end][0][0]

                # actual mongo delete command
                delete_crew_member(employee_id)
            display_main_view_crew_window.refresh()
            display_main_view_crew_window.close()
            display_view_crew_window = main_view_crew_window()
        elif event == '-EDIT CREW-':
            display_main_view_crew_window.refresh()
            display_main_view_crew_window.close()
            display_edit_crew_window = edit_crew_window()

    # main_view_site_window
    if window == display_main_view_site_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_main_view_site_window.close()
            display_main_window = main_window()
        elif event == '-VIEW SITE-':
            display_main_view_site_window.close()
            display_detail_site_window = site_details_window()
        elif event == '-ADD SITE-':
            display_main_view_site_window.close()
            display_add_site_window = add_site_window()
        elif event == '-DELETE SITE-':
            for idx in values['-READ TABLE-']:
                site_info = get_site_query()

                # identifies which crew to delete
                start = values['-READ TABLE-'][0]
                end = start + 1
                site_id = site_info[start:end][0][0]

                # actual mongo delete command
                delete_site(site_id)
            display_main_view_site_window.close()
            display_main_view_site_window = main_view_site_window()
        elif event == '-EDIT SITE-':
            display_main_view_site_window.close()
            display_edit_site_window = edit_site_window()

    ##----------DISPLAY DETAILS WINDOWS------------##

    # display_crew_details_window
    if window == display_detail_crew_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_detail_crew_window.close()
            display_view_crew_window = main_view_crew_window()

    # display_site_details_window
    if window == display_detail_site_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_detail_site_window.close()
            display_main_view_site_window = main_view_site_window()

    ##--------------EDIT WINDOWS---------------##

    # edit_crew_window
    if window == display_edit_crew_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_edit_crew_window.close()
            display_main_view_crew_window = main_view_crew_window()

    # edit_site_window
    if window == display_edit_site_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_edit_site_window.close()
            display_main_view_site_window = main_view_site_window()


    ##------------ADD WINDOWS---------------##

    # add_crew_window
    if window == display_add_crew_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_add_crew_window.refresh()
            display_add_crew_window.close()
            display_main_view_crew_window = main_view_crew_window()
        elif event == '-SUBMIT-':
            display_add_crew_window.refresh()
            add_crew_members(values)
            display_add_crew_window.close()
            display_main_view_crew_window = main_view_crew_window()

    # add_site_window
    if window == display_add_site_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_add_site_window.close()
            display_main_view_site_window = main_view_site_window()
        elif event == '-SUBMIT-':
            add_site(values)
            display_add_site_window.close()
            display_main_view_site_window = main_view_site_window()

    ##------------VIEW SPECIFICS WINDOWS--------------##

    #
    if window == display_view_specific_site_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_view_specific_site_window.close()
            display_main_view_site_window = main_view_site_window()
        elif event == '-EDIT SITE-':
            display_main_view_site_window.close()
            display_edit_site_window = edit_site_window()

    #
    if window == display_view_specific_crew_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_main_view_crew_window = main_view_crew_window()
            display_view_specific_crew_window.close()
        elif event == '-EDIT CREW-':
            display_edit_crew_window = edit_crew_window()
            display_main_view_crew_window.close()

# end of program
window.close()

# TODO dynamically building of site+crew db, based on specific site doc in site collection
# TODO feed the Mongo tabular data to a real time DL model
# TODO web framework
