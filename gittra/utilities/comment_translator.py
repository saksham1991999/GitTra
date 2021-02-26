from collections import defaultdict

from . import comment_parser
from . import translator

#function to translate the comments using the API function calls
#args: content of a file, destination language, and the mime-type
def translate_file_comments(file_content, language, mime=None):
    translated_content = file_content
    translated_copy = defaultdict(str)
    #tranlate each comment
    for comment in comment_parser.extract_comments_from_str(file_content, mime=mime):
        comment_text = comment.text()
        translated_comment = translator.translate_comment(comment_text, language)
        translated_copy[translated_comment] = comment_text
        translated_content = translated_content.replace(comment_text, translated_comment, 1)
    return translated_content, translated_copy


#function to translate back the comments : used when merging
#args: content of a file, a copy of already translated comments ,destination language, and the mime-type
def translate_file_comments_back(file_content, translation_copy, language, mime=None):
    translated_content = file_content
    #Check each comment for translation, if translation exists replace
    for comment in comment_parser.extract_comments_from_str(file_content, mime=mime):
        comment_text = comment.text()
        if comment_text in translation_copy:
            translated_content = translated_content.replace(comment_text, translation_copy[comment_text])
        else:
            translated_comment = translator.translate_comment(comment_text, language)
            translated_content = translated_content.replace(comment_text, translated_comment)
    return translated_content
