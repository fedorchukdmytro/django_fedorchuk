from django.shortcuts import render
from django.http import HttpResponse
from .models import Group
# Create your views here.


def list_groups(request):
    groups_list = Group.objects.all()
    output = [ f"{group.id}, {group.descipline} {group.hours_to_take};<br/>" for group in groups_list]
    return HttpResponse(output)