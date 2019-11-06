from django.db import models
import uuid, json

"""DEFINE TODOS OS MODELOS DO PROJETO"""

class Unit(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class User(models.Model):
    oid = models.AutoField(primary_key=True)
    username = models.CharField('UserName', max_length=100)
    email =  models.EmailField(max_length=254)


class Sensor(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="sensors")
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField('Label', max_length=100)
    description = models.CharField('Description',  max_length=1000)


class Stream(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name="streams")
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField('Label',  max_length=100)
    enable = models.BooleanField('Enable')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="+")
    

class Data(models.Model):
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE, related_name="data")
    timestamp = models.DateTimeField("TimeStamp", auto_now=False, auto_now_add=False)
    value = models.FloatField('Value')


