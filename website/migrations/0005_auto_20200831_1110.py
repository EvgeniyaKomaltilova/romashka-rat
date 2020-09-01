# Generated by Django 3.1 on 2020-08-31 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_new_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=False, verbose_name='опубликовать')),
                ('name', models.CharField(max_length=127, verbose_name='название')),
                ('picture', models.ImageField(upload_to='images', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='new',
            name='public',
            field=models.BooleanField(default=False, verbose_name='опубликовать'),
        ),
        migrations.AlterField(
            model_name='new',
            name='text',
            field=models.CharField(max_length=255, verbose_name='текст новости'),
        ),
    ]
