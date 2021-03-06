from django.db import models
# from django.utils import timezone
import os
from django.urls import reverse

# Create your models here.

#
# class TextContent(models.Model):
#     id = models.CharField(primary_key=True, max_length=24)
#     text = models.CharField(max_length=1000)
#
#     def __str__(self):
#         if len(self.text) > 50:
#             short = self.text[:50] + "..."
#         else:
#             short = self.text
#         return self.id + ": " + short
#
#
# class ImageContent(models.Model):
#     def directory(self, f_str):
#         f_name, f_ext = os.path.splitext(f_str)
#         return "ContentImages/" + self.name + f_ext
#
#     id = models.AutoField(primary_key=True, default=0)
#     graphic = models.ImageField(upload_to=directory)
#     name = models.CharField(max_length=100, default="unnamed")
#
#     def __str__(self):
#         return self.name


class Page(models.Model):
    name = models.CharField(max_length=100, default="Unnamed", verbose_name="Nazwa") # this is the name for both a button and a header
    icon = models.CharField(max_length=100, default="question", verbose_name="Ikona", blank=True) #this is the icon for a button on the index page

    url = models.CharField(max_length=100, verbose_name="Adres")
    is_internal = models.BooleanField(verbose_name="Wewnętrzny")
    order = models.IntegerField(default=1)

    def get_url(self):
        if self.is_internal:
            return reverse(self.url)
        else:
            return self.url

    def __str__(self):
        return self.name

    def get_target_app(self):
        if self.is_internal:
            app, view = self.url.split(":")
            return app
        else:
            return None


class ImageListing(models.Model):
    name = models.CharField(max_length=100)
    # this could try to remove the directory on delete

    def directory(self):
        return self.name

    def __str__(self):
        return self.name


class ImageElement(models.Model):
    def directory(self, f_str):
        f_name, f_ext = os.path.splitext(f_str)
        return "./" + self.my_manager.directory() + "/img_" + self.subtitle + f_ext

    graphic = models.ImageField(upload_to=directory)  # str(manager.id)+"/")
    subtitle = models.CharField(max_length=100, blank=True)
    my_manager = models.ForeignKey(ImageListing, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtitle

    # TODO: idea, try to make the file be removed from media when it is removed from the database.
    #       implement the pre_delete signal, and use os and graphic.path to remove the right file
