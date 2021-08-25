
from django.urls import path

from .views import (create_student,
                    delete_student,
                    edit_student,
                    generate,
                    generate_student,
                    generate_students,
                    index,
                    list_students)

urlpatterns = [
    path('', index, name='index'),
    path('list-students/', list_students, name='list-students'),
    path('edit-student/<int:student_id>', edit_student, name='edit-student'),
    path('generate-student/', generate_student),
    path('generate-students/', generate_students),
    path('create-student/', create_student, name='create-student'),
    path('delete-student<int:student_id>', delete_student, name='delete-student'),
    path('generate/', generate, name='generate')
]
