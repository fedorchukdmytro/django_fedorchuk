from django.contrib import admin

from .models import Logger, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "age")
    list_filter = ("age", "last_name", "first_name")
    search_fields = ("last_name__startswith", )


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ("method", "execution_time", "path", "created")
    list_filter = ("method", )
