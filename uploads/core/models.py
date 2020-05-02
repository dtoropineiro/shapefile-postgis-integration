from __future__ import unicode_literals

from django.db import models


class Shapefile(models.Model):
    description = models.CharField(max_length=255, blank=True)
    shapefile = models.FileField(upload_to='shapefiles/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
