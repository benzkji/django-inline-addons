# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inline_addons.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                (b'objects', inline_addons.models.EditorManager()),
            ],
        ),
        migrations.CreateModel(
            name='FrontendUser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                (b'objects', inline_addons.models.FrontendUserManager()),
            ],
        ),
    ]
