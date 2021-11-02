from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .froms import TeacherFormFromModel
from .models import Teacher


class TeacherList(ListView):
    model = Teacher

    def get_queryset(self):
        filtered_techers = {key: value for key, value in self.request.GET.items()}
        query = Teacher.objects.filter(**filtered_techers)
        return query


class TeacherCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Teacher
    form_class = TeacherFormFromModel
    success_url = reverse_lazy('list-teachers')
    success_message = 'Teacher was created'
    template_name = 'teachers/create_teacher.html'


class EditTeacher(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherFormFromModel
    success_url = reverse_lazy('list-teachers')


class DeleteTeacher(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('list-teachers')
