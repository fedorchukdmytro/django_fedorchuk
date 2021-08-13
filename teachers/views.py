from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .froms import TeacherFormFromModel
from .models import Teacher


def list_teachers(request):
    teachers_list = Teacher.objects.all()
    output = [
        f"{teacher.id}, {teacher.last_name} {teacher.first_name}, {teacher.age};<br/>" for teacher in teachers_list]
    return render(request, 'list_teachers.html', {'teachers': teachers_list})


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
            return redirect('list-teachers')
    else:
        form = TeacherFormFromModel
    return render(request, 'create_teacher.html', {'form': form})


def edit_teacher(request, teacher_id):
    if request.method == 'POST':
        form = TeacherFormFromModel(request.POST)
        if form.is_valid():
            Teacher.objects.update_or_create(defaults=form.cleaned_data, id=teacher_id)
            return HttpResponseRedirect(reverse('list-teachers'))
    else:
        student = Teacher.objects.filter(id=teacher_id).first()
        form = TeacherFormFromModel(instance=student)

    return render(request, 'edit_teacher.html', {'form': form, 'teacher_id': teacher_id})

def delete_teacher(request, teacher_id):
    teacher= Teacher.objects.filter(id=teacher_id)
    teacher.delete()
    return HttpResponseRedirect(reverse('list-teachers'))
  