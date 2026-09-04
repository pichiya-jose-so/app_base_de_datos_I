from django.shortcuts import render

# ------------------------------------------------------------------------------------------------------
# NOTA DE JULIO
# Desde aqui se renderizan las vistas de la aplicacion (aqui se puede hacer uso de las apis),
# para el uso de las vistas se pueden crear vistas para cada path y se llaman desde urls.py
# Si un archivo html no se encuentra en la carpeta templates, no se podra renderizar la vista correspondiente desde el navegador.
# Si un archivo no está renderizado en la vista correspondiente, no se podra crear el path correspondiente en urls.py y no se podra acceder a la vista desde el navegador.
# ------------------------------------------------------------------------------------------------------

# llama al index (inicio de la pagina web)
def index(request):
    #Se define la funcion index que recibe un objeto request como parametro y retorna la vista HIndex.html
    return render(request, 'HIndex.html')

def apuestas(request):
    return render(request, 'HApuestas.html')

def billetera(request):
    return render(request, 'HBilletera.html')

def eventos(request):
    return render(request, 'HEventos.html')

def login(request):
    return render(request, 'HLogin.html')

def movimientos(request):
    return render(request, 'HMovimientos.html')

def registro(request):
    return render(request, 'HRegistro.html')

def saldo (request):
    return render(request, 'HSaldo.html')
#y el primo 