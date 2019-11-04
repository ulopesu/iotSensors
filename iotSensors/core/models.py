from django.db import models
from django.contrib.auth.models import User
from iotSensors.core.enum import UNIT_CHOICES


class Sensor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.UUIDField("Key")
    label = models.CharField(verbose_name="Label", max_length=50)
    description = models.CharField(verbose_name="Description",  max_length=50)
    

class Stream(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    key = models.UUIDField("Key")
    label = models.CharField(verbose_name= "Label",  max_length=50)
    enable = models.BooleanField("Enable")
    unit = models.CharField(max_length=3, choices = UNIT_CHOICES)

class Data(models.Model):
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE)
    timestamp = models.DateTimeField("TimeStamp", auto_now=False, auto_now_add=False)
    value = models.FloatField("Value")