from django.db import models
from django.utils import timezone
import os

# Create your models here.


class TextContent(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    text = models.CharField(max_length=1000)

    def __str__(self):
        if len(self.text) > 50:
            short = self.text[:50] + "..."
        else:
            short = self.text
        return self.id + ": " + short

class ImageContent(models.Model):
    def directory(self, f_str):
        f_name, f_ext = os.path.splitext(f_str)
        return "ContentImages/" + self.name + f_ext

    graphic = models.ImageField(upload_to=directory)
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.name

class ImageListing(models.Model):
    id = models.CharField(primary_key=True, max_length=24)

    def __str__(self):
        return self.id


class ImageElement(models.Model):
    def directory(self, f_str):
        f_name, f_ext = os.path.splitext(f_str)
        return self.my_manager.id + "/" + self.subtitle + f_ext

    graphic = models.ImageField(upload_to=directory)  # str(manager.id)+"/")
    subtitle = models.CharField(max_length=100)
    my_manager = models.ForeignKey(ImageListing, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtitle
