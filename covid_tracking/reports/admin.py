from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Report

# Register your models here.


@admin.register(Report)
class ReportAdmin (OSMGeoAdmin):
    default_lat =  43.818567
    default_lon = 18.327333
    default_zoom = 5