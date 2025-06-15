from django.shortcuts import render
# from ..decorators.logging import log_request
from .decorators.logging import log_request

from .models import Apps

@log_request
def index(request):
    data = Apps.objects.all()
    return render(request, 'home.html', {'data':data})
