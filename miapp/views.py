from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("""
        <h1>Inicio</h1>
    """)

def hola_mundo(request):
    return HttpResponse("""
        <h1>hola mundo</h1>
        <h3>soy Sebastian</h3>
    """)

def pagina(request):
    return HttpResponse("""
        <h1>Pagina de mi web</h1>
        <p>creado por Sebastian Vega</p>
    """)