from django.http import HttpResponse
from django.shortcuts import render

from .froms import TeacherFormFromModel
from .models import Teacher


def list_teachers(request):
    teachers_list = Teacher.objects.all()
    output = [
        f"{teacher.id}, {teacher.last_name} {teacher.first_name}, {teacher.age};<br/>" for teacher in teachers_list]
    return HttpResponse(output)


def filter_teachers(request):
    filtered_techers = {key: value for key, value in request.GET.items()}
    query = Teacher.objects.filter(**filtered_techers).values('last_name', 'first_name', 'age')
    output = [f'{t}<br/>' for t in query]
    if len(output) == 0:
        return HttpResponse('No such teacher')
    else:
        return HttpResponse(output)


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherFormFromModel(request.POST)
        if form.is_valid():
            Teacher.objects.create(**form.cleaned_data)
            return HttpResponse('Teacher created!')
    else:
        form = TeacherFormFromModel
    return render(request, 'create_teacher.html', {'form': form})
