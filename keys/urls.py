from django.urls import path


from . import views

app_name = 'keys'

urlpatterns = [
    path('', views.keys, name='keys'),
    path('add/', views.create_user, name='add_user'),
    path('create/<int:pk>', views.create_key, name='create_key'),
    path('info/<int:pk>', views.user_info, name='user_info'),
]