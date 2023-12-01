from django.contrib import admin
from django.db.models.functions import Length
from django.db.models import Count

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-date','title','author']
    list_display = ['title','author','date','symbols_count']
    list_filter = ['title','author','date']
    list_display_links = ('date',)
    # list_editable = ['author']
    # readonly_fields = ['author','title']
    prepopulated_fields = {"slug":("title",)}
    list_per_page = 5
    @admin.display(description='Длина', ordering='_symbols')
    def symbols_count(self, article:Article):
        return f"Символы: {len(article.text)}"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_symbols=Length('text'))
        return queryset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title','status','tag_count']
    list_filter = ['title','status']

    @admin.display(description='Использований:', ordering='tag_count')
    def tag_count(self, object):
        return object.tag_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(tag_count=Count('article'))
        return queryset
# admin.site.register(Tag,TagAdmin)
admin.site.register(Article,ArticleAdmin)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','article','image_tag']
