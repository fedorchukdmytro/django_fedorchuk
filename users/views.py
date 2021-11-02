from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import MyUserCreateForm

def registration(request):
    if request.method == "POST":
        form = MyUserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Your account has been created! You are now able to login')
            form.save()
            return redirect('login')
    else:    
        form = MyUserCreateForm()
    return render(request, 'registration.html', {'form':form})


    