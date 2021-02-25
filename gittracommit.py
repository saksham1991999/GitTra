import sys
import os
import subprocess
#for gittra push

#taken directory: original directory
def gittraCommit(message):
    #concatenating the command
    push = "git commit -m"
    #rm .git/index
    p = subprocess.Popen(["git", "add", "."], cwd=os.path.join(os.getcwd(), "original_dir"))
    p.wait()
    p = subprocess.Popen(["git", "commit", "-m", message], cwd=os.path.join(os.getcwd(), "original_dir"))
    p.wait()
    
try:
    message = (sys.argv)[1]
    gittraCommit(message)
except ValueError:
    print("Git commit err: commit message necessary")   
