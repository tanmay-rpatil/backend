from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import InputSerializer,FileSerializer,AnalyticsSerializer,Sensor_ReadingSerializer
from .models import Device,Accel,File
import datetime
# Create your views here.
@api_view(['POST'])
def insert(request,format=None):
	serializer = InputSerializer(data=request.data)
	if serializer.is_valid():
		print(serializer.data['device_id'])
		device = Device.objects.get( pk = int(serializer.data['device_id']))
		data = (serializer.data['content'])
		for line in data.splitlines():
			print(line)
			lst = line.split(",")
			timestamp = datetime.datetime.strptime(lst[0], '%Y-%m-%d %H:%M:%S.%f')
			a = Accel(device_id=device,active_ms=int(lst[1]),timestamp=timestamp,x_axis=lst[2],y_axis=lst[3],z_axis=lst[4])
			a.save()
		# serializer.save()
		# print('yeeehaawww')
	# print(serializer.data['device_id'])
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
	serializer = AnalyticsSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		print('saved')
	# print(serializer.data['device_id'])
	return Response(serializer.data)

@api_view(['POST'])
def insert_readings(request,format=None):
	serializer = Sensor_ReadingSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		print('saved')
	# print(serializer.data['device_id'])
	return Response(serializer.data)