from django import forms
from .models import Contact 

class MyForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone','desc','date']
