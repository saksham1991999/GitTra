import sys
import os
import shutil

from utilities import comment_translator
from utilities import fileType

print("entered " + str(len(sys.argv)) + " arguments")
print("First argument is " + (sys.argv)[1])

# concatenating git command
remoteGitName = (sys.argv)[1]
path = os.getcwd()
clone = "git clone " + remoteGitName

dirname = "original-project"
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

def translate_file(filename, language):
    original_file = open(os.path.join(initial_dir, filename), mode='r+', encoding="utf8")
    translated_file = open(os.path.join(final_dir, filename), "w", encoding="utf-8")
    mime = fileType.get_parser_mime(filename)
    file_content = original_file.read()
    translated_content = comment_translator.translate_file_comments(file_content, language=language, mime=mime)
    translated_file.write(translated_content)


# source to be copied
src = os.path.join(path, "original-project")

# walking directory
walk_dir = os.path.abspath(os.path.join(path, "original-project"))

print('walk_dir (absolute) = ' + walk_dir)

# removing git info for the translated directory
# shutil.rmtree(os.path.join(dst, ".git"))

# implement new module to get a .traignore file from the commandline
translation_ignore = [".git", "node_modules"]

# need to import gitignore file
gitignore = []

for root, subdirs, files in os.walk(walk_dir, topdown=True):
    subdirs[:] = [d for d in subdirs if d not in translation_ignore]
    subdirs[:] = [d for d in subdirs if d not in gitignore]
    files[:] = [d for d in files if d not in translation_ignore]
    files[:] = [d for d in files if d not in gitignore]
    print(root)
    for file in files:
        # for all (text-based) files call the translation module
        if (fileType.get_magic_mime(file) == 'text/plain'):
            translate_file(file, 'en')
