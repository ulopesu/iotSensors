from rest_framework import serializers
from django.contrib.auth.models import User
from iotSensors.core.models import Sensor, Stream, Data
from iotSensors.core.enum import UNIT_CHOICES

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=100)
    email = serializers.CharField(required=True, allow_blank=False, max_length=100)
    class Meta:
        model = User

class SensorSerializer(serializers.Serializer):
    user = UserSerializer()
    key = serializers.IntegerField(read_only=True)
    label = serializers.CharField(required=True, allow_blank=False, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    class Meta:
        model = Sensor

class Stream(serializers.Serializer):
    sensor = SensorSerializer()
    key = serializers.IntegerField(read_only=True)
    label = serializers.CharField(required=True, allow_blank=False, max_length=100)
    enable = serializers.BooleanField()
    unit = serializers.ChoiceField(choices= UNIT_CHOICES)
    class Meta:
        Stream

class Data(serializers.Serializer):
    stream = SensorSerializer()
    timestamp = serializers.DateTimeField()
    value = serializers.FloatField()
    class Meta:
        Data
    