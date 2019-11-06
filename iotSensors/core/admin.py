from django.contrib import admin
from iotSensors.core.models import Sensor, Stream, Data, Unit

class UnitAdmin(admin.ModelAdmin):
    pass
admin.site.register(Unit, UnitAdmin)

class SensorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sensor, SensorAdmin)

class StreamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Stream, StreamAdmin)

class DataAdmin(admin.ModelAdmin):
    pass
admin.site.register(Data, DataAdmin)