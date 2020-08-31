from django.shortcuts import render, HttpResponse, redirect

layout = """
    <h1>sitio web con Django</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">hola mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas">pagina de pruebas</a>
        </li>
        <li>
            <a href="/contacto">contacto</a>
        </li>
    </ul>
    <hr/>
"""
def index(request):
    html = """
        <h1>Inicio</h1>
    """
    return HttpResponse(layout + html)

def hola_mundo(request):
    html = """
        <h1>hola mundo</h1>
        <h3>soy Sebastian</h3>
    """
    return HttpResponse(layout + html)

def pagina(request, redirigir = 0):
    if redirigir == 1:
        return redirect("contacto", nombre = "Sebastian", apellido = "Vega")
    html = """
        <h1>Pagina de mi web</h1>
        <p>creado por Sebastian Vega</p>
    """
    return HttpResponse(layout + html)

def contacto(request, nombre = "", apellido = ""):
    html = f"<h2>contacto {nombre} {apellido}</h2>"
    return HttpResponse(layout + html)