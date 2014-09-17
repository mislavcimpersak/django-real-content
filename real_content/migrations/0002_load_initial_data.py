# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('real_content', '0001_initial'),
    ]

    operations = [
        call_command("loaddata", "my_fixture.json")
    ]