import sys
import os
import shutil
from utilities import comment_translator
from utilities import fileType
from script import parse_directory
from utilities import ascii

print("entered " + str(len(sys.argv)) + " arguments")
print("First argument is " + (sys.argv)[1])

# concatenating git command
remoteGitName = (sys.argv)[1]
path = os.getcwd()
clone = "git clone " + remoteGitName

dirname = "original_dir"
clone = clone + " " + dirname

print(path)
print(clone)
os.system("sshpass -p your_password ssh user_name@your_localhost")
os.chdir(path)  # Specifying the path where the cloned project needs to be copied
os.system(clone)  # Cloning
print("!!! Remote Repo cloned as original-project")


# duplicate the repository just created

# go inside the newly created directory and read all the comments
# name of directory is translated-project

# recursively find the files to be worked on
# for each of the files:
# find the type of file
# based on the type of file find comments
# translate each of the comments using the google API
# replace the comments in-line

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well.


# source to be copied
src = os.path.join(path, "original_dir")

# walking directory
walk_dir = os.path.abspath(os.path.join(path, "original_dir"))

print('walk_dir (absolute) = ' + walk_dir)

# removing git info for the translated directory
# shutil.rmtree(os.path.join(dst, ".git"))

#parse comments and commit
parse_directory("original_dir", "translated_dir", "en")

print("\n\n\n")
ascii.getAscii()