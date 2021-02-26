import sys
import os
import subprocess
#for gittra push

#taken directory: original directory
def gittra_commit(message):
    #concatenating the command
    p = subprocess.Popen(["git", "commit", "-m", message], cwd=os.path.join(os.getcwd(), "original_dir"))
    p.wait() 
