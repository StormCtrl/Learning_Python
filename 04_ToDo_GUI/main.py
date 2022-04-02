#Importing Modules
import PySimpleGUI as sg
from ToDoCode import * #Code has layout information as well

#Setting the Theme
sg.theme('Dark Blue 3')

#layout that makes sure I get the correct input for a new ToDo Object
layout_input = [
    [sg.Input(default_text = "", key="-TASK-"), sg.Button("Add" ,tooltip="Add something here")],
    [sg.Text("", key="-TEST-")],
    ]

#layout for a single todo object, will have to create a class for this
layout_single_task = [
    [sg.Text("Here we will have one to do task"), sg.Button("Done")]
    ]

#I'll have to make a variable that can be called that will list all the tasks
layout_all_tasks = [
    [sg.Frame("Your ToDo",
    layout_single_task,
    element_justification = "center",
    vertical_alignment = "center")]
    ]

#Ofcourse, I have to put my name on it
layout_credits = [[sg.Text("Program made by Daniel van Veldhoven", justification = "center")]]

#Combining all the layouts togehter
layout = layout_input + layout_all_tasks + layout_credits

#How the window will look like
window = sg.Window('StormCtrl - ToDo',
    layout,
    grab_anywhere = True,
    no_titlebar = False,
    alpha_channel = 0.9,
    resizable = True,
    element_justification = "center")

#Execute the Program in while Event Loop
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == 'Add':
        # change the "test" element to be the value of "task" element
        pass
    if event == "-POPUP-":
        #Popup even if the user doesn't add any text for a ToDo
        event, values = sg.Window("WARNING:",
            [[sg.T("You need to input something"),sg.B("OK")]],
            auto_close = True,
            no_titlebar = True,).read(close=True)
#part of the PySimpleGUI to make sure everything is closed
window.close()
