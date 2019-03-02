from django.db import models
from django.utils import timezone
import os

# Create your models here.


class Content(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    text = models.CharField(max_length=1000)


class GraphicalItemManager(models.Model):
    id = models.CharField(primary_key=True, max_length=24)

    def __str__(self):
        return self.id


class GraphicalItem(models.Model):
    def directory(self, f_str):
        f_name, f_ext = os.path.splitext(f_str)
        return self.my_manager.id + "/" + self.subtitle + f_ext

    graphic = models.ImageField(upload_to=directory)  # str(manager.id)+"/")
    subtitle = models.CharField(max_length=100)
    my_manager = models.ForeignKey(GraphicalItemManager, on_delete=models.CASCADE)
