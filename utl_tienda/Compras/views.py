from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from . import forms
from Productos.models import Producto
from Compras.models import Compra
from django.contrib.auth.models import User

class ListadoComprasView(TemplateView):
    template_name = 'historial_compras.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        lista = Compra.objects.filter(comprado_por=usuario)
        context['lista']=lista
        return context
    
class ListadoTodasLasComprasView(TemplateView):
    template_name = 'historial_compras_admin.html'

    def get_context_data(self):
        lista = Compra.objects.all()
        return {'lista': lista}

# El kwargs es parecido al contexto de algunos metodos. En este se usa para obtener la informacion de un objeto entero y llega como parametro parecido a las funciones de POST enviando el objeto esperado
# pero en este caso recibiendolo.
class CargarProductoView(FormView): 
    template_name = 'compra_productos.html'
    form_class = forms.CompraCrearForm
    success_url = reverse_lazy('lista_productos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        id = self.kwargs.get('id')
        producto = get_object_or_404(Producto, id=id)
        kwargs['initial'] = { # Creamos un objeto con los atributos que llegaran del kwargs para despues retornarlo en el contexto y asi poder usar esos atributos para mostrar los detalles del producto
            'producto': producto.id,
            'nombre_producto': producto.producto_nombre,
            'precio_producto': producto.producto_precio,
            'imagen_url': producto.producto_imagen.url if producto.producto_imagen else '' # validacion simple y pa' toda la familia donde retorne la url o una cadenita vacia
        }
        return kwargs

    def form_valid(self, form):
        producto = get_object_or_404(Producto, id=self.kwargs['id']) # obtenemos el producto antes mecionado desde el kwargs con la funcion perrona donde regresa el objeto o nel por el id
        compra = Compra( # Creamos un objeto con los atributos para poder guardarlo dentro de la BADA
            producto=producto,
            nombre_producto=producto.producto_nombre,
            cantidad=form.cleaned_data['cantidad'],
            precio_producto=producto.producto_precio,
            precio_total=form.cleaned_data['cantidad'], #producto.producto_precio, # Multiplicacion simple para mostrar el total que no pidieron en el proyecto pero me da amsiedad no mostrar (No se va a mostrar jeje)
            comprado_por=self.request.user
        )
        compra.save()
        return super().form_valid(form)