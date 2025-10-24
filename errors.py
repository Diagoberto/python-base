#! /usr/bin/env python3

import os
import sys

# LBYL - Look Before You Leap

# EAFP - Easy to Ask forgiveness then permission
# (Eh mais facil pedir perdao do que permissao
#######################################

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e: 
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(2)

