from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("descipline", "hours_to_take", 'link_to_curator', "link_to_headman",
                    'number_of_students_engaged', 'total_groups', 'total_groups_in_un')
    list_filter = ("descipline", "hours_to_take")
    search_fields = ("descipline__startswith", )
    list_display_links = ['link_to_curator', 'link_to_headman', "descipline", 'number_of_students_engaged']

    def link_to_headman(self, obj):
        if obj.headman is not None:
            link = reverse("admin:students_student_change", args=[obj.headman.id])
            return format_html(u'<a href="%s">%s<a/>' % (link, obj.headman.last_name))
        else:
            pass

    def link_to_curator(self, obj):
        if obj.curator is not None:
            link = reverse("admin:teachers_teacher_change", args=[obj.curator.id])
            return format_html(u'<a href="%s ">%s<a/>' % (link, obj.curator.last_name))
        else:
            pass
