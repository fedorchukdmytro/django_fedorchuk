from django.contrib.auth import views as auth_views
from django.urls import path

from users import views as user_views
from users.views import PassChangeDone, PassChangeView, password_reset_request


# app_name = 'students'

urlpatterns = [
    path('registration/', user_views.registration, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_change', PassChangeView.as_view(), name='password_change'),
    path('password_change_done', PassChangeDone.as_view(), name='password_change_done'),
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),












]
