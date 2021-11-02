
from django.urls import path

from users import views as user_views

# app_name = 'students'

urlpatterns = [
    path('registration/', user_views.registration, name='register'),
    
]
