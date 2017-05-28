from django import forms
from django.forms.models import inlineformset_factory

from .models import Compra, ItensCompra

class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        exclude = ['dtCompra']
        labels = {
            'vlrCompra': 'Valor da Compra',
        }

class ItensCompraForms(forms.ModelForm):
    class Meta:
        model = ItensCompra
        exclude = ['Compra', 'id']
        labels = {
            'Produto': 'Novo produto',
            'vlrCompra': 'valor do produto',
            'Qtde': 'Quantidade',
            #'vlrMedioProduto': 'Valor médio',
        }