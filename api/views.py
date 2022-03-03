# REST framework libs used
###
from fnmatch import fnmatch
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status, generics #for CRUD
from .serializers import *
###

#Models and other local py imports
###
from .models import Analytics, Device,File, Sensor, Sensor_Reading, Sensor_Reading_File
from .helper import nix_to_ts
###

#Misc libs
###
import datetime
###

# libs for archiving and unzipping
###
from pathlib import Path 
from zipfile import ZIP_STORED, ZipFile
import os
from io import BytesIO
from django.http import FileResponse,HttpResponse
from django.core.files import File as File_helper
###

#BASE DIRECTORY NAME
BASE_DIR = Path(__file__).resolve().parent.parent

## Insertions
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
	with open( str(BASE_DIR.joinpath('testing/delta.txt')) ,'a') as log:
		log.write(str(serializer.data['count'])+','+str(delta.total_seconds())+'\n')
		return Response(serializer.data)

class FileView(APIView):
	parser_classes = (MultiPartParser, FormParser)
	#create
	def post(self, request):
		file_serializer = FileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileMethods(generics.RetrieveUpdateDestroyAPIView):
	# HTTP methods included:
	# PUT- full update, PATCH- partial update, GET- retrive by id, DELETE- delete 
    queryset = File.objects.all()
    serializer_class = FileSerializer

# for inserting sesnor readings as files
class SensorReadingFileView(APIView):
	parser_classes = (MultiPartParser, FormParser)
	def post(self, request):
		start = datetime.datetime.now() # for logging insertion time.
		new_obj = request.data.copy()
		try:
			new_obj['time'] = nix_to_ts(int(new_obj['time']))
		except:
			return Response("invalid fromat for timestamp", status=status.HTTP_400_BAD_REQUEST)
		print(new_obj)
		file_serializer = Sensor_Reading_FileSerializer(data=new_obj)
		if file_serializer.is_valid():
			file_serializer.save()
			delta = datetime.datetime.now() - start
			with open( str(BASE_DIR.joinpath('testing/delta-file.txt')),'a') as log:
				log.write(str(file_serializer.data['sensor'])+' : '+str(delta.total_seconds())+'\n')
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# for extracting sensor files from zip:
class SensorReadingUnzip(APIView):
	parser_classes = (MultiPartParser, FormParser, FileUploadParser)
	def post(self, request):
		# start = datetime.datetime.now() # for logging insertion time.
		serializer = Sensor_Reading_ZipSerializer(data=request.data)
		# print(serializer)
		if serializer.is_valid():
			##IMP Check for integrity before extraction??
			zip_file = request.FILES['zip_file']
			# timestamps = serializer.data['timestamps'] # a list of timestamps?
			sensor_id = serializer.data['sensor_id']
			##IMP Check for valid sensor id
			sensor_used = Sensor.objects.get(pk=sensor_id)
			# print(timestamps[0])
			iter = 0
			with ZipFile(zip_file, 'r') as opened:
				files = opened.infolist()
				for readings_file in files:
					raw_data = BytesIO(opened.read(readings_file))
					fname = readings_file.filename
					file_obj = File_helper(raw_data, name=fname)
					ts = int(fname[fname.find('_')+1:fname.find('.')])
					print(ts)
					timestamp = datetime.datetime.strptime(nix_to_ts(ts), '%Y-%m-%d %H:%M:%S.%f')
					to_save = Sensor_Reading_File(sensor=sensor_used, time=timestamp, data_file=file_obj)
					to_save.save()
					iter+=1
					# print(readings_file.filename,timestamps[iter])

			return Response({"saved count":iter, "sensor":str(sensor_used), "sensor_id": sensor_id}, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

# old version -> insert single sensor reading
@api_view(['POST'])
def insert_readings(request,format=None):
	serializer = Sensor_ReadingSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		print('saved')
	# print(serializer.data['device_id'])
	return Response(serializer.data)



## Querying
# return a zip of all files in range
class ReadingQueryView(APIView):
	def post(self, request):
		serializer = Sensor_Reading_Query_FileSerializer(data=request.data)
		# print(serializer)    
		if serializer.is_valid():
			# query the db to get a list of files
			start_datetime = (serializer.data['start'])
			end_datetime = (serializer.data['end'])
			sensor = (serializer.data['sensor_id'])
			files_list_qs = Sensor_Reading_File.objects.filter(time__range=(start_datetime,end_datetime),sensor=sensor)
			print(start_datetime,end_datetime,sensor)
			# archive the file list 
			# Folder name in ZIP archive which contains the files
			# E.g [thearchive.zip]/somefiles/file2.txt
			# zip_subdir = str(BASE_DIR.joinpath('queries/query.zip'))
			zip_subdir = 'query'
			zip_filename = "%s.zip" % zip_subdir
			# Open BytesIO to grab in-memory ZIP contents
			s = BytesIO()
			# The zip compressor
			zf = ZipFile(s, "w")
			for files in files_list_qs:
				# Calculate path for file in zip
				fdir, fname = os.path.split((files.data_file.path))
				zip_path = os.path.join(zip_subdir, fname)
				# Add file, at correct path
				zf.write(str(files.data_file.path), zip_path)
			# Must close zip for all contents to be written
			zf.close()
			 # Grab ZIP file from in-memory, make response with correct MIME-type
			resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
			# ..and correct content-disposition
			resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
			print(resp)    
			return resp
			##credits: @dbr https://stackoverflow.com/questions/67454/serving-dynamically-generated-zip-archives-in-django
			# return Response( status=status.HTTP_201_CREATED) #change response code
		else:
			return Response( status=status.HTTP_400_BAD_REQUEST)

