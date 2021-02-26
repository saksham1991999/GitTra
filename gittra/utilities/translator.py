from google_trans_new import google_translator
from googletrans import Translator, LANGUAGES

translator = Translator()
languages = LANGUAGES

#function to call the translate API
#args: comment string and destination language
def translate_comment(comment, dest):
    translator = google_translator()
    translate_text = translator.translate(comment,lang_tgt=dest)
    return translate_text

#function to detect a comment
def detect_comment(comment):
    return translator.detect(comment).lang
