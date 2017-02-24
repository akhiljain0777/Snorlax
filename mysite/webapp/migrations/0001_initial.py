# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
