from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from .forms import TaskForm

from .models import Task


# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     context_object_name = 'tasks'
#
#     def get_queryset(self):
#         return Task.objects.all()


def index(request):
    completed_task = Task.objects.filter(is_completed=True)
    active_task = Task.objects.filter(is_completed=False)

    context = {'completed_tasks': completed_task,
               'active_task': active_task}

    return render(request, 'index.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'detail.html', {'task': task})


def add_and_save_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_manager:index')
        else:
            context = {'form': form}
            return render(request, 'task_create.html', context)
    else:
        form = TaskForm()
        context = {'form': form}
        return render(request, 'task_create.html', context)


def change_task(request, task_id):
    task_form = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task_form)
        if form.is_valid():
            form.save()
            return redirect('task_manager:index')
        else:
            context = {'form': form}
            return render(request, 'task_create.html', context)
    else:
        form = TaskForm(instance=task_form)
        context = {'form': form}
        return render(request, 'task_create.html', context)


def completed_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.is_completed:
        task.mark_as_incomplete()
    else:
        task.mark_as_completed()
    return redirect('task_manager:index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_manager:index')
