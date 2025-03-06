from django import forms
from Compras.models import Compra
from Productos.models import Producto

class CompraCrearForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cantidad']
        widgets = {
            "cantidad": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        }

    def save(self, id, user):
        producto = Producto.objects.filter(id=id).first()
        compra = Compra(
            producto=producto, 
            cantidad=self.cleaned_data['cantidad'],
            comprado_por = user
        )
        compra.save()
        