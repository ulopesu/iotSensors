from rest_framework import serializers
from iotSensors.core.models import Unit, User, Sensor, Stream, Data


class UnitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'description']


class DataSerializer(serializers.HyperlinkedModelSerializer):
    #stream = StreamSerializer()
    #timestamp = serializers.DateTimeField()
    #value = serializers.FloatField()
    class Meta:
        model = Data
        fields = ['stream', 'timestamp', 'value']


class StreamSerializer(serializers.HyperlinkedModelSerializer):
    #sensor = SensorSerializer()
    #key = serializers.IntegerField(read_only=True)
    #label = serializers.CharField(required=True, allow_blank=False, max_length=100)
    #enable = serializers.BooleanField()
    #unit = serializers.ChoiceField(choices= UNIT_CHOICES)
    data = DataSerializer(many=True)
    class Meta:
        model = Stream
        fields = ['oid', 'sensor', 'key', 'label', 'enable', 'unit', 'data']


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    streams = StreamSerializer(many=True)
    #user = UserSerializer()
    #key = serializers.IntegerField(read_only=True)
    #label = serializers.CharField(required=True, allow_blank=False, max_length=100)
    #description = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    class Meta:
        model = Sensor
        fields = ['oid', 'user', 'key', 'label', 'description', 'streams']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    sensors = SensorSerializer(many=True)
    class Meta:
        model = User
        fields = ['oid', 'username', 'email', 'sensors']
        
    