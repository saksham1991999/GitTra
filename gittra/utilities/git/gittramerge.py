import sys
import os

from gittra.script import parse_back

#function to call merge inside the original directory
def gittra_merge(initial_dir, final_dir):
    parse_back(initial_dir, final_dir)
