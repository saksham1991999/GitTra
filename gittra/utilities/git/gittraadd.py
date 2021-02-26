import sys
import os
import subprocess
#for gittra push

#taken directory: original directory
def gittra_add(files):
    #concatenating the command
    push = "git add "+ files
    p = subprocess.Popen([push], cwd=os.path.join(os.getcwd(), "original_dir"))
    p.wait()