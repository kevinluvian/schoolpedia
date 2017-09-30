# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolcomment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schoolcomment',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.School'),
        ),
        migrations.AddField(
            model_name='schedulerlog',
            name='school',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.School'),
        ),
        migrations.AddField(
            model_name='enquiryanswer',
            name='answered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enquiryanswer',
            name='enquiry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Enquiry'),
        ),
        migrations.AddField(
            model_name='commentreport',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SchoolComment'),
        ),
        migrations.AddField(
            model_name='commentreport',
            name='reported_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.School'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
