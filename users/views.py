import socket

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from django.core.mail import BadHeaderError, send_mail
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .forms import MyUserCreateForm


class PassChangeView(PasswordChangeView):
    template_name = 'password/password_change_form.html'
    form = PasswordChangeForm


class PassChangeDone(PasswordChangeDoneView):
	template_name = 'password/password_change_done.html'


def registration(request):
    if request.method == "POST":
        form = MyUserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Your account, {username},has been created! You are now able to login')
            form.save()
            return redirect('login')
    else:
        form = MyUserCreateForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')


def password_reset_request(request):
	if request.method == "POST":
		if socket.gethostname().endswith(".local"):
			domain = '127.0.0.1:8000'
		else:
			domain = 'dfedorchuk.herokuapp.com'

		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email": user.email,
					'domain': domain,
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'fedorchuk.dmytro@ukr.net', [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect("/password_reset/done/")
			messages.error(request, 'An invalid email was entered')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form": password_reset_form})
