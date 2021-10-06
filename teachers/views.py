from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, FormView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from .froms import TeacherFormFromModel
from .models import Teacher


# def list_teachers(request):
#     teachers_list = Teacher.objects.all()
#     p = Paginator(teachers_list, 20)
#     page_num = request.GET.get('page', 1)
#     page = p.page(page_num)
#     context = {'teachers': page}
#     return render(request, 'list_teachers.html', context)

class TeacherList(ListView):
    model = Teacher

    def get_queryset(self):
        args = self.request.GET
        dict_param = {}
        for key, value in args.items():
            dict_param[key] = value

        queryset = Teacher.objects.filter(**dict_param)
        return queryset



# class FilteredTeacherView(View):    
#     def get(self, request, *args, **kwargs):
#         filtered_techers = {key: value for key, value in request.GET.items()}
#         query = Teacher.objects.filter(**filtered_techers).values('last_name', 'first_name', 'age')
#         output = [f'{t}<br/>' for t in query]
#         if len(output) == 0:
#             return HttpResponse('No such teacher')
#         else:
#             return output


# def create_teacher(request):
#     if request.method == 'POST':
#         form = TeacherFormFromModel(request.POST)
#         if form.is_valid():
#             Teacher.objects.create(**form.cleaned_data)
#             return redirect('list-teachers')
#     else:
#         form = TeacherFormFromModel
#     return render(request, 'create_teacher.html', {'form': form})


class TeacherCreateView(SuccessMessageMixin, CreateView):
    model = Teacher
    form_class = TeacherFormFromModel
    success_url = reverse_lazy('list-teachers')
    success_message = 'Teacher was created'
    template_name = 'teachers/create_teacher.html'



class EditTeacher(UpdateView):
    model  = Teacher
    form_class = TeacherFormFromModel
    success_url = reverse_lazy('list-teachers')
    # def form_valid(self, form):
    #     Teacher.objects.update_or_create(defaults=form.cleaned_data, id=teacher_id)
    #     return HttpResponseRedirect(reverse('list-teachers'))
        



# def edit_teacher(request, teacher_id):
    
    
#     if request.method == 'POST':
#         form = TeacherFormFromModel(request.POST)
#         if form.is_valid():
#             Teacher.objects.update_or_create(defaults=form.cleaned_data, id=teacher_id)
#             return HttpResponseRedirect(reverse('list-teachers'))
#     else:
#         student = Teacher.objects.filter(id=teacher_id).first()
#         form = TeacherFormFromModel(instance=student)

#     return render(request, 'edit_teacher.html', {'form': form, 'teacher_id': teacher_id})

class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('list-teachers')





# def delete_teacher(request, teacher_id):
#     teacher = Teacher.objects.filter(id=teacher_id)
#     teacher.delete()
#     return HttpResponseRedirect(reverse('list-teachers'))
