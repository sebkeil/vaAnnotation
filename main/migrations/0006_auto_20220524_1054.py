# Generated by Django 2.1.15 on 2022-05-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220523_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotationbox',
            name='rank_value',
        ),
        migrations.AddField(
            model_name='annotationbox',
            name='rank_idx',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
