from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Teacher


@receiver(pre_save, sender=Teacher)
def capitalize(instance, **kwargs):
    first_name = instance.first_name
    capFirst_name = first_name.capitalize()
    instance.first_name = capFirst_name
    last_name = instance.last_name
    capLast_name = last_name.capitalize()
    instance.last_name = capLast_name
