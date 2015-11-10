# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100, blank=True)),
                ('AuthorID', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('Country', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('Publishdate', models.CharField(max_length=100, blank=True)),
                ('ISBN', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=100)),
                ('Price', models.FloatField(max_length=100, blank=True)),
                ('Publisher', models.CharField(max_length=200, blank=True)),
                ('AuthorID', models.ForeignKey(to='library.Author')),
            ],
        ),
    ]
