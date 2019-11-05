from django.db import models
from django.contrib.auth.models import User
from iotSensors.core.enum import UNIT_CHOICES


class Sensor(models.Model):
    classOID = 0
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oid = models.IntegerField('Oid')
    key = models.UUIDField('Key')
    label = models.CharField('Label', max_length=100)
    description = models.CharField('Description',  max_length=1000)
    class Meta:
        ordering = ['oid']
    

class Stream(models.Model):
    classOID = 0
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    oid = models.IntegerField('Oid')
    key = models.UUIDField('Key')
    label = models.CharField('Label',  max_length=100)
    enable = models.BooleanField('Enable')
    unit = models.CharField(max_length=5, choices = UNIT_CHOICES)
    class Meta:
        ordering = ['oid']


class Data(models.Model):
    classOID = 0
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE)
    oid = models.IntegerField('Oid')
    timestamp = models.DateTimeField("TimeStamp", auto_now=False, auto_now_add=False)
    value = models.FloatField('Value')
    class Meta:
        ordering = ['oid']


    