'''
Simple Sorter, most easy little program made for actual
use in real-life. Takes in a simple text file and creates
a new one with names or objects sorted in alphabetical
order
'''
import PySimpleGUI as sg
sg.theme("Dark Grey 13")

#Global Variable
master_list = []
user_input = ""
user_output = ""

#the function sorts the file
def Sorter(x):
    if type(x) != list:
        print ("Not a proper input")
        pass
    else:
        x.sort()

#the function that opens the file and creates the list
def OpenFile(x):
    global master_list
    try:
        f = open(x,"r")
        for x in f:
            x = x.strip("\n")
            master_list.append(x)
        f.close()
    except:
        pass

#function that saves the file
def SaveFile(x):
    global master_list
    try:
        f = open(x, "a")
        for x in master_list:
            f.write(x + "\n")
        f.close()
    except:
        pass
