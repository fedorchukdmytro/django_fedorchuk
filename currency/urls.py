

from django.urls import path

from .views import CurrencyListView


urlpatterns = [
    path('currency', CurrencyListView.as_view(), name='exchange')
]
