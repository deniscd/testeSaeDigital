from django import forms

from .models import Produtos

class ProdutosForm(forms.ModelForm):

    class Meta:
        model = Produtos
        exclude = ['vlrMedioProduto']
        fields = ('strProduto',)
        labels = {
            'strProduto': 'Novo produto',
        }