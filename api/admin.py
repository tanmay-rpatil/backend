from django.contrib import admin
from .models import Device,Accel,File, Sensor,Analytics, Sensor_Reading
# Register your models here.

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
	list_display = ['type_of_sensor', 'device','schema']

@admin.register(Device)
class SensorAdmin(admin.ModelAdmin):
	list_display = ['name', 'user']


@admin.register(Accel)
class AccelAdmin(admin.ModelAdmin):
	readonly_fields = ('timestamp',)
	list_display = ['timestamp', 'sensor', 'active_ms']

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
	readonly_fields = ('timestamp',)
	list_display = ['timestamp', 'sensor']
## UTC seconds to SQL timestamp
# do = datetime.datetime.strptime(ts_new, '%Y-%m-%d %H:%M:%S.%f')
# a = Accel(device_id=d,active_ms=100,timestamp=do,x_axis='1',y_axis='2',z_axis='3')
# '2019-08-01 18:03:38.000671'