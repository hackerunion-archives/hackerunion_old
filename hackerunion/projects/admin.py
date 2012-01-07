from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    filter_horizontal = ['tags']
    list_display = ['title', 'creator', 'created_on', 'is_active']
    list_filter = ['is_active']
    ordering = ['title']
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['title']


admin.site.register(Project, ProjectAdmin)
