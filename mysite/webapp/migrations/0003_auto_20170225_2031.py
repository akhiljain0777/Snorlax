# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20170225_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='uname',
            new_name='rname',
        ),
    ]
