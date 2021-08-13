
from django.urls import path

from .views import *

urlpatterns = [
    
    path('list-students/', list_students,name='list-students'),
    path('edit-student/<int:student_id>', edit_student, name='edit-student'),
    path('generate-student/', generate_student),
    path('generate-students/', generate_students),
    path('create-student/', create_student),
    path('delete-student<int:student_id>', delete_student, name='delete-student')
]