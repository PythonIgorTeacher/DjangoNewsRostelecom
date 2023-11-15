from django.contrib import admin
from .models import Demo

class DemoAdmin(admin.ModelAdmin):
    list_display = ['title','image','image_tag']


admin.site.register(Demo,DemoAdmin)

