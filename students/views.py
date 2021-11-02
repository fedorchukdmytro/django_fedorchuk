from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, FormView, ListView, UpdateView
from django.views.generic.base import TemplateView, View

from faker import Faker

from .forms import ContactUS
from .forms import GenerateNow
from .forms import GenerateRandomUserForm
from .forms import StudentFormFromModel
from .models import Student
from .tasks import send_email_to, st_generate

f = Faker()


class HomeView(TemplateView):
    template_name = 'index.html'


class StudentListView(ListView):
    model = Student


class GenerateStudent(View):

    def get(self, request, *args, **kwargs):
        studentadd = Student._gen()
        messages.success(request, studentadd)
        return HttpResponseRedirect(reverse('list-students'))


class GenerateStudents(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        class CountForm(forms.Form):
            count = forms.IntegerField(min_value=1, max_value=100)
        form = CountForm(request.GET)
        if form.is_valid():
            count = form.cleaned_data['count']
            studentList = []
            for _ in range(count):
                studentList.append(Student._gen())
            output = [
                f"{student.id} {student.first_name} {student.last_name} {student.age};<br/>" for student in studentList]
        else:
            return HttpResponse(str(form.errors))
        return HttpResponse(output)


class GenerateNow(LoginRequiredMixin, FormView):
    template_name = 'students/generate_now.html'
    form_class = GenerateNow

    def form_valid(self, form):
        count = form.cleaned_data['count']
        for _ in range(count):
            Student._gen()
        return redirect('list-students')


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentFormFromModel
    success_url = reverse_lazy('list-students')
    success_message = 'Student has create'
    template_name = 'students/create_student.html'


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentFormFromModel
    success_url = reverse_lazy('list-students')
    template_name = 'students/edit_student.html'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('list-students')
    template_name = 'students/delete.html'


class GenerateWithCelery(LoginRequiredMixin, FormView):
    template_name = 'students/generate.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data['total']
        st_generate.delay(total)
        # messages.success(request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('list-students')


class ContactUs(LoginRequiredMixin, FormView):
   template_name = 'students/ContactUS.html'
   form_class = ContactUS

   def form_valid(self, form):
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        email_from = form.cleaned_data['email_from']
        send_email_to.delay(title, message, email_from)
        return HttpResponse('Mail Sent')


def check():
    pass


def handler404(request, exception):
    return render(request, 'not_found.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
