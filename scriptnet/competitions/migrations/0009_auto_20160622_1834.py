# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 15:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0008_auto_20160621_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.FileField(null=True, upload_to='uploads/avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortbio', models.TextField(default='')),
                ('avatar', models.FileField(null=True, upload_to='uploads/avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Organizer',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='participant',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='organizer',
        ),
        migrations.AddField(
            model_name='competition',
            name='organizer',
            field=models.ManyToManyField(to='competitions.Individual'),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='members',
            field=models.ManyToManyField(to='competitions.Individual'),
        ),
        migrations.AddField(
            model_name='submission',
            name='submitter',
            field=models.ManyToManyField(to='competitions.Individual'),
        ),
    ]
