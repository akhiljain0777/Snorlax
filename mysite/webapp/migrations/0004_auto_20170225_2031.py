# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20170225_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='rname',
            new_name='uname',
        ),
    ]
