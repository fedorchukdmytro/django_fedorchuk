from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "age", 'submissive_group')
    list_filter = ("age", "last_name", "first_name")
    search_fields = ("last_name__startswith", )
    list_display_links = ['submissive_group',]
