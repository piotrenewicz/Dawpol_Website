# Generated by Django 2.2.2 on 2019-07-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_hire', '0002_auto_20190625_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]