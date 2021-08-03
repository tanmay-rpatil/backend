from rest_framework import serializers
from .models import File,Analytics

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