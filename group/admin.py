from django.contrib import admin

from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("descipline", "hours_to_take", "curator", "headman")
    list_filter = ("descipline", "hours_to_take")
    search_fields = ("descipline__startswith", )
    list_display_links = ["curator", "headman"]



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