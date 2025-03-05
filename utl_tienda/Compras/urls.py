from django.urls import path
from Compras.views import CargarProductoView, ListadoComprasView, ListadoTodasLasComprasView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('cargar_producto/<int:id>', login_required(CargarProductoView.as_view()), name='cargar_producto'),
    path('listado_compras/<int:id>', login_required(ListadoComprasView.as_view()), name='listado_compras'),
    path('lista_todas_compras/', ListadoTodasLasComprasView.as_view(), name='lista_todas_compras'),
]