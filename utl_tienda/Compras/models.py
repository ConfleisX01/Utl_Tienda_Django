from django.contrib.auth.models import User
from django.db import models
from Productos.models import Producto  # Importamos el modelo Producto

class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con Producto
    cantidad = models.IntegerField(default=1)  # Cantidad comprada
    comprado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='producto_comprado')  # Usuario que compró

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"Compra de {self.cantidad}"