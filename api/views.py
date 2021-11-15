from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import InputSerializer,FileSerializer,AnalyticsSerializer,Sensor_ReadingSerializer, Sensor_Reading_FileSerializer
from .models import Analytics, Device,File, Sensor, Sensor_Reading, Sensor_Reading_File
import datetime

# bulk insert for sesnor stream data in JSON format
@api_view(['POST'])
def insert(request,format=None):
	start = datetime.datetime.now() # for logging insertion time.
	serializer = InputSerializer(data=request.data)
	# if valid, take the sensor ID
	# then insert each entry which is an item in a JSON array 
	if serializer.is_valid():
		sensor = Sensor.objects.get( pk = int(serializer.data['sensor_id']))
		data = (serializer.data['data'])
		to_save = []
		for line in data:
			# print(line['timestamp'])
			timestamp = datetime.datetime.strptime(line['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
			a = Sensor_Reading(sensor=sensor,time=timestamp,data=line)
			to_save.append(a)
	Sensor_Reading.objects.bulk_create(to_save)
	delta = datetime.datetime.now() - start
	with open('/home/tanmay/BITS/sop/backend/testing/delta.txt','a') as log:
		log.write(str(serializer.data['count'])+','+str(delta.total_seconds())+'\n')
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
# for testing sesnor readings as files
class SensorReadingFileView(APIView):
	parser_classes = (MultiPartParser, FormParser)
	def post(self, request):
		file_serializer = Sensor_Reading_FileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# bulk insert for analytics data in JSON format
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