#! /usr/bin/env python3

import os
import sys

# LBYL - Look Before You Leap

# EAFP - Easy to Ask forgiveness then permission
# (Eh mais facil pedir perdao do que permissao

try:
    names = open("names.txt").readlines()
    1 / 1 #ZeroDivisionError
    print(names.append) #Attributor
except FileNotFoundError: 
    print("Error: File names.txt not found.")
    sys.exit(1)
except ZeroDivisionError:
    print("Error: You cant divide by zero!!!")
    sys.exit(1)
except AttributeError: 
    print("Error: List doesnt  banana!!!")
    sys.exit(1)
    

try:
    print(names[3])
except:
    print("Error: Missing name in the list")
    sys.exit(2)

