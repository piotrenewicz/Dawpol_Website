# Generated by Django 2.2.2 on 2019-06-24 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_auto_20190624_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('imagelisting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.ImageListing')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
            bases=('main.imagelisting',),
        ),
    ]