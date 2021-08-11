import random

from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from faker import Faker

from .forms import StudentForm
from .models import Student


f = Faker()


def list_students(request):
    student_list = Student.objects.all()
    output = [f" {student.id} {student.last_name} {student.first_name},{student.age};<br/>" for student in student_list]
    return HttpResponse(output)


def generate_student(request):
    studentadd = Student.objects.create(first_name=f.last_name(), last_name=f.last_name(), age=random.randint(18, 100))
    output = f"{studentadd.id} {studentadd.first_name} {studentadd.last_name} {studentadd.age}"
    return HttpResponse(output)


def generate_students(request):
    class CountForm(forms.Form):
        count = forms.IntegerField(min_value=1, max_value=100)
    form = CountForm(request.GET)
    if form.is_valid():
        count = form.cleaned_data['count']
        studentList = [
            Student.objects.create(first_name=f.first_name(), last_name=f.last_name(), age=random.randint(18, 100))
            for _ in range(count)]
        output = [
            f"{student.id} {student.first_name} {student.last_name} {student.age};<br/>" for student in studentList]
    else:
        return HttpResponse(str(form.errors))
    return HttpResponse(output)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponse('Student created!')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})
