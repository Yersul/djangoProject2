# Generated by Django 3.2.5 on 2021-10-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titles',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
