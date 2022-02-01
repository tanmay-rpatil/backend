from django.contrib import admin
from .models import Device,File, Sensor,Analytics, Sensor_Reading, Sensor_Reading_File, Type, Schema
# Register your models here.

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
	list_display = ['type_of_sensor', 'device','schema']

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

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ['category','table']

@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
	list_display = ['purpose']
## UTC seconds to SQL timestamp
# do = datetime.datetime.strptime(ts_new, '%Y-%m-%d %H:%M:%S.%f')
# a = Accel(device_id=d,active_ms=100,timestamp=do,x_axis='1',y_axis='2',z_axis='3')
# '2019-08-01 18:03:38.000671'