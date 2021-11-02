from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('index')
    else:    
        form = UserCreationForm()
    return render(request, 'registration.html', {'form':form})


    