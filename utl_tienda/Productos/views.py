from django.shortcuts import render, get_object_or_404
from Productos.models import Producto
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from . import forms

# Create your views here.
class ListaProductosView(TemplateView):
    template_name = 'lista_productos.html'

    def get_context_data(self):
        lista = Producto.objects.all()
        return {'lista': lista}
    
class ListadoProductosView(TemplateView):
    template_name = 'administracion_productos.html'

    def get_context_data(self):
        lista = Producto.objects.all()
        return {'lista': lista}

class CrearProductoView(FormView):
    template_name = 'registro_productos.html'
    form_class = forms.ProductoRegistrarForm
    success_url = reverse_lazy('administracion_productos')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class EditarProductoView(FormView):
    template_name = 'editar_productos.html'
    form_class = forms.ProductoEditarForm
    success_url = reverse_lazy('administracion_productos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        id = self.kwargs.get('id')
        producto = get_object_or_404(Producto, id=id)
        kwargs['instance'] = producto
        return kwargs
    
    def form_valid(self, form):
        form.save(self.kwargs.get('id'))
        return super().form_valid(form)
