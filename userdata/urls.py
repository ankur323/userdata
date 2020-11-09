from django.conf.urls import url, include
from django.contrib import admin
from uploadapp import views

urlpatterns = [
    url(r'', include('uploadapp.urls', namespace="uploadapp")),
    url(r'^admin/', admin.site.urls),
]
