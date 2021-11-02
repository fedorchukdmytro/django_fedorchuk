from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import GroupFormFromModel
from .models import Group


class GroupView(ListView):
    model = Group
    template_name = 'list_groups.html'


class CreateGroupView(LoginRequiredMixin, CreateView):
    template_name = 'create_group.html'
    form_class = GroupFormFromModel
    success_url = reverse_lazy('list-groups')
    success_message = 'Group was created'


class EditGroupView(LoginRequiredMixin, UpdateView):
    model = Group
    success_url = reverse_lazy('list-groups')
    success_message = 'Group was updated'
    template_name = 'edit_group.html'
    form_class = GroupFormFromModel


class DeleteGroupView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'group_confirm_delete.html'
    success_url = reverse_lazy('list-groups')
