from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from iotSensors.core.enum import UNIT_CHOICES
from iotSensors.core.models import Sensor, Stream, Data
from iotSensors.core.serializers import SensorSerializer, StreamSerializer, DataSerializer
import uuid

def units(request):
    if request.method == 'GET':
        units = [{'oid': unit[0], 'label': unit[1]} for unit in UNIT_CHOICES]
        return units


def userSensors(request, user):
    if request.method == 'GET':
        try:
            user = User.objects.get(user=user)
        except User.DoesNotExist:
            return HttpResponse({'message': 'User do not exist!'}, content_type='text/json')

        sensors = []
        for sensor in Sensor.objcts.all():
            if sensor.user == user:
                sensorSerialized = SensorSerializer(sensor)
                sensor.append(HttpResponse(sensorSerialized.data), content_type='text/json')

        if sensors != []:
            return sensors
        else:
            return HttpResponse({'message': 'This user do not have sensors!'}, content_type='text/json')


def getSensor(request, key):
    if request.method == 'GET': 
        try:
            sensor in Sensor.objects.get(key=key)
            sensorSerialized = SensorSerializer(sensor)
            return HttpResponse(sensorSerialized.data, content_type='text/json')
        except:
            return HttpResponse({'message': 'This sensor-key is invalidate!'}, content_type='text/json')


def getStream(request, key):
    if request.method == 'GET': 
        try:
            stream in Stream.objects.get(key=key)
            streamSerialized = StreamSerializer(stream)
            return HttpResponse(streamSerialized.data, content_type='text/json')
        except:
            return HttpResponse({'message': 'This stream-key is invalidate!'}, content_type='text/json')


def addSensor(request, data):
    try:
        data = JSONParser().parse(request)
        user = request.user
        key = uuid.uuid4()
        label = data.label
        description = data.label
        oid = Sensor.classOID
        sensor = Sensor(classOID = oid+1, user=user, oid=oid, key=key, label=label, description=description)
        sensor.save()
        sensorSerialized = SensorSerializer(sensor)
        return HttpResponse(sensorSerialized.data, content_type='text/json')
    except expression as identifier:
        return HttpResponse({'message': 'Data invalidate!'}, content_type='text/json')

    

