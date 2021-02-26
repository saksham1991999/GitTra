import sys
import os
import subprocess

#function to execute push from original directory concatenating the command
def gittra_push(origin, branch):
    p = subprocess.Popen(["git", "push", origin, branch], cwd=os.path.join(os.getcwd(), "original_dir"))
    p.wait()