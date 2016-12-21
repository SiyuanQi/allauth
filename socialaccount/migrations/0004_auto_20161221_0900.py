# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='provider',
            field=models.CharField(max_length=30, choices=[('weibo', '微博'), ('weixin', '微信')], verbose_name='provider'),
        ),
        migrations.AlterField(
            model_name='socialapp',
            name='provider',
            field=models.CharField(max_length=30, choices=[('weibo', '微博'), ('weixin', '微信')], verbose_name='provider'),
        ),
    ]
