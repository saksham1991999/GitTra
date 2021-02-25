import sys
import os
import subprocess
from gittracommit import gittraCommit

#for gittra pull
#commit the current changes in the original directory


#taken directory: original directory
def gittraPull(origin, branch)
    #concatenating the command
    push = "git pull"+(sys.argv)[1] + (sys.argv)[2]
    p = subprocess.Popen([push], cwd=os.path.join(os.getcwd(), "original_dir"))
    p.wait()

try:
    origin = (sys.argv)[1]
    branch = (sys.argv)[2]
except:
    print("Git commit err: commit message necessary; enter two arguments:gitta pull [origin] [branch]")