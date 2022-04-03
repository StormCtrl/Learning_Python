'''
I've noticed I need often something that can generate a lot of data
This module will help me generate different data sets:
- List of Random Intergers (logical)
- List of Random Floats (logical)
- List of Random Strings (readable)
- Dictionary with Keys & Values
- Dictionary with Keys & Multiple Values in a List
'''
#Import modules
import random

list_callsigns = ["Alpha",
                "Beta",
                "Charlie",
                "Delta",
                "Echo",
                "Foxtrot",
                "Gamma"]

list_short_abc = "ABCDEFGHIJKLMNO"

def gen_int(x):
    gen_int_list = []
    for x in range(1,x):
        y = random.randint(100,999)
        gen_int_list.append(y)
    return gen_int_list

def gen_float(x):
    gen_float_list = []
    for x in range(1,x):
        y = random.random()
        gen_float_list.append(y)
    return gen_float_list

def gen_abc(x):
    gen_abc_list = []
    abc_lenght = len(list_short_abc)
    for x in range(1,x):
        r = random.randint(0,abc_lenght-1)
        y = list_short_abc[r-1]
        gen_abc_list.append(y)
    return gen_abc_list

def gen_string(x):
    gen_string_list = []
    strings_lenght = len(list_callsigns)
    for x in range(1,x):
        r = random.randint(0,strings_lenght-1)
        a = gen_abc(2)[0]
        b = gen_abc(2)[0]
        y = list_callsigns[r] + "_"
        y = a + "_" + y + str(random.randint(100,999)) + b
        gen_string_list.append(y)
    return gen_string_list

def gen_dict(x):
    gen_dict = {}
    for x in range(1,x):
        # a = gen_int(2)[0]
        b = gen_string(2)[0]
        gen_dict[x]=b
    return gen_dict

def gen_dict_array(x):
    gen_dict_array = {}
    gen_dict_list = []
    for x in range(1,x):
        a = gen_int(2)[0]
        b = gen_string(2)[0]
        c = gen_abc(2)[0]
        gen_dict_array[x]=[a,b,c]
    return gen_dict_array
