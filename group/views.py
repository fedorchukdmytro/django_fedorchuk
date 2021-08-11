from django.http import HttpResponse
from django.shortcuts import render

from .forms import GroupFormFromModel
from .models import Group


def list_groups(request):
    groups_list = Group.objects.all()
    output = [f"{group.id}, {group.descipline} {group.hours_to_take};<br/>" for group in groups_list]
    return HttpResponse(output)


def create_group(request):
    if request.method == 'POST':
        form = GroupFormFromModel(request.POST)
        if form.is_valid():
            Group.objects.create(**form.cleaned_data)
            return HttpResponse('Group created!')
    else:
        form = GroupFormFromModel
    return render(request, 'create_group.html', {'form': form})
