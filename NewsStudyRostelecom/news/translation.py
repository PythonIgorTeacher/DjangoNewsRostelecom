from modeltranslation.translator import register, TranslationOptions

from .models import *
@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('title','status')