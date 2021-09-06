from django.db import models
from rest_framework.serializers import SerializerMetaclass
from accounts.models import CustomUser

# Create your models here.
def error_dict():
	return {'error':''}

class Device(models.Model):
	name = models.CharField(max_length=100, blank=False,null=False)
	user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=False, blank=False ) # one to many from user to device
	properties  = models.JSONField(blank=False, null=False, default=dict())
	def __str__(self):
		return ( str(self.user) + "'s " + self.name + " :" + str(self.pk) )

class Sensor(models.Model):
	# device and sesor types 
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
	schema  = models.JSONField(blank=False, null=False, default=dict())

	def __str__(self):
		return ( str(self.device) + ": " + self.type_of_sensor + " :" + str(self.pk) )
	
class File(models.Model):
	# sensor Foreign Key Here.
	sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, null=False, blank=False )
	timestamp = models.DateTimeField(blank=False,null=False)
	file_format = models.CharField(max_length=255, blank=True, null=True)
	file = models.FileField(blank=False, null=False)

class Analytics(models.Model):
	# sensor Foreign Key Here.
	sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, null=False, blank=False )
	timestamp = models.DateTimeField(blank=False,null=False)
	data  = models.JSONField(blank=False, null=False, default=dict())

class Analytics_File(models.Model):
	# sensor Foreign Key Here.
	sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, null=False, blank=False )
	timestamp = models.DateTimeField(blank=False,null=False)
	file = models.FileField(blank=False, null=False)

class Sensor_Reading(models.Model):
	# sensor Foreign Key Here.
	sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING, null=False, blank=False )
	timestamp = models.DateTimeField(blank=False,null=False)
	data  = models.JSONField(blank=False, null=False, default=dict())

class Accel(models.Model):
	# give user as  foreign key too?
	sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, null=False, blank=False )
	active_ms = models.BigIntegerField()
	timestamp = models.DateTimeField(blank=False,null=False)
	x_axis = models.CharField( max_length=15, blank=False,null=False)
	y_axis = models.CharField( max_length=15, blank=False,null=False)
	z_axis = models.CharField( max_length=15, blank=False,null=False)