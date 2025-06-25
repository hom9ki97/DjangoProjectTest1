from django.shortcuts import render, redirect, get_list_or_404

from django.db.models import Sum

from .models import Transaction, Category

from .forms import TransactionForm


def index(request):
    pos_amount = round(
        Transaction.objects.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0, 2)
    neg_amount = round(
        Transaction.objects.filter(transaction_type='outcome').aggregate(Sum('amount'))['amount__sum'] or 0, 2)
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


def transaction_info(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    return render(request, 'transaction_info.html', {'transaction': transaction})


def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:finance')
        print(form.errors)

    else:
        form = TransactionForm()
    return render(request, 'create_transaction.html', {'form': form})


def transaction_change(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('finance:finance')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'create_transaction.html', {'form': form})


def transaction_delete(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('finance:finance')

    else:
        return render(request, 'transaction_info.html', {'transaction': transaction})

def category_info(request, id):
    transactions = Transaction.objects.filter(category_id=id, transaction_type='outcome').select_related('category')
    total = round(transactions.aggregate(Sum('amount'))['amount__sum'] or 0, 2)
    if transactions:
        return render(request, 'category_info.html', {'transactions': transactions, 'total': total})
    else:
        return redirect('finance:finance')
