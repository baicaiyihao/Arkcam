from django.db import models
import mongoengine
import datetime
from mongoengine import *
from  Arkham.settings import mingocon
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    用户数据模型
    引用django自带的数据模型并自定义添加字段，
    需要在setting文件中修改配置AUTH_USER_MODEL = 'users.User'
    """
    email_active = models.BooleanField(default=False,verbose_name="邮箱激活状态")

    class Meta:
        db_table = 'Arkham_user'
        verbose_name='用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username