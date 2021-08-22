from rest_framework import serializers
from .models import File,Analytics,Sensor_Reading

class InputSerializer(serializers.Serializer):
	sensor_id = serializers.IntegerField()
	data = serializers.ListField(
        child=serializers.JSONField()
    )

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