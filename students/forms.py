import re

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms.fields import CharField

from .models import Student


class StudentFormFromModel(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'phone']

    def clean(self):
        # breakpoint()
        cleaned_data = super().clean()
        # cleaned_data = forms.Field.clean(self)
        t = cleaned_data.get('phone')
        if t.isdigit() is not True:
            raise forms.ValidationError('В номере должны быть только цифры.')
        elif len(t) < 12:
            raise forms.ValidationError('В номере должно быть от 12 до 15 цифр включительно .')
        elif len(t) > 15:
            raise forms.ValidationError('В номере должно быть от 12 до 15 цифр включительно.')


class ContactUS(forms.Form):
    title = forms.CharField(label="Тема Вашего обращения", required=True)
    message = forms.CharField(label="Ваше сообщение", required=True)
    email_from = forms.EmailField(label="Введите Ваш адрес электронной почты")


class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(500)
        ]
    )


class GenerateNow(forms.Form):
    count = forms.IntegerField(
        label='введитк число сколько сейчас сгенерить', min_value=5, max_value=10)
