from django.shortcuts import render
from .models import Report
from django.views.generic import ListView

# Create your views here.


class ReportListView(ListView):
    model = Report
    template_name = "reports/map.html"
