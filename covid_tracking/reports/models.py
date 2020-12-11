from django.contrib.gis.db.models import PointField
from django.db import models
from datetime import datetime

class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    first_symptomatic = models.DateField(default=datetime.now)
    location = PointField(null=True, blank=True)