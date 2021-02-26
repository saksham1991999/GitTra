import sys
import os
import subprocess

#for gittra pull
#commit the current changes in the original directory


#taken directory: original directory
def gittra_pull(origin, branch):
    #concatenating the command
    p = subprocess.Popen(["git", "pull", origin, branch], cwd=os.path.join(os.getcwd(), "original_dir"))
    p.wait()