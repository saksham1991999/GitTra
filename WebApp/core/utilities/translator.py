from googletrans import Translator, LANGUAGES


translator = Translator()
languages = LANGUAGES


def detect_comment(comment):
    return translator.detect(comment).lang


def translate_comment(comment, dest):
    return translator.translate(comment, dest=dest).text

#listed below are some alternatives if the translation does not work
#-----------------------------------------------------------

# from googletrans import Translator, LANGUAGES
# from translate import Translator
# from google_trans_new import google_translator


# #
# # languages = LANGUAGES


# def detect_comment(comment):
#     translator = Translator()
#     return translator.detect(comment).lang


# # def translate_comment(comment, dest):
# #     return translator.translate(comment, dest=dest).text


# # def translate_comment(comment, dest):
# #     translator = Translator(to_lang=dest)
# #     translation = translator.translate(comment)
# #     return translation

# def translate_comment(comment, dest):
#     translator = google_translator()
#     translate_text = translator.translate(comment,lang_tgt=dest)
#     return translate_text