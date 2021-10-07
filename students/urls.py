
from django.urls import path

from .views import (ContactUs, GenerateNow,
                    GenerateStudent,
                    GenerateStudents,
                    GenerateWithCelery,
                    HomeView,
                    StudentCreateView,
                    StudentDeleteView,
                    StudentListView,
                    UpdateStudentView,
                    check)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('list-students/', StudentListView.as_view(), name='list-students'),
    path('edit-student/<int:pk>', UpdateStudentView.as_view(), name='edit-student'),
    path('generate-student/', GenerateStudent.as_view(), name='generate-student'),
    path('generate-students/', GenerateStudents.as_view(), name='generate-students'),
    path('create-student/', StudentCreateView.as_view(), name='create-student'),
    path('delete-student/<int:pk>', StudentDeleteView.as_view(), name='delete-student'),
    path('generate/', GenerateWithCelery.as_view(), name='generate'),
    path('generate-now/', GenerateNow.as_view(), name='generate-now'),
    path('contactus/', ContactUs.as_view(), name='contactus'),
    path('check/', check, name='check')
]
