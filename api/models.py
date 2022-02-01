from django.db import models
from rest_framework.serializers import SerializerMetaclass
from accounts.models import CustomUser, Application
from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.managers import TimescaleManager


def error_dict():
	return {'error':''}
#function to give a directory structure to the model
def generate_filename(instance, filename):
	# path is already relative to MEDIA_ROOT
	return '/'.join(['sensor_readings',str(instance.time.year),str(instance.time.month),str(instance.time.day),str(instance.sensor.pk),filename])

class Schema(models.Model):
	# a table that keeps track of schemas for different JSON fields.
	# try -> make this ENUM? A table of tables?
	purpose = models.CharField(max_length=100, blank=False,null=False, help_text='Used for, e,g "type_notif_name","type_sensor_name"') #table that uses this JSON field
	schema = models.JSONField(blank=False, null=False, default=dict)
	def __str__(self):
		return (self.purpose)
class Type(models.Model):
	# to track categories/tyepes of sensors, notifs, etc
	table = models.CharField(max_length=100, blank=False,null=False) #table that uses this JSON field
	category = models.CharField(max_length=50, blank=False,null=False)
	schema = models.ForeignKey(Schema, on_delete=models.RESTRICT, null=False, blank=False ) # one to many from Schemas to Types
	def __str__(self):
		return ( (self.table) + ':' + (self.category) )

class Device(models.Model):
	name = models.CharField(max_length=100, blank=False,null=False)
	user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=False, blank=False ) # one to many from user to device
	properties  = models.JSONField(blank=False, null=False, default=dict)
	def __str__(self):
		return ( str(self.user) + "'s " + self.name + " :" + str(self.pk) )

class Sensor(models.Model):
	# device and sensor types 
	TYPES = (
		('a', 'accel'),
		('g', 'gyro'),
		('c', 'compass'),
		('ca', 'cam')
	)
	type_of_sensor= models.CharField( 
		max_length=2,
		choices=TYPES,
		blank=False,
		null=False,
		default='a',
		help_text='Device type',
	)
	device = models.ForeignKey(Device, on_delete=models.RESTRICT, null=False, blank=False ) # one to many from user to device
	schema  = models.JSONField(blank=False, null=False, default=dict)

	def __str__(self):
		return ( str(self.device) + ": " + self.type_of_sensor + " :" + str(self.pk) )
	
class Sensor_Users(models.Model): 
	#mapping to store user:sensor:app
	sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, null=False, blank=False )
	user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=False, blank=False )
	app = models.ForeignKey(Application, on_delete=models.RESTRICT, null=False, blank=False )

class Notification(models.Model):
	target_device = models.ForeignKey(Device, on_delete=models.RESTRICT, null=False, blank=False )
	contents = models.JSONField(blank=False, null=False, default=dict)

class File(models.Model):
	# sensor Foreign Key Here.
	sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, null=False, blank=False )
	timestamp = models.DateTimeField(blank=False,null=False)
	file_format = models.CharField(max_length=255, blank=True, null=True)
	file = models.FileField(blank=False, null=False, upload_to='files/%Y/%m/%d/')
	
class Analytics(models.Model):
	# sensor Foreign Key Here.
	sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, null=False, blank=False )
	timestamp = models.DateTimeField(blank=False,null=False)
	data  = models.JSONField(blank=False, null=False, default=dict)

class Analytics_File(models.Model):
	# sensor Foreign Key Here.
	sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, null=False, blank=False )
	timestamp = models.DateTimeField(blank=False,null=False)
	file = models.FileField(blank=False, null=False)

class Sensor_Reading(models.Model):
	# sensor Foreign Key Here.
	sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING, null=False, blank=False )
	time = TimescaleDateTimeField(blank=False,null=False,interval="1 day")
	data  = models.JSONField(blank=False, null=False, default=dict)

# for testing the saving reading as a text file
class Sensor_Reading_File(models.Model):
	# sensor Foreign Key Here.
	sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING, null=False, blank=False )
	time = TimescaleDateTimeField(blank=False,null=False,interval="1 day")
	data_file = models.FileField(blank=False, null=False, upload_to=generate_filename)
	
	# def save(self, *args, **kwargs):
	# 		super(Sensor_Reading_File, self).save() # Call the "real" save() method.