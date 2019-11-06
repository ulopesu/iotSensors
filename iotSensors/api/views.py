#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from iotSensors.core.models import Unit, User, Sensor, Stream, Data
from iotSensors.core.serializers import UnitSerializer, UserSerializer, SensorSerializer, StreamSerializer, DataSerializer
import uuid, json


"""DEFINA TODAS AS VIEWS"""

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
                

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class UnitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer



"""RETORNA O JSON DE TODOS OS SENSORES DE UM USUARIO"""
def getSensors(request, id):
    serializer_context = {
        'request': Request(request),
    }

    if request.method == 'GET':
        try:
            user = User.objects.get(oid=id)
        except User.DoesNotExist:
            return HttpResponse({'message': 'User do not exist!'}, content_type='text/json')

        response = []
        sensors = Sensor.objects.filter(user=user)
        for sensor in sensors:
            sensorSerialized = SensorSerializer(sensor, context=serializer_context)
            response.append(sensorSerialized.data)

        return HttpResponse(json.dumps(response), content_type='text/json')
