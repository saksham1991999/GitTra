#This module is for identifying the filetype of the code and returning the type of file, based on the extensions

import magic

def get_mime(path):
    mime = magic.from_file("{}".format(path), mime=True)
    return mime