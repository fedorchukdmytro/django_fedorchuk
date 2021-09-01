from django.db import models


from .choices import CURRENCIES

class Exchange(models.Model):
    created = models.DateTimeField(auto_now=True)
    currency = models.CharField(max_length=4,)
    bank = models.CharField(max_length=20, default = 'privatbank')
    sale_price = models.DecimalField(max_digits=10, decimal_places=5)
    buy_price = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return f"{self.created}, {self.currency}, {self.sale_price} {self.buy_price}"



# Create your models here.

