from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
import random
from faker import Faker
from django import forms
fake = Faker()


def list_students(request):
    student_list = Student.objects.all()
    output = [f" {student.id} {student.last_name} {student.first_name}, {student.age};<br/>" for student in student_list]
    return HttpResponse(output)


def generate_student(request):
    studentadd = Student.objects.create(first_name = fake.last_name(), last_name = fake.last_name(), age = random.randint(18,100))
    output = f"{studentadd.id} {studentadd.first_name} {studentadd.last_name} {studentadd.age}"
    return HttpResponse(output)

def generate_students(request):
    class CountForm(forms.Form):
        count = forms.IntegerField(min_value=1, max_value=100)
    form = CountForm(request.GET)
    if form.is_valid():
        count = form.cleaned_data['count']
        studentList = [
            Student.objects.create(first_name = fake.first_name(), last_name = fake.last_name(), age = random.randint(18,100))
                      for _ in range(count)]
        output = [
            f"{student.id} {student.first_name} {student.last_name} {student.age};<br/>" for student in studentList]
                         
    else:
        return HttpResponse(str(form.errors))            
    return HttpResponse(output)        
        
    
    
