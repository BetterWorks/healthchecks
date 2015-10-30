# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150630_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='grace',
            field=models.DurationField(default=datetime.timedelta(0, 3600)),
        ),
    ]
