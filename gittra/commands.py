import click
import sys
import os

from gittra import script
from gittra.utilities.git.gitcommands import *

@click.group()
def cli():
    pass


@cli.command()
@click.argument("repo", type=str)
@click.argument("lang", type=str)
@click.option("-n", "--rename", type=str, help="Specify the name of the directory to clone into")
def clone(repo, lang, rename, name="clone"):
    """Clones a Github repository and translates all comments"""
    if rename:
        gitclone(repo, lang, rename)
    else:
        gitclone(repo, lang, "translated")


@cli.command()
@click.argument("repo", type=str)
@click.argument("lang", type=str)
def fork(repo, lang, name="fork"):
    """Forks a Github repository and creates a translated branch"""
    gitfork(repo, lang)


@cli.command()
@click.argument("lang", type=str)
def push(name="push"):
    """Pushes into the translated branch of the Github fork"""
    gitpush()