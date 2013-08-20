__author__ = 'hongleviet'


from modeltranslation.translator import translator, TranslationOptions
from ignite.models import *

class CompanyTranslationOptions(TranslationOptions):
    fields = ('one_sentence_description','description','funding')

translator.register(Company, CompanyTranslationOptions)
