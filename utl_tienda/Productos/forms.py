from django import forms
from Productos.models import Producto

class ProductoRegistrarForm(forms.ModelForm): # Registrar productos
    class Meta:
        model = Producto
        fields = ['producto_nombre', 'producto_precio', 'producto_imagen']
        widgets = {
            "producto_nombre": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
            "producto_precio": forms.TextInput(attrs={"class": "form-control", "type": "number"}),
            "producto_imagen": forms.ClearableFileInput(attrs={"class": "form-control", "type": "file"}),
        }

class ProductoEditarForm(forms.ModelForm): # Editar productos
    class Meta:
        model = Producto
        fields = ['producto_nombre', 'producto_precio', 'producto_imagen']
        widgets = {
            "producto_nombre": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
            "producto_precio": forms.TextInput(attrs={"class": "form-control", "type": "number"}),
            "producto_imagen": forms.ClearableFileInput(attrs={"class": "form-control", "type": "file"}),
        }

    def save(self, id):
        item = Producto.objects.filter(id=id).first()
        item.producto_nombre = self.cleaned_data['producto_nombre']
        item.producto_precio = self.cleaned_data['producto_precio']
        item.producto_imagen = self.cleaned_data['producto_imagen']
        item.save()