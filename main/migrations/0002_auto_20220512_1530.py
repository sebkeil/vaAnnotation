# Generated by Django 2.1.15 on 2022-05-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationbox',
            name='rank_value',
            field=models.DecimalField(decimal_places=2, default=0.7958008811168912, max_digits=4),
        ),
    ]