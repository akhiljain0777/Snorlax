# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20170225_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cart_id',
            new_name='order_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
    ]
