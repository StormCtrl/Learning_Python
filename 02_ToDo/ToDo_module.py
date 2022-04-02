#modules needed for this program
import os
import keyboard
from kivy.app import App
from kivy.uix.button import Button
from time import sleep

#Global variables
ToDo_List = {}
idcounter = 1
clearview = True #clears the view of console

#Kivy Code to create the Primary interface
class ToDoApp(App):
    def build(self):
        return Button(text="Hello!",
                      background_color=(0,0,0,1),
                      font_size = 150)

#ToDo Class to create todo objects
class ToDo:
    def __init__(self, title, description, priority, id):
        self.title = title
        self.description = description
        self.priority = priority
        self.id = id

#function to create a single todo object
def createToDo():
    #request input
    x = input("What do you need to do?")
    if x == "":
        print("ToDo without input = nothing. You have nothing to do?")
        sleep(2)
        os.system("cls")
        command_menu()

    y = input("Do you have more details?")
    if y == "":
        y = "No Details"

    z = input("Is this a priority task? y/n ").lower()
    if z == "y" or z == "yes" or z == "yeah" :
        z = "This is a Priority Task"
    else:
        z = "No Priority"
    #create an ID tag for the object
    global idcounter
    idTag = "IDTAG_" + str(idcounter)
    idNr = "ID_" + str(idcounter)
    idInput = str(idcounter)
    idcounter = idcounter + 1
    #create the actual ToDo by calling the class to create object
    globals()[idNr] = ToDo(x,y,z,idInput)
    #include this object in the global ToDo_Dictionary
    ToDo_List.update({idTag:globals()[idNr]})
    os.system("cls")
    command_menu()

#function to print out all the todo objects
def showToDo():
    print("These are your ToDo's:")
    for x in ToDo_List.values():
        print("-----------------------------" + "ID:" + x.id)
        print(x.title)
        print(x.description)
        print(x.priority)

#function to print out all the todo objects
def showToDo_short():
    print("These are your ToDo's:")
    for x in ToDo_List.values():
        print("ID:" + x.id + " - " + x.title)

#function that deletes an entry in todo dictionary
def del_ToDo_simple():
    showToDo_short()
    x = input("Which ToDo do you want to remove(#nr)? ")
    try:
        x = "IDTAG_" + x
        ToDo_List.pop(x)
    except:
        os.system("cls")
        print("There is no ToDo with that ID - returning to menu")
        sleep(2)
    os.system("cls")
    command_menu()

#function that create an infinite loop menu
def command_menu():
    print("ToDo List - by Daniel van Veldhoven")
    print("\nMenu -------------------------------------------------------------")
    print("Add ToDo [1] / Remove ToDo [2]")
    print("\nList -------------------------------------------------------------")
    showToDo()
    while True:
        if keyboard.is_pressed("1"):
            print("Time to Create a new ToDo")
            os.system("cls")
            createToDo()
        elif keyboard.is_pressed("2"):
            print("Time to Delete a new ToDo")
            os.system("cls")
            del_ToDo_simple()

#This launches the App
if __name__ == "__main__":
    ToDoApp().run()
