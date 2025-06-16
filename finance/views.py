from django.shortcuts import render
from unicodedata import category
from django.db.models import Sum

from .models import Transaction, Category


def index(request):
    pos_amount = Transaction.objects.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    neg_amount = Transaction.objects.filter(transaction_type='outcome').aggregate(Sum('amount'))['amount__sum'] or 0
    total = pos_amount - neg_amount
    categories = Category.objects.all()
    transactions = Transaction.objects.all()
    print(pos_amount, neg_amount, categories)
    context = {
        'pos_amount': pos_amount,
        'neg_amount': neg_amount,
        'total': total,
        'categories': categories,
        'transactions': transactions

    }
    return render(request, 'finance.html', context)
