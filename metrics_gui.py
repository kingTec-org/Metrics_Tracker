import PySimpleGUI as sg
from mongo_funcs import *
#from pymongo import MongoClient
import os

sg.theme('DefaultNoMoreNagging')
os.system('mongo_funcs.py')
label_size = (15, 1)
default_button_layout = []


# initial window on opening
def main_window():
    layout = [
        [sg.Button('View Crew', size=(10, 1), key='-VIEW CREW WINDOW-'),
         sg.Button('View Site', size=(10, 1), key='-VIEW SITE WINDOW-')],
        [sg.Button('Exit', size=(22, 1))]]

    return sg.Window('Metrics', layout, finalize=True)


# main crew window, leading to edit crew window
def view_crew_window():
    crew_info_values = get_crew_query()
    headings = get_crew_column_query()
    layout = [[sg.Button('Edit Crew', size=(10, 1), key='-EDIT CREW WINDOW-'),
               sg.Button('Delete Crew', size=(10, 1), key='-DROP CREW-')],
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
              [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('View Crewmembers', layout, finalize=True)


# main site windows leads to edit site window
def view_site_window():
    layout = [[sg.Button('Edit Site', size=(10, 1), key='-EDIT SITE WINDOW-')],
              [sg.Text('View Site Here')],
              [sg.Table(values=get_site_query(),
                        headings=get_site_column_query(),
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification="left",
                        alternating_row_color='LightGray',
                        enable_events=True,
                        bind_return_key=False,
                        key=None
                        )],
              [sg.Button('Back', size=(10, 1), key='-BACK-')]]
    return sg.Window('View Site', layout, finalize=True)


# main crew edit window, leads to add/deletion/alter options
def edit_crew_window():
    layout = [
        [sg.Text('Select crew member to edit')],
        [sg.Button('Add Crew', key='-ADD CREW WINDOW-', size=(10, 1))],
        [sg.Button('Close', size=(10, 1))]]
    return sg.Window('Crew Profiles', layout, finalize=True)


# main add crew window
def add_crew_window():
    layout = [
        [sg.Text('First Name', size=(15, 1)), sg.InputText('FN')],
        [sg.Text('Middle Name', size=(15, 1)), sg.InputText('MN')],
        [sg.Text('Last Name', size=(15, 1)), sg.InputText('LN')],
        [sg.Text('Suffix', size=(15, 1)), sg.InputText('III')],
        [sg.Text('Employee Number', size=(15, 1)), sg.InputText('88888888')],
        [sg.Text('Crew Position', size=(15, 1)), sg.InputText('SO')],
        [sg.Submit(size=(7, 1), key='-SUBMIT-')], [sg.Button('Close', size=(7, 1))]]
    return sg.Window('Add New Crew Member', layout, finalize=True)


# main site edit window, leads to add/deletion/alter options
def edit_site_window():
    layout = [
        [sg.Text('Select site to edit')],
        [sg.Button('Add Site', key='-ADD SITE WINDOW-', size=(10, 1)),
         sg.Button('Close', size=(10, 1))]]
    return sg.Window('Site Profiles', layout, finalize=True)


# main add site window
def add_site_window():
    layout = [
        [sg.Text('Site Name', size=label_size), sg.InputText('')],
        [sg.Text('Country', size=label_size), sg.InputText('')],
        [sg.Text('A/C', size=label_size), sg.InputText('')],
        [sg.Text('Present Staff', size=label_size), sg.InputText('')],
        [sg.Text('Required Staff', size=label_size), sg.InputText('')],
        [sg.Button('Add Site', size=(10, 1), key='--submit--')],
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

    # main_window
    if window == window1:
        if event == '-VIEW CREW WINDOW-':
            window1.hide()
            window2 = view_crew_window()
        elif event == '-VIEW SITE WINDOW-':
            window1.hide()
            window3 = view_site_window()

    # view_crew_window
    if window == window2:
        if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, '-BACK-'):
            window2.close()
            window1.un_hide()
        elif event in ('-DROP CREW-'):
            crew_info = get_crew_query()
            start = values['-READ TABLE-'][0]
            end = start+1
            employee_id = crew_info[start:end][0][0]
            drop_crew_member(employee_id)
            window2.close()
            print('Deleted. Refreshing')
            window1.show()
        elif event in ('-EDIT CREW WINDOW-'):
            window2.hide()
            window4 = edit_crew_window()

    # view_site_window
    if window == window3:
        if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, '-BACK-'):
            window3.close()
            window1.un_hide()
        elif event in ('-EDIT SITE WINDOW-'):
            window3.close()
            window5 = edit_site_window()

    # edit_crew_window
    if window == window4:
        if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, '-BACK-'):
            window4.close()
            window2.un_hide()
        elif event in ('-ADD CREW WINDOW-'):
            window4.hide()
            window6 = add_crew_window()

    # edit_site_window
    if window == window5:
        if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, '-BACK-'):
            window5.close()
            window3 = view_site_window()
        if event in ('-ADD SITE WINDOW-'):
            window5.hide()
            window7 = add_site_window()

    # add_crew_window
    if window == window6:
        if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, '-BACK'):
            window6.close()
            window4.un_hide()
        elif event in ('-SUBMIT-'):
            add_crew_members(values)
            window2 = view_crew_window()
        elif event in ('-*-'):
            pass

    # add_site_window
    if window == window7:
        if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, sg.WIN_CLOSED, '-BACK-'):
            window7.close()
            window5.un_hide()
        elif event in ('-SUBMIT-'):
            add_sites(values)
            window
            pass

# end of program
window.close()

# TODO: feed the Mongo tabular data to a real time DL model
# TODO: web framework
