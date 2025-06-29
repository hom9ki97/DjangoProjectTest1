from django.forms import ModelForm, DateInput

from .models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'amount', 'transaction_type', 'category', 'date']
        widgets = {
            'date': DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                },
                format='%Y-%m-%d'
            ),
        }