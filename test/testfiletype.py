from utilities.fileType import get_magic_mime, get_parser_mime
import os

path = os.path.join(os.getcwd(), "test.py")

assert get_magic_mime(path) == 'text/plain'
assert get_parser_mime(path) == 'text/x-python'
