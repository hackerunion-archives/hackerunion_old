from django.contrib import admin
from people.models import *


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'username_url']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['username', 'type', 'user']


class HackerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'preferred_contact_email']


admin.site.register(HackerProfile, HackerProfileAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Service, ServiceAdmin)
