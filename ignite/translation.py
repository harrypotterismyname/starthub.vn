__author__ = 'hongleviet'


from modeltranslation.translator import translator, TranslationOptions
from ignite.models import *

class CompanyTranslationOptions(TranslationOptions):
    fields = ('one_sentence_description','description','funding')

class Meta_infoTranslationOptions(TranslationOptions):
    fields = ('content',)


translator.register(Company, CompanyTranslationOptions)
translator.register( Meta_info, Meta_infoTranslationOptions)
