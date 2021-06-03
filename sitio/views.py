from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import requests
# Create your views here.

def sitio(request):
    url = 'http://52.202.109.45:8000'
    response = requests.get('http://52.202.109.45:8000/productos/').json()
    return render(request, "sitio/index.html", {
        'response': response,
        'url': url
    })


def login(request):
        return render(request,"sitio/login.html")

def registro(request):
        return render(request,"sitio/registro.html")