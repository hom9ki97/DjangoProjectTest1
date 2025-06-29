from .models import UserData
from django import forms


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['first_name', 'last_name', 'email', 'card_number']
