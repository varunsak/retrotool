# Generated by Django 2.0 on 2017-12-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retro', '0003_auto_20171227_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status_item',
            field=models.CharField(max_length=50, verbose_name='Status'),
        ),
    ]
