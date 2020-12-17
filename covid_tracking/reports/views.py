from django.shortcuts import render
from .models import Report
from django.views.generic import ListView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter
from .serializers import ReportSerializer

# Create your views here.


class ReportListView(ListView):
    model = Report
    template_name = "reports/map.html"


class ReportViewSet(ReadOnlyModelViewSet):
    bbox_filter_field = "location"
    filter_backends = (InBBoxFilter, )
    serializer_class = ReportSerializer
    

