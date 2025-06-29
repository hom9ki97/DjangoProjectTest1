from django.shortcuts import render, redirect, get_object_or_404

from .models import UserData, UserKeys
from .forms import UserDataForm
from .crypto import generate_keys


def keys(request):
    user_data = UserData.objects.all()
    return render(request, 'keys_list.html', {'user_data': user_data})


def create_user(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('keys:keys')
    else:
        form = UserDataForm()
        return render(request, 'key_create.html', {'form': form})


def create_key(request, pk):
    user_data = UserData.objects.get(pk=pk)
    data = {'name': user_data.first_name,
            'surname': user_data.last_name,
            'email': user_data.email,
            'card_number': user_data.card_number,
            'date': user_data.created_at}

    public_key, private_key = generate_keys(data)

    UserKeys.objects.create(
        user=user_data,
        public_key=public_key,
        private_key=private_key
    )
    return redirect('keys:keys')


def user_info(request, pk):
    user_data = get_object_or_404(UserData, pk=pk)
    return render(request, 'key_info.html', {'user_data': user_data})
