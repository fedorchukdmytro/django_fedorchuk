import random

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from faker import Faker

from .forms import StudentFormFromModel
from .models import Student
from .forms import GenerateRandomUserForm
from .forms import ContactUS

from .tasks import st_generate
f = Faker()

def index(request):
    
    return render(request, 'index.html')


def list_students(request):
    student_list = Student.objects.all()
    return render(request, 'list_students.html', {'students': student_list})


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
        studentList = []
        for _ in range(count):
            studentList.append(Student(first_name=f.first_name(),
                                       last_name=f.last_name(),
                                       age=random.randint(18, 100)))
        Student.objects.bulk_create(studentList)
        output = [
            f"{student.id} {student.first_name} {student.last_name} {student.age};<br/>" for student in studentList]
    else:
        return HttpResponse(str(form.errors))
    return HttpResponse(output)


def create_student(request):
    if request.method == 'POST':
        form = StudentFormFromModel(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-students'))
    else:
        form = StudentFormFromModel()
    return render(request, 'create_student.html', {'form': form})


def edit_student(request, student_id):
    if request.method == 'POST':
        form = StudentFormFromModel(request.POST)
        if form.is_valid():
            Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
            return HttpResponseRedirect(reverse('list-students'))
    else:
        student = Student.objects.filter(id=student_id).first()
        form = StudentFormFromModel(instance=student)

    return render(request, 'edit_student.html', {'form': form, 'student_id': student_id})


def delete_student(request, student_id):
    badstudent = Student.objects.filter(id=student_id)
    badstudent.delete()
    return HttpResponseRedirect(reverse('list-students'))


def generate(request):
    if request.method == 'POST':
        form = GenerateRandomUserForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data.get('total')
            st_generate.delay(total)
            messages.success(request, 'We are generating your random users! Wait a moment and refresh this page.')
            return redirect('list-students')
    else:
        form = GenerateRandomUserForm()
    return render(request, 'generate.html', {'form': form})

def ContactUs(request):
    if request.method == 'POST':
        form = ContactUS(request.POST)
        # if form.is_valid():
        #     total = form.cleaned_data.get('total')
        #     st_generate.delay(total)
        #     messages.success(request, 'We are generating your random users! Wait a moment and refresh this page.')
        #     return redirect('list-students')
    else:
        form = ContactUS()
    return render(request, 'ContactUS.html', {'form': form})
    