
from django import forms

from group.models import Group


class GroupFormFromModel(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['descipline', 'hours_to_take', 'headman', 'curator']
