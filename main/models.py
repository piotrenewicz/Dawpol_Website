from django.db import models
from django.utils import timezone

# Create your models here.


class Content(models.Model):
    id = models.IntegerField()
    text = models.CharField()


class Glist(models.Model):
    id = models.IntegerField()


class Gelement(models.Model):
    graphic = models.ImageField()
    subtitle = models.CharField()
    id = models.IntegerField()
    manager = models.ForeignKey(Glist, on_delete=models.CASCADE)

