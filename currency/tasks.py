from celery import shared_task

import requests 
from datetime import datetime, timedelta

from .models import Exchange
 
from .choices import CURRENCIES

@shared_task
def get_currency_rates():
     exchange_response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
     exchange_result = exchange_response.json()
     for rate in exchange_result:
          if rate.get('ccy') not in [currency[0] for currency in CURRENCIES]:
               continue
          exchange = Exchange(
               currency = rate.get('ccy'),
               buy_price = rate.get('buy'),
               sale_price = rate.get('sale') 
          )
          exchange.save()

@shared_task
def cur_nah():
    Exchange.objects.filter(created__lte=(datetime.now() - timedelta(seconds=10))).delete()

@shared_task
def get_currency_mono():    
     exchange_response = requests.get('http://api.monobank.ua/bank/currency')
     exchange_result = exchange_response.json()
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

@shared_task
def get_currency_national():    
     exchange_response = requests.get('https://bank.gov.ua/NBU_Exchange/exchange?json')
     exchange_result = exchange_response.json()
     for rate in exchange_result:
          if rate['CurrencyCodeL'] == 'RUB':
               rate["CurrencyCodeL"] = 'RUR' 
     for rate in exchange_result:
          if rate.get("CurrencyCodeL") not in [currency[0] for currency in CURRENCIES]:
               continue
          exchange = Exchange(
               currency = rate.get("CurrencyCodeL"),
               buy_price = rate.get("Amount"),
               bank = 'NATIONAL',
               sale_price = rate.get("Amount") 
               )
          exchange.save()


