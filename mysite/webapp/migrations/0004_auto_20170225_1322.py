# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20170224_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('payment', models.CharField(max_length=19)),
                ('status', models.CharField(max_length=20)),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Order Date')),
                ('cart_id', models.ForeignKey(to='webapp.cart')),
                ('rest_id', models.ForeignKey(to='webapp.restaurant')),
                ('user_id', models.ForeignKey(to='webapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu_id',
            field=models.ForeignKey(default=datetime.datetime(2017, 2, 25, 13, 22, 14, 802395, tzinfo=utc), to='webapp.menu'),
            preserve_default=False,
        ),
    ]
