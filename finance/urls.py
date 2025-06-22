from django.urls import path

from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.index, name='finance'),
    path('create_transacrion/', views.create_transaction, name='create_transaction'),

]