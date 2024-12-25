#!/usr/bin/python3

import sys
import os
from datetime import date

foldername = (input ('Folder Name?'))

new_directory = "/home/helloxonie/code"
os.chdir = (new_directory) #use absolute path to directory you want to create folders in.

try:
    os.mkdir (foldername)
    print('Folder Created')

except FileExistsError:
    print('Folder already exists')

finally:
    file = open('README.md', 'w+') 
