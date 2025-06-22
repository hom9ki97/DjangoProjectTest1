from django.forms import ModelForm

from .models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'amount', 'transaction_type', 'category', 'date']