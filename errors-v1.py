#! /usr/bin/env python3

import os
import sys

if os.path.exists("names.txt"):
    print("O arquivo names.txt existe")
    input("...") # Race Condition
    names = open("names.txt").readlines()
else:
    print("Error: File names.txt not found.")
    sys.exit(1)


# LBYL - Look Before You Leap

##names = ["Diago", "Beto", "Diagoberto"]

if len(names) >= 3:
    print(names[1])
else:
    print("Error: Missing name in the list")
    sys.exit(2)

