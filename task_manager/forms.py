from django.forms import ModelForm, DecimalField
from django.forms.widgets import Select
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = {'title', 'description', 'is_completed'}
        labels = {'title': 'Название задачи', 'description':'Подробное описание задачи'}
