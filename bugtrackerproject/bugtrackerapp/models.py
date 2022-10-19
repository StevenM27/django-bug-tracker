from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Bug(models.Model):
    author = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    priority = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.type