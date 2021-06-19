from django.shortcuts import render, redirect
from sitio import views
from .carro import Carro
from django.http import HttpResponse, HttpResponseBadRequest
import requests


# Create your views here.

def agregar_producto(request, producto_id):
   # url = 'http://3.86.154.125:8000'
   # response = requests.get.items('http://3.86.154.125:8000/productos').json()
   # return render(request, {
   #     'response': response,
   #     'url': url

   # })
   # for obj in response:

   #     if obj.cod_prod == producto_id:
    #        producto = array[{obj.cod_prod, obj.descripcion, obj.pr_venta, obj.imagen}]

    carro=Carro(request)
    #producto= Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto_id)
    return redirect("sitio")

def eliminar_producto(request, producto_id):

    carro=Carro(request)
    producto= Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("misitio")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id-producto_id)
    carro.restar_producto(producto=producto)
    return redirect("misitio")

def limpiar_carro(request, producto_id):

    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("misitio")