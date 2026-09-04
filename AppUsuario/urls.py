from django.urls import path
from . import views

# Hola


# ------------------------------------------------------------------------------------------------------
# NOTA DE JULIO
# Estos don todos los path de la aplicacion, para el uso de los path se pueden crear un path para cada
# vista que se necesite en la aplicacion. Si se elimina un path aqui, no se podra acceder a la vista
# correspondiente desde el navegador.
# ------------------------------------------------------------------------------------------------------


urlpatterns = [
    path('', views.index, name='index'),
    path('apuestas/', views.apuestas, name='apuestas'), # ejemplo en el navegador de manera local: http://127.0.0.1:8000/apuestas/
    path('billetera/', views.billetera, name='billetera'),
    path('eventos/', views.eventos, name='eventos'),
    path('login/', views.login, name='login'),
    path('movimientos/', views.movimientos, name='movimientos'),
    path('registro/', views.registro, name='registro'),
    path('saldo/', views.saldo, name='saldo'),
]