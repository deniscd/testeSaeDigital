# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20170524_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('dtCompra', models.DateTimeField(default=django.utils.timezone.now)),
                ('vlrCompra', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('vlrCompra', models.DecimalField(max_digits=5, decimal_places=2)),
                ('vlrMedioProduto', models.DecimalField(max_digits=5, decimal_places=2)),
                ('Qtde', models.IntegerField()),
                ('Compra', models.ForeignKey(to='estoque.Produtos')),
                ('Produto', models.ForeignKey(to='estoque.Compra')),
            ],
        ),
    ]
