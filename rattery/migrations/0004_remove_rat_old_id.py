# Generated by Django 3.1.1 on 2020-09-25 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rattery', '0003_rat_old_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rat',
            name='old_id',
        ),
    ]