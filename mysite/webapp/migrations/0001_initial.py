# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('uname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=30)),
                ('rname', models.CharField(max_length=30)),
                ('order_id', models.IntegerField()),
                ('cart_id', models.IntegerField()),
                ('payment', models.CharField(max_length=19)),
                ('status', models.CharField(max_length=20)),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Order Date')),
            ],
        ),
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
                ('overview', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
