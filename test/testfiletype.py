
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from utilities.fileType import get_magic_mime, get_parser_mime

path = os.path.join(os.getcwd(), "..\original_dir\README.md")

assert get_magic_mime(path) == 'text/plain'
assert get_parser_mime(path) == 'text/x-python'
