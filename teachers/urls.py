from django.urls import path

from .views import (create_teacher,
                    delete_teacher,
                    edit_teacher,
                    filter_teachers,
                    list_teachers)

urlpatterns = [

    path('create-teacher/', create_teacher, name='create-teacher'),
    path('list-teachers/', list_teachers, name='list-teachers'),
    path('filter-teachers/', filter_teachers),
    path('edit-teacher/<int:teacher_id>', edit_teacher, name='edit-teacher'),
    path('delete-teacher/<int:teacher_id>', delete_teacher, name='delete-teacher'),
]
