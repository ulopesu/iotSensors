from rest_framework import serializers
from iotSensors.core.models import Units, User, Sensor, Stream, Data
from iotSensors.core.enum import UNIT_CHOICES


class UnitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Units
        fields = ['units']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['oid', 'username', 'email']


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer()
    #key = serializers.IntegerField(read_only=True)
    #label = serializers.CharField(required=True, allow_blank=False, max_length=100)
    #description = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    class Meta:
        model = Sensor
        fields = ['oid', 'user', 'key', 'label', 'description']


class StreamSerializer(serializers.HyperlinkedModelSerializer):
    #sensor = SensorSerializer()
    #key = serializers.IntegerField(read_only=True)
    #label = serializers.CharField(required=True, allow_blank=False, max_length=100)
    #enable = serializers.BooleanField()
    #unit = serializers.ChoiceField(choices= UNIT_CHOICES)
    class Meta:
        model = Stream
        fields = ['oid', 'sensor', 'key', 'label', 'enable','unit']


class DataSerializer(serializers.HyperlinkedModelSerializer):
    #stream = StreamSerializer()
    #timestamp = serializers.DateTimeField()
    #value = serializers.FloatField()
    class Meta:
        model = Data
        fields = ['stream', 'timestamp', 'value']
        
    