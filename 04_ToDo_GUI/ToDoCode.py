'''
ToDo code adjusted for use in combination with PySimpleGUI
All code that is made for the CMD console menu or interaction has been removed.
Also few aspects are trimmed down to keep the build-up short.
Adding an save and load function to make sure the program persists after closed.
'''
#modules needed for this program
import os

#Global variables
ToDo_List = {} #dictionary where all the objects are stored
               #Below is how it looks like it per object
               #{"-IDTAG_55-" : "StringInput", "GUI", 55}
               #Will be overwriten by load function
idcounter = 1 #Counts up as you create objects, making sure every object gets
              #their own ID. Will be overwriten by load function

#ToDo Class to create todo objects
class ToDo:
    def __init__(self, title, gui, id):
        self.title = title
        self.id = id
        self.gui = gui

#saves the object & reload
def save_ToDo():
    pass

#loads the save file
def load_ToDo():
    pass

#function to create a single todo object - old version. New Insights.
def createToDo_old(x):
    #create an ID tag for the object
    global idcounter
    idTag = "-IDTAG_" + str(idcounter) + "-"
    idNr = "ID_" + str(idcounter)
    idInput = str(idcounter)
    idcounter = idcounter + 1

    #This part of the code creates the GUI parts of it
    gui = """layout_ToDo_{} = [[sg.Text({}), sg.Button("Done", key="{}")]]"""
    gui = gui.format(idNr, x, idTag)

    #create the actual ToDo by calling the class to create object
    globals()[idNr] = ToDo(x, gui, idInput)
    #include this object in the global ToDo_Dictionary
    ToDo_List.update({idTag:globals()[idNr]})

#function to create a single todo object
def createToDo(x):
    #create an ID tag for the object
    global idcounter
    idTag = "-IDTAG_" + str(idcounter) + "-"
    idNr = "ID_" + str(idcounter)
    idInput = str(idcounter)
    idcounter = idcounter + 1

    #This part of the code creates the GUI parts of it
    gui = """layout_ToDo_{} = [[sg.Text({}), sg.Button("Done", key="{}")]]"""
    gui = gui.format(idNr, x, idTag)

    #create the actual ToDo by calling the class to create object
    globals()[idNr] = ToDo(x, gui, idInput)
    #include this object in the global ToDo_Dictionary
    ToDo_List.update({idTag:globals()[idNr]})

#function to print out all the todo objects
def showToDo():
    for x in ToDo_List.values():
        print(x.title + " ID:" + x.id + " " + x.gui)

#function that deletes an entry in todo dictionary
def del_ToDo_simple(x):
    x = str(x).lower()
    x = "-IDTAG_" + x + "-"
    ToDo_List.pop(x)

#Printing ToDo_List to the Console for debugging - only works when you are
#within the .py file itself
if __name__ == "__main__":
    print("DEBUGGING -----------------:")
    print("Load a file if there is any:")
    load_ToDo()
    print("\n")

    for x in range(1,11):
        #print("Creating ToDo: Nr" + str(x))
        createToDo("Number " + str(x) + " on my to do list for debugging.")

    print("Print the dictionary properly by calling function to Console #1:")
    showToDo()

    print("\nDeleting some objects........")
    del_ToDo_simple(1)
    del_ToDo_simple(4)
    del_ToDo_simple(8)

    print("Print the dictionary properly by calling function to Console #2:")
    showToDo()
