from django import forms
from .models import MRSystem


class MRSForm(forms.ModelForm):
    class Meta:
        model = MRSystem
        fields = "__all__"
