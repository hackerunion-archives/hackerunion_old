from django.contrib import admin
from people.models import *


class HackerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'preferred_contact_email', 'chapter']
    list_filter = ['chapter']
    ordering = ['user']


admin.site.register(HackerProfile, HackerProfileAdmin)
