from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from uploads.core.views import *


urlpatterns = [
    path('', home, name='home'),
    path('uploads/form/', model_form_upload, name='model_form_upload'),
    path('uploads/list/', list_shapefiles, name='list_shapefiles'),
    path('uploads/list/done/<int:id>', run_script, name='run_script')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
