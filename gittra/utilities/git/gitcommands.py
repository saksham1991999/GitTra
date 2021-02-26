import click
import sys
import os
import subprocess

from gittra.script import parse_back, parse_directory
from gittra.utilities import ascii


# forks the repo
def gittra_fork(remote, language):
    
    # forks the original repo
    forkCLI = "gh repo fork " + remote + " --clone=true --remote=true" 
    os.system(forkCLI)
    repoName = remote.split('/')[-1]
    os.chdir(repoName)

    # creates new translated branch
    os.system("git checkout -b translated")

    # translate all comments in the entire repo
    parse_directory("", "", language)

    # saves changes to remote
    os.system("git add . && git commit -m 'initial commit on translated branch'")
    os.system("git push --set-upstream origin translated")

    # prints ascii message
    ascii.getAscii()


# pushes commits into translated branch
def gittra_push():

    # ensures changes are being made to the translated branch
    os.system("git checkout translated")
    # pushes changes into translated branch
    os.system("git push") 

    # also updates the main branch
    os.system("git push --force main")
    os.system("git checkout main")
    parse_back("", "")

    # prints ascii message
    ascii.getAscii()


def gittra_clone(remote, language):
    
    # clones the repo
    cloneCLI = "git clone " + remote
    os.system(cloneCLI)
    repoName = remote.split('/')[-1]
    os.chdir(repoName)

    # creates new translated branch
    os.system("git checkout -b translated")

    # translate all comments in the entire repo
    parse_directory("", "", language)

    # prints ascii message
    ascii.getAscii()
