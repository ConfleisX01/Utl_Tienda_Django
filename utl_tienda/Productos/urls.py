from django.urls import path
from Productos.views import ListaProductosView, CrearProductoView, ListadoProductosView, EditarProductoView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('lista_productos/', ListaProductosView.as_view(), name='lista_productos'),
    path('administracion_productos/', ListadoProductosView.as_view(), name='administracion_productos'),
    path('registro_productos/', CrearProductoView.as_view(), name='crear_producto'),
    path('editar_producto/<int:id>', EditarProductoView.as_view(), name='editar_producto'),
]