# Generated by Django 2.1.3 on 2019-01-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRP', '0005_auto_20190112_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='praktyki',
            name='czyPlatne',
        ),
        migrations.AlterField(
            model_name='praktyki',
            name='wynagrodzenie',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]