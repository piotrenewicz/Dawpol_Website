from django.db import models
from main.models import ImageListing#, ImageContent

# Create your models here.


class Car(ImageListing):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def save(self, *args, **kwargs):   # this is extremely brittle,
        self.name = "[car_hire]: "+self.title
        super(Car, self).save()

    def directory(self):
        return "car_hire/" + self.title

    def __str__(self):
        return self.title