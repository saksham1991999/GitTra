#make commits to the origin git repository
import sys
import os
import shutil
import translator

def commit():
    #make add all files after entering the directory
    os.system("cd translated-project")

    os.system("git add .")

    #make a commit
    os.system('commit -m "translate project"')

    #go out of the directory
    os.system("cd ..")