from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from . import forms
from Productos.models import Producto
from Compras.models import Compra
from django.contrib.auth.models import User
from Compras.forms import CompraCrearForm

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
    
class ProductoSeleccionadoView(FormView):
    template_name = 'compra_productos.html'
    form_class = forms.CompraCrearForm
    success_url = reverse_lazy('lista_productos')
    idProducto = 0

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        id = self.kwargs.get('id')
        producto = get_object_or_404(Producto, id=id)
        kwargs['instance'] = producto
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)