import sys
import os

import subprocess
#for gittra push

#taken directory: original directory

#concatenating the command
def gittraPush(origin, branch):
    p = subprocess.Popen(["git", "push", origin, branch], cwd=os.path.join(os.getcwd(), "original_dir"))
    p.wait()

try:
    origin = (sys.argv)[1]
    branch = (sys.argv)[2]

    gittraPush(origin, branch)
except ValueError:
    print("Git push err: remote name needed in the form: gittra push [remote] [branch]")  