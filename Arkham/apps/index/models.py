from django.db import models
import mongoengine
import datetime
from mongoengine import *
from  Arkham.settings import mingocon
from django.contrib.auth.models import AbstractUser

# 域名存储数据模型
class WebUrls(Document):  # 默认的会在 mongodb 中的数据库创建一个名称为book的表
    urid = mongoengine.StringField(required=True, max_length=125)
    urls = mongoengine.StringField(required=True)
    state = mongoengine.BooleanField(required=True, max_length=125)
    time = mongoengine.DateTimeField(default=datetime.datetime.now)