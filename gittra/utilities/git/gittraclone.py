import sys
import os
import shutil
from gittra.utilities import comment_translator
from gittra.utilities import fileType
from gittra import script
from gittra.utilities import ascii

def gittra_clone(remote, language):

    # concatenating git command
    path = os.getcwd()
    clone = "git clone " + remote

    dirname = "original_dir"
    clone = clone + " " + dirname

    #commented for testing
    #ensure the person is signed in with ssh-pass
    #os.system("sshpass -p your_password ssh user_name@your_localhost")

    os.chdir(path)  # Specifying the path where the cloned project needs to be copied
    os.system(clone)  # Cloning
    print("!!! Remote Repo cloned as original-project")

    # source to be copied
    src = os.path.join(path, "original_dir")

    # walking directory
    walk_dir = os.path.abspath(os.path.join(path, "original_dir"))

    print('walk_dir (absolute) = ' + walk_dir)

    #parse comments and commit
    script.parse_directory("original_dir", "translated_dir", language)

    print("\n")
    ascii.getAscii()