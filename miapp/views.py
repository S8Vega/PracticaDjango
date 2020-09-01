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
    return render(request, "index.html")

def hola_mundo(request):
    return render(request, "hola_mundo.html")

def pagina(request, redirigir = 0):
    if redirigir == 1:
        return redirect("contacto", nombre = "Sebastian", apellido = "Vega")
    return render(request, "pagina.html")

def contacto(request, nombre = "", apellido = ""):
    html = f"<h2>contacto {nombre} {apellido}</h2>"
    return HttpResponse(layout + html)