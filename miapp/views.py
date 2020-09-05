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
    year = 2021
    hasta = range(year, 2051)
    nombre = "Sebastian Vega"
    lenguajes = ["JavaScript", "Python", "Java", "C++"]
    return render(request, "index.html", {
        'title': "Inicio",
        'mi_variable': "años hasta el 2050",
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })


def hola_mundo(request):
    return render(request, "hola_mundo.html")


def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect("contacto", nombre="Sebastian", apellido="Vega")
    return render(request, "pagina.html", {
        'texto': "este es mi texto",
        'lista': ['uno', 'dos', 'tres']
    })


def contacto(request, nombre="", apellido=""):
    html = f"<h2>contacto {nombre} {apellido}</h2>"
    return HttpResponse(layout + html)
