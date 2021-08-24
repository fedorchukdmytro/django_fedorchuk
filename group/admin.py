from django.contrib import admin

from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("descipline", "hours_to_take")
    list_filter = ("descipline", "hours_to_take")
    search_fields = ("descipline__startswith", )
