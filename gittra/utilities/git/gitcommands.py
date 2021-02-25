import click
import sys
import os

from gittra.script import parse_back, parse_directory

# forks the repo
def gitfork(remote, language):
    
    # forks the original repo
    forkCLI = "gh repo fork " + remote + "--clone=true --remote=true" 

    # creates new translated branch
    os.system("git checkout -b translated")

    # translate all comments in the entire repo
    repoName = remote.split('.git')[0].split('/')[-1]
    parse_directory(repoName, repoName, language)

    # saves changes to remote
    os.system("git add . && git commit -m 'initial commit on translated branch'")
    os.system("git push --set-upstream origin translated")

    # todo: set up Github action for future pushes


# pushes commits into translated branch
def gitpush():

    os.system("sshpass -p your_password ssh user_name@your_localhost")
    # ensures changes are being made to the translated branch
    os.system("git checkout translated")
    # pushes changes into translated branch
    os.system("git push") 


def gitclone(remote, language, dirName):
    if not dirName:
        dirName = "translated-repo"
    cloneCLI = "git clone " + remote + " " + dirName
   
    os.system("sshpass -p your_password ssh user_name@your_localhost")
    path  = os.getcwd()
    os.chdir(path) # specifies the path where the cloned project needs to be copied
    os.system(cloneCLI) # clone into directory
    
    parse_directory(dirName, dirName, language)