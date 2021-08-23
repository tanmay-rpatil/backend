from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import InputSerializer,FileSerializer,AnalyticsSerializer,Sensor_ReadingSerializer
from .models import Analytics, Device,Accel,File, Sensor, Sensor_Reading
import datetime
# Create your views here.
@api_view(['POST'])
def insert(request,format=None):
	serializer = InputSerializer(data=request.data)
	print('serializer')
	if serializer.is_valid():
		print('valid')
		print(serializer.data['sensor_id'])
		sensor = Sensor.objects.get( pk = int(serializer.data['sensor_id']))
		data = (serializer.data['data'])
		for line in data:
			# print(line['timestamp'])
			timestamp = datetime.datetime.strptime(line['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
			a = Sensor_Reading(sensor=sensor,timestamp=timestamp,data=line)
			a.save()
	return Response(serializer.data)

class FileView(APIView):
	parser_classes = (MultiPartParser, FormParser)
	def post(self, request):
		file_serializer = FileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_analytics(request,format=None):
	serializer = InputSerializer(data=request.data)
	print('serializer')
	if serializer.is_valid():
		print('valid')
		print(serializer.data['sensor_id'])
		sensor = Sensor.objects.get( pk = int(serializer.data['sensor_id']))
		data = (serializer.data['data'])
		for line in data:
			# print(line['timestamp'])
			timestamp = datetime.datetime.strptime(line['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
			a = Analytics(sensor=sensor,timestamp=timestamp,data=line['data'])
			a.save()
	return Response(serializer.data)

@api_view(['POST'])
def insert_readings(request,format=None):
	serializer = Sensor_ReadingSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		print('saved')
	# print(serializer.data['device_id'])
	return Response(serializer.data)