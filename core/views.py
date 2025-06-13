from django.shortcuts import render

from .models import Apps

def index(request):
    data = Apps.objects.all()
    return render(request, 'home.html', {'data':data})
