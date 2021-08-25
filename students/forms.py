import re


from django import forms
from django.forms.fields import CharField

from .models import Student


class StudentFormFromModel(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'phone']

    def clean(self):
        cleaned_data = super().clean()
        t = cleaned_data.get('phone')
        if re.search('[a-zA-Z]+', t) is not None:
            raise forms.ValidationError('Please remove letter from phone number.')

class ContactUS(forms.Form): 
    title = forms.CharField(label="Тема Вашего обращения", required=True)
    message = forms.CharField(label="Ваше сообщение", required=True)
    email_from = forms.EmailField(label="Введите Ваш адрес электронной почты")

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(500)
        ]
    )