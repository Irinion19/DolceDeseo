
import http
from django.http import HttpResponse
import datetime

def bienvenida(request):
    return HttpResponse("hola mari <3")

def bienvenidarojo(request):
    return HttpResponse("<p style='color: red;'>hola mari <3 ;)</p>")

def categoriaedad(request, edad):
    if edad >=18:
        if edad >= 60:
            categoria = "tercera edad"
        else:
            categoria = "adultez"
    else:
        if edad < 10:
            categoria = "infancia"
        else:
            categoria = "adolescencia"
    resultado = "<h1>Categoria de  la edad: %s</h1>" %categoria
    return HttpResponse(resultado)

def obtenermomentoactual(request):
    # respuesta = "<h1> Momento actual: {0}</h1>" .format(datetime.datetime.now())
    respuesta = "<h1> Momento actual: {0}</h1>" .format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)