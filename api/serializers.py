from rest_framework import serializers
from .models import File,Analytics,Sensor_Reading

class InputSerializer(serializers.Serializer):
	device_id = serializers.IntegerField()
	content = serializers.CharField(max_length=None, trim_whitespace=False)

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = '__all__'

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Analytics
        fields = '__all__'

class Sensor_ReadingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Sensor_Reading
        fields = '__all__'