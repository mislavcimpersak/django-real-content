# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('real_content', '0001_initial'),
    ]

    operations = [
    ]

    # def __init__(self, name, app_label):
    #     super(Migration, self).__init__(name, app_label)
    #     call_command("loaddata", "init_languages.json"),
    #     call_command("loaddata", "init_content.json")
