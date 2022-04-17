from pyexpat import model
from django.contrib import admin
from .models import Device,File, Questionnaire, Response, Sensor,Analytics, Application, Sensor_Reading, Sensor_Reading_File,Schema
# Register your models here.

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
	list_display = ['name']

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
	list_display = ['type_of_sensor', 'device']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
	list_display = ['name', 'user']

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
	# readonly_fields = ('file',)
	list_display = ['timestamp', 'file']

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
	readonly_fields = ('timestamp',)
	list_display = ['timestamp', 'sensor']

@admin.register(Sensor_Reading)
class Sensor_ReadingAdmin(admin.ModelAdmin):
	readonly_fields = ('time',)
	list_display = ['time', 'sensor']

@admin.register(Sensor_Reading_File)
class Sensor_ReadingFileAdmin(admin.ModelAdmin):
	# readonly_fields = ('file',)
	list_display = ['time', 'data_file','sensor']

@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
	list_display = ['category','table']

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
	list_display = ['app','title']

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
	list_display = ['questions','user']
