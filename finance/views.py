from django.shortcuts import render, redirect

from django.db.models import Sum

from .models import Transaction, Category

from .forms import TransactionForm


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

def create_transaction(request):
    if request.method =='POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('finance:finance')
    else:
        form = TransactionForm()
    return render(request, 'create_transaction.html', {'form': form})
