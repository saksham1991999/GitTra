from utilities import comment_translator
from utilities import fileType

def translate_file(filename, initial_dir, final_dir, language):
    original_file = open(initial_dir + filename, mode='r+', encoding="utf8")
    translated_file = open(final_dir + filename, "w", encoding="utf-8")
    # mime = fileType.get_mime(path)  # Don't understand why it isn't working
    mime ='text/x-python'
    file_content = original_file.read()
    translated_content = comment_translator.translate_file_comments(file_content, language=language, mime=mime)
    translated_file.write(translated_content)

# for root, subdirs, files in os.walk(walk_dir, topdown=True):
#     subdirs[:] = [d for d in subdirs if d not in translation_ignore]
#
#
#     print(root)