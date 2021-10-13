from django.contrib import admin

from .models import Exchange


@admin.register(Exchange)
class AdminExchange(admin.ModelAdmin):
    list_display = ('created', 'bank', 'currency', 'sale_price', 'buy_price')
