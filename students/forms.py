from django import forms

from .models import Student


class StudentForm(forms.Form):
    first_name = forms.CharField(label='Student\' firstname', required=True)
    last_name = forms.CharField(label='Student\'s lastname', required=True)
    age = forms.IntegerField(label='Student\'s age',)
