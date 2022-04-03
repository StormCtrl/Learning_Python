#Importing Modules
import PySimpleGUI as sg
from todo_v02 import *
sg.theme('DarkAmber')

#layout that makes sure I get the correct input for a new ToDo Object
layout_input = [
    [sg.Input(key="-TASK-"), sg.Button("Add", key="-ADD-")],
    [sg.Text("", key="-TEST-")],
    [sg.Button("Reset", key="-RESET-")]
    ]

#layout for a single todo object, will have to create a class for this
input_task_list = []
def todo_to_list():
    for x in todo_list.values():
        input_task_list.append(x)
todo_to_list()

layout_each_task = [sg.Listbox(input_task_list,
                        size=(50,15),
                        enable_events=True,
                        key="-LIST-",
                        right_click_menu=["Name","Delete"],
                        )]

#I'll have to make a variable that can be called that will list all the tasks
layout_all_tasks = [
    [sg.Frame("Your ToDo",
    [layout_each_task],
    element_justification = "center",
    vertical_alignment = "center")]
    ]

#Ofcourse, I have to put my name on it
layout_credits = [
    [sg.Text("Program made by Daniel van Veldhoven", justification = "center")]
    ]

#Combining all the layouts togehter
layout = layout_input + layout_all_tasks + layout_credits



print(layout_each_task)
for x in layout_each_task:
    print(x)
#How the window will look like
window = sg.Window('ToDo',
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
    if event == sg.WIN_CLOSED or event == "EXIT":
        save_todo()
        break
    if event == "-ADD-":
        create_todo(values["-TASK-"])
    if event == "-RESET-":
        reset_todo()
    #need to add code to remove elements/tasks

#part of the PySimpleGUI to make sure everything is closed
window.close()
