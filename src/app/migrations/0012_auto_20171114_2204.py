# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20171030_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.IntegerField(blank=True, default=None, null=True, unique=True)),
                ('school_name', models.CharField(max_length=200)),
                ('url_address', models.TextField()),
                ('address', models.TextField()),
                ('postal_code', models.TextField()),
                ('telephone_no', models.TextField()),
                ('telephone_no_2', models.TextField()),
                ('fax_no', models.TextField()),
                ('fax_no_2', models.TextField()),
                ('email_address', models.TextField()),
                ('mrt_desc', models.TextField()),
                ('bus_desc', models.TextField()),
                ('principal_name', models.TextField()),
                ('first_vp_name', models.TextField()),
                ('second_vp_name', models.TextField()),
                ('third_vp_name', models.TextField()),
                ('fourth_vp_name', models.TextField()),
                ('fifth_vp_name', models.TextField()),
                ('visionstatement_desc', models.TextField()),
                ('missionstatement_desc', models.TextField()),
                ('philosophy_culture_ethos', models.TextField()),
                ('dgp_code', models.TextField()),
                ('zone_code', models.TextField()),
                ('cluster_code', models.TextField()),
                ('type_code', models.TextField()),
                ('nature_code', models.TextField()),
                ('session_code', models.TextField()),
                ('sap_ind', models.TextField()),
                ('autonomous_ind', models.TextField()),
                ('gifted_ind', models.TextField()),
                ('ip_ind', models.TextField()),
                ('mainlevel_code', models.TextField()),
                ('mothertongue1_code', models.TextField()),
                ('mothertongue2_code', models.TextField()),
                ('mothertongue3_code', models.TextField()),
                ('special_sdp_offered', models.TextField()),
                ('lat', models.FloatField(blank=True, default=None, null=True)),
                ('lng', models.FloatField(blank=True, default=None, null=True)),
                ('logo_name', models.CharField(default='no-img.jpg', max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MixedSchoolProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('app.school',),
        ),
        migrations.CreateModel(
            name='SecondarySchoolProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('app.school',),
        ),
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='enquiry',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='enquiryanswer',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='reportcomment',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='schoolcomment',
            options={'ordering': ['created_at']},
        ),
    ]