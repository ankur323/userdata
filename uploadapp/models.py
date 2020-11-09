# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UploadInfo(models.Model):
    filename = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, null=True)
    uploadtime = models.IntegerField()
    sheetnames = models.CharField(max_length=1000)
    # headerlist = models.CharField(max_length=1000, null=True) #check this maxlength, json serialised
    datalist = models.TextField(null=True)  # check this maxlength  , json serialisecs


class UploadSetting(models.Model):
    setting_name = models.CharField(max_length=100)
    userid = models.CharField(max_length=50)
    worksheet = models.CharField(max_length=50, null=True)
    delimeter = models.CharField(max_length=50, null=True)
    default_ownerid = models.CharField(max_length=50,
                                       null=True)  # todo change this to list with foreign key on User Object
    header_row = models.IntegerField(null=True)
    datastart_row = models.IntegerField(null=True)
    upload_data_type = models.CharField(max_length=50, null=True)
    upload_identifier_type = models.CharField(max_length=50, null=True)
    number_format = models.CharField(max_length=50, null=True)
    as_of_date = models.IntegerField(null=True)
    date_format = models.CharField(max_length=50, null=True)
    is_update = models.BooleanField()
    is_replace = models.BooleanField()
    column_to_identifier_map = models.CharField(max_length=50, null=True)
    security_id_map = models.CharField(max_length=50, null=True)
    search_replace_map = models.CharField(max_length=50, null=True)
