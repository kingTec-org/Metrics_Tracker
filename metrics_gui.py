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
            display_main_view_crew_window.close()
            display_main_view_crew_window = main_view_crew_window()
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
            display_main_view_site_window.refresh()
            display_main_view_site_window.close()
            display_detail_site_window = site_details_window()
        elif event == '-ADD SITE-':
            display_main_view_site_window.refresh()
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
            display_main_view_site_window.refresh()
            display_main_view_site_window.close()
            display_edit_site_window = edit_site_window()

    ##----------DISPLAY DETAILS WINDOWS------------##

    # display_crew_details_window
    if window == display_detail_crew_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_detail_crew_window.close()
            display_main_view_crew_window = main_view_crew_window()

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
        elif event == '-RANDOMIZE-':
            display_add_crew_window.refresh()
            display_add_crew_window.close()
            display_add_crew_window = add_crew_window()

    # add_site_window
    if window == display_add_site_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_add_site_window.refresh()
            display_add_site_window.close()
            display_main_view_site_window = main_view_site_window()
        elif event == '-SUBMIT-':
            display_add_site_window.refresh()
            add_site(values)
        elif event == '-RANDOMIZE-':
            pass

    ##------------VIEW SPECIFICS WINDOWS--------------##

    #
    if window == display_view_specific_site_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_view_specific_site_window.refresh()
            display_view_specific_site_window.close()
            display_main_view_site_window = main_view_site_window()
        elif event == '-EDIT SITE-':
            display_view_specific_site_window.refresh()
            #display_view_specific_site_window.close()
            print('create individual edit site window')

    #
    if window == display_view_specific_crew_window:
        if event in (sg.WIN_CLOSED, '-BACK-'):
            display_main_view_crew_window = main_view_crew_window()
            display_view_specific_crew_window.close()
        elif event == '-EDIT CREW-':
            display_edit_crew_window = edit_crew_window()
            #display_view_specific_crew_window.close()
            print('create individual edit crew window')

# end of program
window.close()

# TODO dynamically building of site+crew db, based on specific site doc in site collection
# TODO feed the Mongo tabular data to a real time DL model
# TODO web framework
