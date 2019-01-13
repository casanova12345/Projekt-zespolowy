# Generated by Django 2.1.3 on 2019-01-12 17:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRP', '0002_auto_20190112_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praktyki',
            name='czyPlatne',
            field=models.BooleanField(blank=True, default=False, null=True, validators=[django.core.validators.MinValueValidator(0, message='Wartość większa od zera')]),
        ),
        migrations.AlterField(
            model_name='praktyki',
            name='dataRozpoczecia',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='praktyki',
            name='dataZakonczenia',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='praktyki',
            name='miasto',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
