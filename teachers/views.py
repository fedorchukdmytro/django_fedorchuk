from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher
# Create your views here.


def list_teachers(request):
    teachers_list = Teacher.objects.all()
    output = [ f"{teacher.id}, {teacher.last_name} {teacher.first_name}, {teacher.age};<br/>" for teacher in teachers_list]
    return HttpResponse(output)