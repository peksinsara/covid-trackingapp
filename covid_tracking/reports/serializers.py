from rest_framework_gis.serializers import (GeoFeatureModelSerializer)
from .models import Report


#making request to the view and send them to data
class ReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Report
        geo_field = "location"
        fields = ("first_symptomatic", )
        
        