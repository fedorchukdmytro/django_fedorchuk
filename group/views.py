from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GroupFormFromModel
from .models import Group


def list_groups(request):
    groups_list = Group.objects.all()
    return render(request, 'list_groups.html', {'groups': groups_list})


def create_group(request):
    if request.method == 'POST':
        form = GroupFormFromModel(request.POST)
        if form.is_valid():
            Group.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-groups'))
    else:
        form = GroupFormFromModel
    return render(request, 'create_group.html', {'form': form})


def edit_group(request, group_id):
    if request.method == 'POST':
        form = GroupFormFromModel(request.POST)
        if form.is_valid():
            Group.objects.update_or_create(defaults=form.cleaned_data, id=group_id)
            return HttpResponseRedirect(reverse('list-groups'))
    else:
        group = Group.objects.filter(id=group_id).first()
        form = GroupFormFromModel(instance=group)

    return render(request, 'edit_group.html', {'form': form, 'group_id': group_id})


def delete_group(request, group_id):
    fuckofgroup = Group.objects.filter(id=group_id).first()
    fuckofgroup.delete()
    return HttpResponseRedirect(reverse('list-groups'))
