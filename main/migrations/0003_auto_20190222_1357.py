# Generated by Django 2.1.7 on 2019-02-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190221_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.CharField(max_length=24, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='glist',
            name='id',
            field=models.CharField(max_length=24, primary_key=True, serialize=False),
        ),
    ]