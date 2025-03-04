from django.urls import path
from Compras.views import CargarProductoView

urlpatterns = [
    path('cargar_producto/<int:id>', CargarProductoView.as_view(), name='cargar_producto')
]