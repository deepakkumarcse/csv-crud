from django import forms
from .models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'nameId'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'id': 'emailId'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'id': 'phoneId'})
        }
