# -------------------
# -- File Handling --
# -------------------
# "a" Append   Open file appending values, Create file if not exists
# "r" Read     [Default Value] Open file for read and give error if file is not exists
# "w" Write    Open file for writing, Create file if not exists
# "x" Create   Create File, Give Error If File Exists
# ---------------------------------------------------

import os 

print(os.getcwd()) # main current working Directory

print(os.path.dirname(os.path.abspath(__file__)))  # Directory for the opened file

#print(os.path.abspath(__file__))

#file = open("Walid.txt")  # Absoulate path

