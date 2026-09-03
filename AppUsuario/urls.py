from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apuestas/', views.apuestas, name='apuestas'),
    path('billetera/', views.billetera, name='billetera'),
    path('eventos/', views.eventos, name='eventos'),
    path('login/', views.login, name='login'),
    path('movimientos/', views.movimientos, name='movimientos'),
    path('registro/', views.registro, name='registro'),
    path('saldo/', views.saldo, name='saldo'),
]