
from django.urls import path

from  .views import *


urlpatterns = [
    
    path('edit-group/<int:group_id>', edit_group, name='edit-group'),
    path('create-group/', create_group, name='create-group'),
    path('list-groups/', list_groups, name='list-groups'),
    path('delete-group/<int:group_id>', delete_group, name='delete-group'),
    
]