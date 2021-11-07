from http.client import ImproperConnectionState
from django.contrib import admin
from django.urls import path
from apimain import views
from  rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apimain/', include('apimain.urls')) ,
]

urlpatterns = format_suffix_patterns(urlpatterns)