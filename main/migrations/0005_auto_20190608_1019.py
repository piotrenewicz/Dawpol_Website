# Generated by Django 2.1.7 on 2019-06-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190608_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]