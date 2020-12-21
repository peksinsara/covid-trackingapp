from django.views.generic import ListView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter

from .models import Report
from .serializers import ReportSerializer
from .forms import ReportForm
from django.shortcuts import render

from django.views.generic import TemplateView
from rest_framework import viewsets


class ReportListView(TemplateView):
    model = Report 
    template_name = "reports/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = ReportForm()
        return context


class ReportViewSet(ReadOnlyModelViewSet):
    queryset = Report.objects.all()
    bbox_filter_field = "location"
    filter_backends = (InBBoxFilter, )
    serializer_class = ReportSerializer
