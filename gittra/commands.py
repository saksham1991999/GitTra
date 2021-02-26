import click
import sys
import os

from gittra import script
from gittra.utilities.git.gittraclone import gittra_clone
from gittra.utilities.git.gittramerge import gittra_merge
from gittra.utilities.git.gittrapush import gittra_push
from gittra.utilities.git.gittraadd import gittra_add
from gittra.utilities.git.gittracommit import gittra_commit
from gittra.utilities.git.gittrapull import gittra_pull

@click.group()
def cli():
    pass

@cli.command()
@click.argument("repo", type=str)
@click.argument("lang", type=str)
def clone(repo, lang, name="clone"):
    """Clones a Github repository:: gittra clone [remote] [language=en]"""
    gittra_clone(repo, lang) 

@cli.command()
@click.argument("initial", type=str)
@click.argument("final", type=str)
def merge(initial, final, name="merge"):
    """Clones a Github repository:: gittra merge [original] [translated]"""
    """: usage: gittra clone []"""
    gittra_merge(initial, final)


@cli.command()
@click.argument("origin", type=str)
@click.argument("branch", type=str)
def push(origin, branch, name="push"):
    """Pushes merged original into remote:: gittra push [origin] [branch]"""
    gittra_push(origin, branch)

@cli.command()
@click.argument("origin", type=str)
@click.argument("branch", type=str)
def pull(origin, branch, name="pull"):
    """Pulls the original untransalted directory:: gittra pull [origin] [branch]"""
    gittra_pull(origin, branch)

@cli.command()
@click.argument("files", type=str)
def add(files, name="add"):
    """Adds original files for staging:: gittra add [.]"""
    gittra_add(files)

@cli.command()
@click.argument("message", type=str)
def commit(message, name="commit"):
    """Makes a commit for the original file:: gittra commit [.]"""
    gittra_add(message)