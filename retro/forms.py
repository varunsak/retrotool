from django import forms
from django.contrib.admin import widgets

from .models import Retro


class RetroCreateForm(forms.ModelForm):
    class Meta:
        model = Retro
        fields = ['project', 'team', 'sprint', 'description', 'action_item', 'owner', 'status', 'eta']
