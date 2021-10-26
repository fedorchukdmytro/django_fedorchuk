from django.urls import path

from .views import (DeleteTeacher,
                    EditTeacher,
                    TeacherCreateView,
                    TeacherList,)


urlpatterns = [

    path('create-teacher/', TeacherCreateView.as_view(), name='create-teacher'),
    path('list-teachers/', TeacherList.as_view(), name='list-teachers'),
    path('edit-teacher/<int:pk>', EditTeacher.as_view(), name='edit-teacher'),
    path('delete-teacher/<int:pk>/', DeleteTeacher.as_view(), name='delete-teacher'),
]
