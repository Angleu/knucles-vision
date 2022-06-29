from xml.dom.minidom import Document
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
import backend


'indica os caminhos da app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("backend.urls")),
     ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns  += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
