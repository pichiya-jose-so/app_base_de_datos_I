from django.shortcuts import render

# Create your views here.

# llama al index (inicio de la pagina web)
def index(request):
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