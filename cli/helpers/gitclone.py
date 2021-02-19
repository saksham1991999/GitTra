import sys
import os

def clone(remote, language, dirName):
    if not dirName:
        dirName = "translated-repo"
    cloneCLI = "git clone " + remote + " " + dirName
   
    os.system("sshpass -p your_password ssh user_name@your_localhost")
    path  = os.getcwd()
    os.chdir(path) # Specifying the path where the cloned project needs to be copied
    os.system(clone) # Cloning

    walk_dir = os.path.abspath(os.path.join(path, dirName))
    # print('walk_dir (absolute) = ' + walk_dir)

    translation_ignore=[".git","node_modules"]

    for root, subdirs, files in os.walk(walk_dir, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in translation_ignore]
        print(root)