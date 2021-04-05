#form = sg.FlexForm('PPP Simple data entry form')
# begin with a blank form
#layout = [[sg.Text('Please enter your First Name, Last Name, E-Mail')]
#		[sg.Text('First Name', size=(15, 1)), sg.InputText('X')],
#		[sg.Text('Last Name', size=(15, 1)), sg.InputText('Y')],
#		[sg.Text('E-mail Address', size=(15, 1)), sg.InputText('Z')],
#		[sg.Submit(), sg.Cancel()]

#window=sg.Window('Earth Residents Contact Data', layout)

#button, values = window.Read()

#window.Close() # added to fix downstream problem

#print(button, values[0], values[1], values[2])

#quit()

'''
    Example of wizard-like PySimpleGUI windows
'''
import PySimpleGUI as sg

def make_window1():
    layout = [[sg.Text('Window 1'), ],
              [sg.Input(k='-IN-', enable_events=True)],
              [sg.Text(size=(20,1),  k='-OUTPUT-')],
              [sg.Button('Next >'), sg.Button('Exit')]]

    return sg.Window('Window 1', layout, finalize=True)


def make_window2():
    layout = [[sg.Text('Window 2')],
               [sg.Button('< Prev'), sg.Button('Next >')]]

    return sg.Window('Window 2', layout, finalize=True)


def make_window3():
    layout = [[sg.Text('Window 3')],
               [sg.Button('< Prev'), sg.Button('Exit')]]
    return sg.Window('Window 3', layout, finalize=True)



window1, window2, window3 = make_window1(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
        break

    if window == window1:
        if event == 'Next >':
            window1.hide()
            window2 = make_window2()
        window1['-OUTPUT-'].update(values['-IN-'])

    if window == window2:
        if event == 'Next >':
            window2.hide()
            window3 = make_window3()
        elif event in (sg.WIN_CLOSED, '< Prev'):
            window2.close()
            window1.un_hide()

    if window == window3:
        window3.close()
        window2.un_hide()

window.close()
