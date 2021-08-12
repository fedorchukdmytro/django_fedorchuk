"""django_fedorchuk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from group import views as gviews

from students import views as sviews

from teachers import views as tviews

urlpatterns = [
    path('list-students/', sviews.list_students),
    path('generate-student/', sviews.generate_student),
    path('generate-students/', sviews.generate_students),
    path('create-student', sviews.create_student),
    path('create-teacher/', tviews.create_teacher),
    path('create-group/', gviews.create_group),
    path('list-groups/', gviews.list_groups),
    path('list-teachers/', tviews.list_teachers),
    path('filter-teachers/', tviews.filter_teachers),
    path('admin/', admin.site.urls)
]
