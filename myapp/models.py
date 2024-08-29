from django.db import models


# Create your models here.

class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(TimeStamp):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
