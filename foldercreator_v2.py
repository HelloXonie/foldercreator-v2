import sys
import os
from datetime import date

foldername = (input ('Folder Name?'))


os.chdir = ('~/code') #use absolute path to directory you want to create folders in.

    try:
        os.mkdir (foldername)
        print('Folder Created')

    except FileExistsError:
        print('Folder already exists')

    finally:
        file = open('README.md', 'w+') 
