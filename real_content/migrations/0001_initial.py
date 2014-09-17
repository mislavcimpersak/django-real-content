# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(unique=True)),
                ('content_category', models.CharField(default=b'p', max_length=1, choices=[(b'p', 'Paragraph'), (b't', 'Title')])),
                ('source', models.URLField(default=b'', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('length', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short', models.CharField(unique=True, max_length=5)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ('short',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='content',
            name='language',
            field=models.ForeignKey(to='real_content.Language'),
            preserve_default=True,
        ),
    ]
