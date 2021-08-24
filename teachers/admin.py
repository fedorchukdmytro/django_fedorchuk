from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "age")
    list_filter = ("age", "last_name", "first_name")
    search_fields = ("last_name__startswith", )
