from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    addres = models.CharField(max_length=200)
    