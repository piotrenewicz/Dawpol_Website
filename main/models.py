from django.db import models
from django.utils import timezone

# Create your models here.


def grab_time():
    time = timezone.now()
    return time


class Comment(models.Model):
    autor = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField(default=grab_time())

    def __str__(self):
        insight = self.autor + ": " + self.content[:20]
        if len(self.content) > 20:
            insight += "..."
        return insight
