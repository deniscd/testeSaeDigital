# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_compra_itenscompra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itenscompra',
            name='vlrMedioProduto',
        ),
        migrations.AddField(
            model_name='produtos',
            name='vlrMedioProduto',
            field=models.DecimalField(default=200, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itenscompra',
            name='Compra',
            field=models.ForeignKey(to='estoque.Compra'),
        ),
        migrations.AlterField(
            model_name='itenscompra',
            name='Produto',
            field=models.ForeignKey(to='estoque.Produtos'),
        ),
    ]
