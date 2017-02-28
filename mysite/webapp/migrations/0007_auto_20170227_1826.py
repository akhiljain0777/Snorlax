# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_cart_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='order_id',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
