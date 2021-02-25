import json
import os

from utilities import comment_translator, fileType, translator


# implement new module to get a .traignore file from the commandline
translation_ignore = ['.git', 'node_modules']

# need to import gitignore file
gitignore = []

def translate_file(filename, initial_dir, final_dir, language):
    original_file = open(os.path.join(initial_dir, filename), mode='r+', encoding="utf8")
    translated_file = open(os.path.join(final_dir, filename), "w", encoding="utf-8")
    mime = fileType.get_parser_mime(path=filename)
    file_content = original_file.read()
    if mime == 'none':
        translated_file.write(file_content)
        return {}
    translated_content, translations_copy = comment_translator.translate_file_comments(file_content, language=language, mime=mime)
    translated_file.write(translated_content)
    return translations_copy

def parse_directory(initial_dir, final_dir, language):
    current_dir = os.path.abspath(os.getcwd())
    walk_dir = os.path.join(current_dir, initial_dir)
    os.makedirs(os.path.join(current_dir, final_dir), exist_ok=True)
    try:
        f = open(os.path.join(walk_dir, ".gitignore"), "r")
        gitignore.append(list(map(lambda x: x.strip("\n"), f.readlines())))
    except Exception as e:
        gitignore = []
    translation_copy = {}
    for root, subdirs, files in os.walk(walk_dir, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in translation_ignore]
        subdirs[:] = [d for d in subdirs if d not in gitignore]
        files[:] = [d for d in files if d not in translation_ignore]
        files[:] = [d for d in files if d not in gitignore]
        final_root = root.replace(initial_dir, final_dir)
        os.makedirs(final_root, exist_ok = True)
        for file in files:
            file_translation_copy = translate_file(file, root, final_root, language)
            translation_copy.update(file_translation_copy)
    json.dump(translation_copy, open(os.path.join(os.path.join(current_dir, final_dir), "translations.json"), "w"))


def translate_file_back(filename, initial_dir, final_dir, translation_copy, language):
    original_file = open(os.path.join(initial_dir, filename), mode='r+', encoding="utf8")
    translated_file = open(os.path.join(final_dir, filename), "w", encoding="utf-8")
    mime = fileType.get_parser_mime(path=filename)
    print(filename)
    file_content = original_file.read()
    if mime == 'none':
        translated_file.write(file_content)
        return {}
    translated_content = comment_translator.translate_file_comments_back(file_content, translation_copy, language=language, mime=mime)
    translated_file.write(translated_content)


def parse_back(initial_dir, final_dir):
    current_dir = os.path.abspath(os.getcwd())
    walk_dir = os.path.join(current_dir, initial_dir)
    os.makedirs(os.path.join(current_dir, final_dir), exist_ok=True)
    translation_ignore.append("translations.json")

    try:
        f = open(os.path.join(walk_dir, ".gitignore"), "r")
        gitignore = list(map(lambda x: x.strip("\n"), f.readlines()))
    except FileNotFoundError as e:
        gitignore = []

    try:
        with open(os.path.join(walk_dir, "translations.json"), "r") as f:
            data = f.read()
        translation_copy = json.loads(data)
    except FileNotFoundError:
        translation_copy = {}

    language = 'en'
    for comment in translation_copy:
        language = translator.detect_comment(translation_copy[comment])
        break
    for root, subdirs, files in os.walk(walk_dir, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in translation_ignore]
        subdirs[:] = [d for d in subdirs if d not in gitignore]
        files[:] = [d for d in files if d not in translation_ignore]
        files[:] = [d for d in files if d not in gitignore]
        final_root = root.replace(initial_dir, final_dir)
        os.makedirs(final_root, exist_ok=True)
        for file in files:
            translate_file_back(file, root, final_root, translation_copy, language)


# parse_directory("original_dir", "translated_dir", "en")

parse_back("translated_dir", "original_dir")

