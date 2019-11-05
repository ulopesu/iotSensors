from django.db import models
from django.contrib.auth.models import User, Group
from iotSensors.core.enum import UNIT_CHOICES
import uuid, json

class Units(models.Model):
    units = json.dumps([{'oid': unit[0], 'label': unit[1]} for unit in UNIT_CHOICES])
    

class Sensor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField('Label', max_length=100)
    description = models.CharField('Description',  max_length=1000)


class Stream(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField('Label',  max_length=100)
    enable = models.BooleanField('Enable')
    unit = models.CharField(max_length=5, choices = UNIT_CHOICES)



class Data(models.Model):
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE)
    timestamp = models.DateTimeField("TimeStamp", auto_now=False, auto_now_add=False)
    value = models.FloatField('Value')


