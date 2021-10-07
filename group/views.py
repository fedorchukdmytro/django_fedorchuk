from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import GroupFormFromModel
from .models import Group


class GroupView(ListView):
    model = Group
    template_name = 'list_groups.html'


class CreateGroupView(CreateView):
    template_name = 'create_group.html'
    form_class = GroupFormFromModel
    success_url = reverse_lazy('list-groups')
    success_message = 'Group was created'


class EditGroupView(UpdateView):
    model = Group
    success_url = reverse_lazy('list-groups')
    success_message = 'Group was updated'
    template_name = 'edit_group.html'
    form_class = GroupFormFromModel


class DeleteGroupView(DeleteView):
    model = Group
    template_name = 'group_confirm_delete.html'
    success_url = reverse_lazy('list-groups')
