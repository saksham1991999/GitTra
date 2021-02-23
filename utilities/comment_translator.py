from collections import defaultdict

from . import comment_parser
from . import translator


def translate_file_comments(file_content, language, mime=None):
    translated_content = file_content
    translated_copy = defaultdict(str)
    for comment in comment_parser.extract_comments_from_str(file_content, mime=mime):
        comment_text = comment.text()
        translated_comment = translator.translate_comment(comment_text, 'en')
        translated_copy[translated_comment] = comment_text
        translated_content = translated_content.replace(comment_text, translated_comment, 1)
    return translated_content, translated_copy
