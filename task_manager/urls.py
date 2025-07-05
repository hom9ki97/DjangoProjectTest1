from django.urls import path

from . import views

app_name = 'task_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('add_task/', views.add_and_save_task, name='task_create'),
    path('completed/<int:task_id>', views.completed_task, name='completed'),
    path('api/task/<int:task_id>/toggle/', views.completed_task_rest, name='api-toggle-task'),
    path('change/<int:task_id>/', views.change_task, name='task_change'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task')
]