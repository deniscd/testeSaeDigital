from django.db import models
from django.utils import timezone

class Produtos(models.Model):
    idProduto = models.ForeignKey('auth.User')
    strProduto = models.TextField()
    dtCriacao = models.DateTimeField(
        default=timezone.now
    )

    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def cadastro_produto(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.strProduto

    def calcula_preco_medio(self):
        return self.strProduto