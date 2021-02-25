import sys
import os
import subprocess
#for gittra push

#taken directory: original directory
def gittraAdd():
    #concatenating the command
    push = "git add"+(sys.argv)[1]
    p = subprocess.Popen([push], cwd=os.path.join(os.getcwd(), "original_dir"))
    p.wait()
    

files = []
try:
    
except ValueError:
        print("Git commit err: commit message necessary")