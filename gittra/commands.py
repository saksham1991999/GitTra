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
def clone(repo, lang, name="clone"):
    """Clones a Github repository and creates a translated branch"""
    gittra_clone(repo, lang)


@cli.command()
@click.argument("repo", type=str)
@click.argument("lang", type=str)
def fork(repo, lang, name="fork"):
    """Forks a Github repository and creates a translated branch"""
    gittra_fork(repo, lang)


@cli.command()
def push(name="push"):
    """Pushes into the translated branch of the Github fork"""
    gittra_push()