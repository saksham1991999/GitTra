import sys
import os
from zipfile import ZipFile

from ..translator import parse_directory


def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def get_username_reponame(url):
    url = url.strip().replace("https://", "")
    url = url.replace("github.com/", "")
    username, repo_name = url.split("/")
    return username, repo_name


def git_clone(url):
    username, repo_name = get_username_reponame(url)
    path = os.getcwd()
    media_path = os.path.join(path, "media")
    user_path = os.path.join(media_path, username)
    os.makedirs(user_path, exist_ok=True)

    clone = "git clone " + url
    # os.system("sshpass -p your_password ssh user_name@your_localhost")
    os.chdir(user_path)
    os.system(clone)
    return repo_name, user_path


def translate_repo(repo_name, user_path, language):
    repo_path = os.path.join(user_path, repo_name)
    translated_repo_path = os.path.join(user_path, repo_name + "-translated-"+language)
    zip_path = os.path.join(user_path, repo_name + "-translated-" + language + ".zip")
    parse_directory(repo_path, translated_repo_path, language)
    zip_file(zip_path, translated_repo_path)
    return zip_path


def zip_file(zip_path, translated_repo_path):
    file_paths = get_all_file_paths(translated_repo_path)
    with ZipFile(zip_path, 'w') as zip:
        for file in file_paths:
            zip.write(file)
