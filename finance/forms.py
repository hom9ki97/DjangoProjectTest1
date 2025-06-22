from django.forms import ModelForm, DateInput

from .models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'amount', 'transaction_type', 'category', 'date']
        widgets = {
            'date': DateInput(
                attrs={
                    'type': 'date',  # Включает встроенный календарь
                    'class': 'form-control',  # Стили Bootstrap
                },
                format='%Y-%m-%d'  # Формат даты для HTML5
            ),
        }