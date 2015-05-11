# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_speedrecord'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pingrecord',
            options={'get_latest_by': 'when_created'},
        ),
        migrations.AlterModelOptions(
            name='speedrecord',
            options={'get_latest_by': 'when_created'},
        ),
    ]
