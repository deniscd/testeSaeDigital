# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='idProduto',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='produtos',
            name='strProduto',
            field=models.CharField(max_length=200),
        ),
    ]
