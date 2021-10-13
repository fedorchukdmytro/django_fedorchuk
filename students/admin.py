from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Logger, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "age", 'link_to_group', 'phone', 'submissive_group',
                    'status', 'total_students_in_his_group')
    list_filter = ('status',)
    search_fields = ("last_name__startswith", )
    list_display_links = ["last_name", "first_name", 'link_to_group', ]
    # list_editable = ['age']

    def link_to_group(self, obj):
        if obj.group is not None:
            link = reverse("admin:group_group_change", args=[obj.group.id])
            return format_html(u'<a href="%s">%s<a/>' % (link, obj.group.descipline))
        else:
            pass
    link_to_group.short_description = 'СОСТОИТ В ГРУППЕЕЕ'


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ("method", "execution_time", "path", "created")
    list_filter = ("method", )
