

from django.urls import path

from .views import list_exchange


urlpatterns = [
    path('currency', list_exchange, name='exchange')
]
