import sys
import os

print("entered "+str(len(sys.argv))+" arguments")
print("First argument is "+(sys.argv)[1])
remoteGitName = (sys.argv)[1]
path  = os.getcwd() 
clone = "git clone "+remoteGitName 
clone = clone+" translated-project"
print(path)
print(clone)
os.system("sshpass -p your_password ssh user_name@your_localhost")
os.chdir(path) # Specifying the path where the cloned project needs to be copied
os.system(clone) # Cloning
print("!!! Remote Repo cloned as translated-project")

#duplicate the repository just created

#go inside the newly created directory and read all the comments

#recursively find the files to be worked on
    #for each of the files: 
        # find the type of file
        #based on the type of file find comments
        #translate each of the comments using the google API
            #replace the comments in-line
