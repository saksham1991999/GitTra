import os

from utilities import comment_translator
from utilities import fileType


# implement new module to get a .traignore file from the commandline
translation_ignore = ['.git', 'node_modules']

# need to import gitignore file
gitignore = []

def translate_file(filename, initial_dir, final_dir, language):
    original_file = open(os.path.join(initial_dir, filename), mode='r+', encoding="utf8")
    translated_file = open(os.path.join(final_dir, filename), "w", encoding="utf-8")
    mime = fileType.get_parser_mime(path=filename)
    if mime == 'none':
        return
    file_content = original_file.read()
    translated_content = comment_translator.translate_file_comments(file_content, language=language, mime=mime)
    translated_file.write(translated_content)

def parse_directory(initial_dir, final_dir, language):
    current_dir = os.path.abspath(os.getcwd())
    walk_dir = os.path.join(current_dir, initial_dir)
    os.makedirs(os.path.join(current_dir, final_dir), exist_ok=True)
    
    try:
        f = open(os.path.join(walk_dir, ".gitignore"), "r")
        gitignore = list(map(lambda x: x.strip("\n"), f.readlines()))
    except:
        gitignore = []
    for root, subdirs, files in os.walk(walk_dir, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in translation_ignore]
        subdirs[:] = [d for d in subdirs if d not in gitignore]
        files[:] = [d for d in files if d not in translation_ignore]
        files[:] = [d for d in files if d not in gitignore]
        final_root = root.replace(initial_dir, final_dir)
        os.makedirs(final_root, exist_ok = True)
        for file in files:
            translate_file(file, root, final_root, language)


parse_directory("original_dir", "translated_dir", "en")
