from django.contrib import admin
from django.urls import reverse 
from .models import Group
from django.utils.html import format_html

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("descipline", "hours_to_take", 'link_to_curator', "link_to_headman")
    list_filter = ("descipline", "hours_to_take")
    search_fields = ("descipline__startswith", )
    list_display_links = ['link_to_curator', 'link_to_headman', "descipline" ]

    def link_to_headman(self, obj):
        if obj.headman != None:
            link = reverse("admin:students_student_change", args=[obj.headman.id])
            return format_html(u'<a href="%s">%s<a/>' % (link,obj.headman.last_name))
        else:
            pass
    def link_to_curator(self, obj):
        if obj.curator != None:
            link = reverse("admin:teachers_teacher_change", args=[obj.curator.id])
            return format_html(u'<a href="%s ">%s<a/>' % (link,obj.curator.last_name))
        else:
            pass

    
# class YourModelAdmin(model.modelAdmin):
#     list_display = ["field_one", "field_two", "related"]
#     list_display_links = ["field_one", "related"]
# # model B(models.Model):
#     name = models.CharField(max_length=20)

# model A(models.Model):
#     field1 = models.CharField(max_length=20)
#     Bkey = models.ForeignKey(B)

#     def link_to_headman(self, obj):
#         link = urlresolvers.reverse("admin:")


# # class AAdmin(admin.ModelAdmin):
# #     list_display = ["field1","link_to_B"]
#     def link_to_B(self, obj):
#         link=urlresolvers.reverse("admin:yourapp_b_change", args=[obj.B.id]) #model name has to be lowercase
#         return u'<a href="%s">%s</a>' % (link,obj.B.name)
#     link_to_B.allow_tags=True