from django.urls import path

from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.index, name='finance'),
    path('create_transacrion/', views.create_transaction, name='create_transaction'),
    path('transaction/<int:pk>/', views.transaction_info, name='transaction'),
    path('transaction_change/<int:pk>/', views.transaction_change, name='transaction_change'),
    path('transaction_delete/<int:pk>/', views.transaction_delete, name='transaction_delete'),
    path('category/<int:id>/', views.category_info, name='category_info'),

]