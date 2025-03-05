from django.db import models

class Producto(models.Model):
    producto_nombre = models.TextField(max_length=100)
    producto_precio = models.DecimalField(max_digits=10, decimal_places=2)
    producto_imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    class Meta: 
        permissions = [("puede_administrar_productos", "Puede administrar productos")]
        ordering = ['producto_nombre'] # Ordenamos la lista de productos por el nombre

    def __str__(self):
        return f"{self.id}--{self.producto_nombre}"