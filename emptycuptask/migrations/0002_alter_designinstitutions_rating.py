# Generated by Django 4.1.13 on 2023-11-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emptycuptask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designinstitutions',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
    ]