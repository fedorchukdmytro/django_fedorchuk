from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import GroupFormFromModel
from .models import Group


# def list_groups(request):
#     groups_list = Group.objects.all()
#     p = Paginator(groups_list, 20)
#     page_num = request.GET.get('page', 1)
#     page = p.page(page_num)
#     context = {'groups': page}
#     return render(request, 'list_groups.html', context)

class GroupView(ListView):
    model = Group
    template_name = 'list_groups.html'


# def create_group(request):
#     if request.method == 'POST':
#         form = GroupFormFromModel(request.POST)
#         if form.is_valid():
#             Group.objects.create(**form.cleaned_data)
#             return HttpResponseRedirect(reverse('list-groups'))
#     else:
#         form = GroupFormFromModel
#     return render(request, 'create_group.html', {'form': form})

class CreateGroupView(CreateView):
    template_name = 'create_group.html'
    form_class = GroupFormFromModel
    success_url = reverse_lazy ('list-groups')
    success_message = 'Group was created'


# def edit_group(request, group_id):
#     if request.method == 'POST':
#         form = GroupFormFromModel(request.POST)
#         if form.is_valid():
#             Group.objects.update_or_create(defaults=form.cleaned_data, id=group_id)
#             return HttpResponseRedirect(reverse('list-groups'))
#     else:
#         group = Group.objects.filter(id=group_id).first()
#         form = GroupFormFromModel(instance=group)

#     return render(request, 'edit_group.html', {'form': form, 'group_id': group_id})
class EditGroupView(UpdateView):
    model = Group
    success_url = reverse_lazy ('list-groups')
    success_message = 'Group was updated'
    template_name = 'edit_group.html'
    form_class = GroupFormFromModel


# def delete_group(request, group_id):
#     fuckofgroup = Group.objects.filter(id=group_id).first()
#     fuckofgroup.delete()
#     return HttpResponseRedirect(reverse('list-groups'))

class DeleteGroupView(DeleteView):
    model = Group
    template_name = 'group_confirm_delete.html'
    success_url = reverse_lazy ('list-groups')