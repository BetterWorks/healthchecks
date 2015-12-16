# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('next_report_date', models.DateTimeField(null=True, blank=True)),
                ('reports_allowed', models.BooleanField(default=True)),
                ('user', models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
