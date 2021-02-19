import os

translation_ignore=[]
gitignore = []
walk_dir = os.path.abspath(os.getcwd())
for root, subdirs, files in os.walk(walk_dir, topdown=True):
    subdirs[:] = [d for d in subdirs if d not in translation_ignore]
    subdirs[:] = [d for d in subdirs if d not in gitignore]
    files[:] = [d for d in files if d not in translation_ignore]
    files[:] = [d for d in files if d not in gitignore]
    print("Root: ",root)
    for file in files:
        #for all files call the translation module
        #translate_file_comments(files)
        print("File Name:", file)
        break