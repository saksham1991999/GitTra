import click
import sys
import os


# forks the repo
def gitfork(remote, language, addClone):
    
    # forks the original repo
    forkCLI = "gh repo fork " + remote
    if addClone:
        forkCLI = forkCLI + " --clone=true"

    # creates new translated branch
    os.system("git checkout -b translated")

    # todo: translate all comments in the entire repo

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
    os.chdir(path) # Specifying the path where the cloned project needs to be copied
    os.system(cloneCLI) # Cloning

    walk_dir = os.path.abspath(os.path.join(path, dirName))
    # print('walk_dir (absolute) = ' + walk_dir)

    translation_ignore=[".git","node_modules"]

    for root, subdirs, files in os.walk(walk_dir, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in translation_ignore]
        print(root)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("repo", type=str)
@click.argument("lang", type=str)
@click.option("-n", "--rename", type=str, help="Specify the name of the directory to clone into")
def fork(repo, lang, rename, name="fork"):
    """Forks a Github repository and creates a translated branch"""
    if rename:
        gitclone(repo, lang, rename)
    else:
        gitclone(repo, lang, "translated")


@cli.command()
@click.argument("lang", type=str)
def push(name="push"):
    """Pushes into the translated branch of the Github fork"""
    gitpush()
def clone(repo, lang, rename, name="clone"):
    """Clones a Github repository with translated comments"""
    if rename:
        gitclone(repo, lang, rename)
    else:
        gitclone(repo, lang, "translated")
