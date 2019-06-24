# Generated by Django 2.2.2 on 2019-06-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageelement',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='imagelisting',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='page',
            name='icon',
            field=models.CharField(blank=True, default='question', max_length=100, verbose_name='Ikona'),
        ),
    ]