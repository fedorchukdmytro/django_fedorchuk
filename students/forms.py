import re

from django import forms

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
