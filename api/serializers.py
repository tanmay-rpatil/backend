from rest_framework import serializers
from .models import File,Analytics,Sensor_Reading,Analytics_File,Sensor_Reading_File

class InputSerializer(serializers.Serializer):
	sensor_id = serializers.IntegerField()
	count = serializers.IntegerField()
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
#for testing the upload as file method
class Sensor_Reading_FileSerializer(serializers.ModelSerializer):
	class Meta():
		model = Sensor_Reading_File
		fields = '__all__'

class Analytics_FileSerializer(serializers.ModelSerializer):
	class Meta():
		model = Analytics_File
		fields = '__all__'
		