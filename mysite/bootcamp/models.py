from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    age  = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)