# Generated by Django 3.1.1 on 2020-09-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rattery', '0004_remove_rat_old_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='litter',
            options={'verbose_name': 'Литеру', 'verbose_name_plural': 'Литеры'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Локацию', 'verbose_name_plural': 'Локации'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Личность', 'verbose_name_plural': 'Заводчики и владельцы'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterModelOptions(
            name='prefix',
            options={'verbose_name': 'Приставку', 'verbose_name_plural': 'Приставки питомников'},
        ),
        migrations.AlterModelOptions(
            name='questionnaire',
            options={'verbose_name': 'Анкету', 'verbose_name_plural': 'Анкеты'},
        ),
        migrations.AlterModelOptions(
            name='rat',
            options={'verbose_name': 'Крысу', 'verbose_name_plural': 'Крысы'},
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='email',
            field=models.CharField(max_length=64, null=True, verbose_name='контакты'),
        ),
    ]
