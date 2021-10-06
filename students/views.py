import random
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, FormView
from django import forms
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse , reverse_lazy
from django.views.generic.base import View

from faker import Faker

from .forms import ContactUS
from .forms import GenerateNow
from .forms import GenerateRandomUserForm
from .forms import StudentFormFromModel
from .models import Student
from .tasks import send_email_to, st_generate

f = Faker()


def index(request):
    return render(request, 'index.html')


# def list_students(request):
#     student_list = Student.objects.all()
#     p = Paginator(student_list, 20)
#     page_num = request.GET.get('page', 1)
#     page = p.page(page_num)
#     context = {'students': page}
#     return render(request, 'list_students.html', context)

from django.utils import timezone
from django.views.generic.list import ListView

class StudentListView(ListView):
    model = Student
    # paginate_by = 10  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

# def generate_student(request):
#     # breakpoint()
#     studentadd = Student._gen()
#     output = f"{studentadd.id} {studentadd.first_name} {studentadd.last_name} {studentadd.age}"
#     return HttpResponse(output)



class GenerateStudent(View):
    
    def get(self,request, *args, **kwargs):
        studentadd = Student._gen()
        messages.success(request, studentadd)
        return HttpResponseRedirect(reverse('list-students'))
    

class GenerateStudents(View):
    def get(self,request, *args, **kwargs):
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


# def generate_now(request):
#     if request.method == 'POST':
#         # breakpoint()
#         form = GenerateNow(request.POST)
#         if form.is_valid():
#             count = form.cleaned_data['count']
#             studentList = []
#             for _ in range(count):
#                 studentList.append(Student(first_name=f.first_name(), last_name=f.last_name(), age=random.randint(18, 100)))
#                 Student.objects.bulk_create(studentList)

#             return redirect('list-students')
#     else:
#         form = GenerateNow()
#     return render(request, 'generate_now.html', {'form': form})

class GenerateNow(FormView):
    template_name = 'students/generate_now.html'
    form_class = GenerateNow

    def form_valid(self, form):
        count = form.cleaned_data['count']
        student_list = []
        for _ in range(count):
            Student._gen()
        return redirect('list-students')





# def create_student(request):
#     if request.method == 'POST':
#         form = StudentFormFromModel(request.POST)
#         if form.is_valid():
#             student = Student.objects.create(**form.cleaned_data)
#             messages.success(request, 'One student created successfuly  {}'.format(student))
#             return redirect('list-students')
#     else:
#         form = StudentFormFromModel()
#     return render(request, 'create_student.html', {'form': form})


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentFormFromModel
    success_url = reverse_lazy('list-students')
    success_message = 'Student has create'
    template_name = 'students/create_student.html'


# def edit_student(request, student_id):
#     if request.method == 'POST':
#         form = StudentFormFromModel(request.POST)
#         if form.is_valid():
#             Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
#             return HttpResponseRedirect(reverse('list-students'))
#     else:
#         student = Student.objects.filter(id=student_id).first()
#         form = StudentFormFromModel(instance=student)

#     return render(request, 'edit_student.html', {'form': form, 'student_id': student_id})

class UpdateStudentView(UpdateView):
    model = Student
    form_class = StudentFormFromModel
    success_url = reverse_lazy('list-students')
    template_name = 'students/edit_student.html'


# class EditStudentView(UpdateView):
#     model = Student
#     fields = ['first_name', 'last_name', 'age', 'phone']
#     template_name = 'students/student_edit.html'

#     def get_success_url(self, *kwargs):
#         return reverse('list-students')




# def delete_student(request, student_id):
#     badstudent = Student.objects.filter(id=student_id)
#     badstudent.delete()
#     return HttpResponseRedirect(reverse('list-students'))



class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('list-students')
    template_name = 'students/delete.html'

    



# def generate(request):
#     if request.method == 'POST':
#         form = GenerateRandomUserForm(request.POST)
#         if form.is_valid():
#             total = form.cleaned_data['total']
#             st_generate.delay(total)
#             messages.success(request, 'We are generating your random users! Wait a moment and refresh this page.')
#             return redirect('list-students')
#     else:
#         form = GenerateRandomUserForm()
#         return render(request, 'generate.html', {'form': form})

class GenerateWithCelery(FormView):
    template_name = 'students/generate.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data['total']
        st_generate.delay(total)
        # messages.success(request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('list-students')


class ContactUs(FormView):
   template_name = 'students/ContactUS.html'
   form_class = ContactUS

   def form_valid(self, form):
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        email_from = form.cleaned_data['email_from']
        send_email_to.delay(title, message, email_from)
        return HttpResponse('Mail Sent')

   
   
   
   
    # if request.method == 'POST':
    #     form = ContactUS(request.POST)
    #     if form.is_valid():
    #         title = form.cleaned_data['title']
    #         message = form.cleaned_data['message']
    #         email_from = form.cleaned_data['email_from']
    #         send_email_to.delay(title, message, email_from)
    #     return HttpResponse('Mail Sent')

    # else:
    #     form = ContactUS()
    # return render(request, 'ContactUS.html', {'form': form})

def check():
    pass

def handler404(request, exception):
    return render(request, 'not_found.html', status=404)



def handler500(request):
    return render(request, '500.html', status=500)