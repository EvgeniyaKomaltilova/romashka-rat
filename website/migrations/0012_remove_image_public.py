# Generated by Django 3.1 on 2020-09-02 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20200902_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='public',
        ),
    ]