from django.contrib.admin.decorators import register
from requests.models import HTTPBasicAuth
from currency.models import Exchange
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .choices import CURRENCIES
# Create your views here.

def currency_exchange_rate(request):
    
#     exchange_response = requests.get(' http://api.monobank.ua/bank/currency')
#     exchange_result = exchange_response.json()
     
    
#     if any(type(rate) == str for rate in exchange_result):
#         print('ОПЯТЬ ХУЙНЯ')
               
#     else:
#         for rate in exchange_result:
#             if rate['currencyCodeA'] == 840:
#                     rate['currencyCodeA'] = 'USD'
#             elif rate['currencyCodeA'] == 978:
#                     rate['currencyCodeA'] = 'EUR'
#             elif rate['currencyCodeA'] == 643:
#                     rate['currencyCodeA'] = 'RUR'

#         # new_result = exchange_result    
#         for rate in exchange_result:
#             if rate.get('currencyCodeA') not in [currency[0] for currency in CURRENCIES]:
#                 continue
#             exchange = Exchange(
#                 currency = rate.get('currencyCodeA'),
#                 buy_price = rate.get('rateBuy'),
#                 bank = 'MONO',
#                 sale_price = rate.get('rateSell') 
#             )
#             exchange.save()

#     return HttpResponse (exchange_result)

# def get_currency_national(request):    
    exchange_response = requests.get('https://bank.gov.ua/NBU_Exchange/exchange?json')
    exchange_result = exchange_response.json()
     
    
    if any(type(rate) == str for rate in exchange_result):
         print('ОПЯТЬ ХУЙНЯ')
               
    else:
          new_result = []
          for rate in exchange_result:
                print(rate)       
        # if rate['r030'] == 840:
        #             print(rate['r030'])
        #             rate["r030"] = 'USD'
        #             new_result.append(rate)
        #        elif rate["r030"] == 978 :
        #             rate["r030"] = 'EUR'
        #             new_result.append(rate)
        #        elif rate["r030"] == 643:
        #             rate["r030"] = 'RUR'
        #             new_result.append(rate)
        # # new_result = exchange_result    
        #   for rate in new_result:
        #        if rate.get("r030") not in [currency[0] for currency in CURRENCIES]:
        #          continue
        #        exchange = Exchange(
        #            currency = rate.get("r030"),
        #            buy_price = rate.get("rate"),
        #            bank = 'NATIONAL',
        #            sale_price = rate.get("rate") 
        #            )
            #    exchange.save()
    return HttpResponse(exchange_result)