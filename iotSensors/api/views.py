#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from iotSensors.core.enum import UNIT_CHOICES
from iotSensors.core.models import Units, Sensor, Stream, Data
from iotSensors.core.serializers import UnitsSerializer, UserSerializer, GroupSerializer, SensorSerializer, StreamSerializer, DataSerializer
import uuid, json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all().order_by('-date_joined')
    serializer_class = SensorSerializer

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all().order_by('-date_joined')
    serializer_class = StreamSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all().order_by('-date_joined')
    serializer_class = DataSerializer

class UnitsViewSet(viewsets.ReadOnlyModelViewSet):
    if len(Units.objects.all()) > 0:
        queryset = Units.objects.all()
        serializer_class = UnitsSerializer
    else:
       unitObj = Units()
       unitObj.save()


"""
def units(request):
    if request.method == 'GET':
        units = [{'oid': unit[0], 'label': unit[1]} for unit in UNIT_CHOICES]
    return HttpResponse(json.dumps(units), content_type='text/json')

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
        sensor = Sensor(user=user, key=key, label=label, description=description)
        sensor.save()
        sensorSerialized = SensorSerializer(sensor)
        return HttpResponse(sensorSerialized.data, content_type='text/json')
    except expression as identifier:
        return HttpResponse({'message': 'Data invalidate!'}, content_type='text/json')

    

"""