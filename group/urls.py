
from django.urls import path

from .views import (CreateGroupView, DeleteGroupView, EditGroupView, GroupView)

urlpatterns = [

    path('edit-group/<int:pk>', EditGroupView.as_view(), name='edit-group'),
    path('create-group/', CreateGroupView.as_view(), name='create-group'),
    path('group/list/', GroupView.as_view(), name='list-groups'),
    path('delete-group/<int:pk>', DeleteGroupView.as_view(), name='delete-group')
]
