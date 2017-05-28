from django.db import models
from django.utils import timezone

class Produtos(models.Model):
    strProduto = models.CharField(max_length=200)
    dtCriacao = models.DateTimeField(
        default=timezone.now
    )
    vlrMedioProduto = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return self.strProduto

    def calcula_preco_medio(self):
        return self.strProduto

class Compra(models.Model):
    dtCompra = models.DateTimeField(
        default=timezone.now
    )
    vlrCompra = models.DecimalField(max_digits=5, decimal_places=2, null=False)


class ItensCompra(models.Model):
    Compra = models.ForeignKey('Compra')
    Produto = models.ForeignKey('Produtos')
    vlrCompra = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    Qtde = models.IntegerField()
