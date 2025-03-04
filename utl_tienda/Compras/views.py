from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView
from . import forms
from Productos.models import Producto
from Compras.models import Compra

class CargarProductoView(FormView):
    template_name = 'compra_productos.html'
    form_class = forms.CompraCrearForm
    success_url = reverse_lazy('lista_productos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        id = self.kwargs.get('id')
        producto = get_object_or_404(Producto, id=id)
        kwargs['initial'] = {
            'producto': producto.id,
            'nombre_producto': producto.producto_nombre,
            'precio_producto': producto.producto_precio,
            'imagen_url': producto.producto_imagen.url if producto.producto_imagen else ''
        }
        return kwargs

    def form_valid(self, form):
        producto = get_object_or_404(Producto, id=self.kwargs['id'])
        compra = Compra(
            producto=producto,
            nombre_producto=producto.producto_nombre,
            cantidad=form.cleaned_data['cantidad'],
            precio_producto=producto.producto_precio,
            precio_total=form.cleaned_data['cantidad'] * producto.producto_precio,
        )
        compra.save()
        return super().form_valid(form)