from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = "__all__"


class SortForm(forms.Form):
    CHOICES = forms.CharField(widget=forms.RadioSelect(choices=[('date', 'Date'), ('priority', 'Priority'), ('status', 'Status')]))