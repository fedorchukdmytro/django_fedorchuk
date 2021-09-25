from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import Exchange


def list_exchange(request):
    listall = Exchange.objects.all()
    context = {'list': listall}
    return render(request, 'exchange.html', context)
