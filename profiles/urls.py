from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>/', views.order_history, name='order_history'),
    path('delete/', views.delete_profile, name='delete_profile'),
    path('delete/confirm/', views.confirm_delete_profile, name='confirm_delete_profile'),
]
