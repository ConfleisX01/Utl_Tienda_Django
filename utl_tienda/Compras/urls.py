from django.urls import path
from Compras.views import ListadoComprasView, ListadoTodasLasComprasView, ProductoSeleccionadoView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listado_compras/<int:id>', login_required(ListadoComprasView.as_view()), name='listado_compras'),
    path('lista_todas_compras/', ListadoTodasLasComprasView.as_view(), name='lista_todas_compras'),
    path('producto_seleccionado/<int:id>', ProductoSeleccionadoView.as_view(), name='producto_seleccionado')
]