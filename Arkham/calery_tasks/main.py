import os
from celery import Celery
from Arkham import settings

# 创建celery实例对象
app = Celery("calery_tasks")

# 把celery和django进行组合，识别和加载django的配置文件,直接复制manage.py中的配置
#导入一下setting不然会报错，from Arkham import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Arkham.settings')

# 通过app对象加载配置
app.config_from_object("calery_tasks.config")

# 加载任务
# 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
# app.autodiscover_tasks(["任务1","任务2"])
app.autodiscover_tasks(["calery_tasks.sms","calery_tasks.sendMail","calery_tasks.saveurls"])

