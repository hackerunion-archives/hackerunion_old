from django.contrib import admin
from chapters.models import *

class ChapterAdmin(admin.ModelAdmin):
    list_display = ['subdomain', 'name']


admin.site.register(Chapter, ChapterAdmin)
