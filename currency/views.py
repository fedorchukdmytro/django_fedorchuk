from django.contrib.admin.decorators import register
from requests.models import HTTPBasicAuth
from currency.models import Exchange
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .choices import CURRENCIES
# Create your views here.

def currency_exchange_rate(request):
    breakpoint()
    exchange_response = requests.get('http://api.monobank.ua/bank/currency')
    exchange_result = exchange_response.json()
    print(exchange_result) 
    
    if any(type(rate) == str for rate in exchange_result):
         print('ОПЯТЬ ХУЙНЯ')
               
    else:
          new_result = []
          for rate in exchange_result:
               if rate['currencyCodeA'] == 840 and rate['currencyCodeB'] == 980:
                    rate['currencyCodeA'] = 'USD'
                    new_result.append(rate)
               elif rate['currencyCodeA'] == 978 and rate['currencyCodeB'] == 980:
                    rate['currencyCodeA'] = 'EUR'
                    new_result.append(rate)
               elif rate['currencyCodeA'] == 643 and rate['currencyCodeB'] == 980:
                    rate['currencyCodeA'] = 'RUR'
                    new_result.append(rate)   
          for rate in new_result:
               if rate.get('currencyCodeA') not in [currency[0] for currency in CURRENCIES]:
                 continue
               exchange = Exchange(
                   currency = rate.get('currencyCodeA'),
                   buy_price = rate.get('rateBuy'),
                   bank = 'MONO',
                   sale_price = rate.get('rateSell') 
                   )
               exchange.save()
    return HttpResponse(exchange_result)