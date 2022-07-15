from django.db import models
import mongoengine

from django.utils import timezone
from mongoengine import *
from  Arkham.settings import mingocon
from django.contrib.auth.models import AbstractUser

# 域名存储数据模型
class WebUrls(Document):  # 默认的会在 mongodb 中的数据库创建一个名称为book的表
    urid = mongoengine.IntField(required=True, max_length=125)
    #子域名url
    urls = mongoengine.StringField(required=True)
    #网站状态
    statecode = mongoengine.IntField(default=200)
    state = mongoengine.BooleanField(default=True)
    #添加时间
    time = mongoengine.DateTimeField(default=timezone.now)


