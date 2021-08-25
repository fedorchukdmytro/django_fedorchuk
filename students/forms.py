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
    title = forms.CharField(max_lenth=100, required=True)
    message = forms.CharField(max_length=100, required=True)
    email_from = forms.EmailField(required=True)