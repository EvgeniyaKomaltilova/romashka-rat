# Generated by Django 3.1 on 2020-09-03 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20200903_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='litter',
            name='public',
            field=models.BooleanField(default=True, verbose_name='опубликовать'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='public',
            field=models.BooleanField(default=True, verbose_name='опубликовать'),
        ),
        migrations.AlterField(
            model_name='rat',
            name='public',
            field=models.BooleanField(default=True, verbose_name='опубликовать'),
        ),
    ]
