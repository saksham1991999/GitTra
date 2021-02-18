from googletrans import Translator, LANGUAGES


translator = Translator()
languages = LANGUAGES


def detect_comment(comment):
    return translator.detect(comment).lang


def translate_comment(comment, dest):
    return translator.translate(comment, dest=dest).text