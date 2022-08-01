"""
An exercise to easily convert a length in feet, inches and 1/16ths to metres.
Built using PySimpleGUI with two frames (frame in frame), spinners and buttons.
"""

import PySimpleGUI as sg
import math

sg.theme('BluePurple')

f_dict = {"0": 0, "1/16": 1, "1/8": 2, "3/16": 3, "1/4": 4, "5/16": 5, "3/8": 6, "7/16": 7,
 "1/2": 8, "9/16": 9, "5/8": 10, "11/16": 11, "3/4": 12, "13/16": 13, "7/8": 14, "15/16": 15,}

f_key = ["0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16",
 "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16",]

layout_frame = [
    [sg.Frame("", [[sg.Text( '', text_color= 'white', background_color='#404040')],
    [sg.Spin([i for i in range(0,100)], s=3, initial_value=0, key='-F1-'), sg.Text('feet', text_color='white', background_color='#404040'),
    sg.Spin([i for i in range(0,12)], s=3, initial_value=0, key='-S1-'), sg.Text('and', text_color= 'white', background_color='#404040'),
    sg.Spin(f_key, s=5, initial_value=0, key='-E1-'), sg.Text('inches', text_color= 'white', background_color='#404040')],
    [sg.Text( 'is equivalent to', text_color= 'white', background_color='#404040')],
    [sg.Multiline('', key='-OUT-', size=(7,1), no_scrollbar=True)],
    [sg.Text( 'metres', text_color= 'white', background_color='#404040')],
    [sg.B('Enter', bind_return_key=True), sg.B('Done')]
], pad=(100, 50), expand_x=True, expand_y=True, element_justification='center', background_color='#404040', border_width=8, relief='raised')]]

layout = [[sg.Frame("Convert Feet to Metres", layout_frame, size=(660, 400), title_location=sg.TITLE_LOCATION_TOP),]]

window = sg.Window("My Layout", layout, margins=(20, 20), font = ('Arial', 16), finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Done'):
        break
    if event == 'Enter':
        f = float(values['-F1-'])
        s = float(values['-S1-']) /12
        e = f_dict[values['-E1-']] / 192
        value = f + s + e
        answer = round(((value * 0.3048 * 10000.0 + 0.005)/10000.0), 4)
    window['-OUT-'].update(answer)

window.close()
