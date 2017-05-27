from django import forms
from django.forms.models import inlineformset_factory

from .models import Compra, ItensCompra

class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        exclude = ['dtCompra']

class ItensCompraForms(forms.ModelForm):
    class Meta:
        model = ItensCompra
        exclude = ['Compra']