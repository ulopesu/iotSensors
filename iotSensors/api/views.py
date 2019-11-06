#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from iotSensors.core.models import Unit, User, Sensor, Stream, Data
from iotSensors.core.serializers import UnitsSerializer, UserSerializer, SensorSerializer, StreamSerializer, DataSerializer
import uuid, json

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
    serializer_class = UnitsSerializer


