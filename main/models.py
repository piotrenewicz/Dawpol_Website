from django.db import models
from django.utils import timezone

# Create your models here.


class Content(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=1000)


class Glist(models.Model):
    id = models.IntegerField(primary_key=True)


class Gelement(models.Model):
    graphic = models.ImageField()
    subtitle = models.CharField(max_length=100)
    manager = models.ForeignKey(Glist, on_delete=models.CASCADE)

