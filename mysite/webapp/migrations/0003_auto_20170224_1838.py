# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20170224_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=datetime.datetime(2017, 2, 24, 18, 38, 10, 520996, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=datetime.datetime(2017, 2, 24, 18, 38, 25, 660124, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(default=datetime.datetime(2017, 2, 24, 18, 38, 35, 241641, tzinfo=utc), max_length=15),
            preserve_default=False,
        ),
    ]
