# Generated by Django 3.1 on 2020-09-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_auto_20200903_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='rat',
            name='in_rattery',
            field=models.BooleanField(default=False, verbose_name='производитель'),
        ),
    ]
