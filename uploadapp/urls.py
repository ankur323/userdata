from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^time/$', views.today_is, name='time'),
    url(r'^$', views.index, name='index'),
    url(r'^get_upload_history$', views.get_upload_history, name=''),
    url(r'^get_upload_data_for_id$', views.get_upload_data_for_id, name=''),
    url(r'^get_user_upload_settings$', views.get_user_upload_settings, name=''),
    url(r'^get_upload_metadata$', views.get_upload_metadata, name=''),
    url(r'^upload_data', views.map_data, name=''),
]