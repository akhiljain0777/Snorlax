# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20170225_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='uname',
            field=models.CharField(max_length=15),
        ),
    ]
