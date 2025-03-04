from django import forms
from Compras.models import Compra

class CompraCrearForm(forms.ModelForm):
    imagen_url = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Compra
        fields = ['producto', 'nombre_producto', 'cantidad', 'precio_producto']
        widgets = {
            "producto": forms.HiddenInput(),
            "nombre_producto": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "precio_producto": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
        }