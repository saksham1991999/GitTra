"""
This module is for identifying the filetype of the code and returning the type of file, based on the extensions
"""
import os


MIME_MAP = {
    '.html': 'text/html',  # HTML
    '.c': 'text/x-c',  # C
    '.cpp': 'text/x-c++',  # C++/C#
    '.cs': 'text/x-c++',  # C++/C#
    '.cxx': 'text/x-c++',  # C++/C#
    '.go': 'text/x-go',  # Go
    '.java': 'text/x-java',  # Java
    '.jsp': 'text/x-java-source',  # Java
    '.js': 'text/x-javascript',  # Javascript
    '.py': 'text/x-python',  # Python
    '.ruby': 'text/x-ruby',  # Ruby
    '.sh': 'text/x-shellscript',  # Unix shell
    '.xml': 'text/xml',  # XML
}


def get_parser_mime(path):
    filename, file_extension = os.path.splitext(path)
    try:
        mime = MIME_MAP[file_extension]
        return mime
    except:
        return 'none'
