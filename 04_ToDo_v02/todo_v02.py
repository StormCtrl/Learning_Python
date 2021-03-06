#modules needed for this program
import json
import os

#Global variables
todo_list = {"ID":1} #dictionary where all the data is stored
               #Below is how it looks like it per entry
               #{55 : "StringInput", "-IDTAG_55-"}
               #Will be overwriten by load function
idcounter = 1 #Counts up as you create objects, making sure every object gets
              #their own ID. Will be overwriten by load function
todo_json = "" #JSON formated todo_list

#Saving, Loading, Deleting & Reset from data.json - use it when closing program
def save_todo():
    global todo_json
    global todo_list
    todo_json = json.dumps(todo_list)
    x = open("data.json", "w") #open the file
    x.write(todo_json) #write away the json
    x.close()

def load_todo():
    global todo_list
    global todo_json
    global idcounter
    if os.path.exists("data.json"):
        x = open("data.json", "r") #open the file
        todo_json = x.read() #read the file
        x.close() #making sure you close it
        todo_list = json.loads(todo_json) #convert json back to dictionary
        idcounter = todo_list.get("ID")
    else:
        save_todo()

def reset_todo():
    global idcounter
    global todo_list
    global todo_json
    if os.path.exists("data.json"):
        os.remove("data.json")
        idcounter = 1
        todo_list = {"ID":1}
        todo_json = ""
        save_todo()
    else:
        print("The file does not exist")

#Only function that can be used during the program
def del_todo(x):
    todo_list.pop(x)

#function to create a single todo object
def create_todo(x):
    global todo_list
    global idcounter
    global todo_json
    idTag = "-IDTAG_" + str(idcounter) + "-"
    #update the dictionary
    todo_list[idTag] = x
    #+ 1 to the idcounter
    idcounter = idcounter + 1
    todo_list["ID"] = idcounter
    todo_json = json.dumps(todo_list) #convert data to json

#function to print out all the todo objects
def show_todo():
    for x in todo_list.values():
        print(x)

#function for testing:
def quick_create_todo():
    for x in range(1,11):
        sample = "Test Sample #" + str(x)
        create_todo(sample)

#Printing ToDo_List to the Console for debugging - only works when you are
#within the .py file itself
if __name__ == "__main__":
    quick_create_todo()
    save_todo()

load_todo()
