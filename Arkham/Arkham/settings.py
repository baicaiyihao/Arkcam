"""
Django settings for Acam_v1 project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import sys
from pathlib import Path
import djongo
import mongoengine
import django_redis
from libs import email_config



mingocon = mongoengine.connect('Acam', host='127.0.0.1', port=27017) #数据模型使用时调用连接

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=3bu8gumfxm05otj3@4h(3hd%dlhko$r5+8e-ck#59*dj3788e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users.apps.UsersConfig',
    'django_filters',
    'apps.index.apps.IndexConfig',
    'apps.tools.apps.ToolsConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Arkham.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2'
        ,
        'DIRS': [os.path.join(BASE_DIR, 'html')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'environment':'utils.jinja2_environment.environment',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Arkham.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'djongo',  # 填写上面安装的模块：djongo
        'ENFORCE_SCHEMA': True,  # True：确保模型架构和数据库架构完全相同。引发MigrationError的差异而发生。
        # 'ENFORCE_SCHEMA':False,#False：（默认）隐式创建集合。返回缺失的字段None而不是引发异常。
        'NAME': 'Acam',  # 填写数据库名字
        'CLIENT': {
            'host': '127.0.0.1',  # iporaddress
            'port': 27017  # port（default=27017）
        }
    }
}

#配置redis存储session
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'


#配置静态文件的存放路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#日志的配置
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {
#             #配置日志级别
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             #配置日志输出的文件路径
#             'filename': os.path.join(BASE_DIR, 'logs/logs.log'),
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'myproject.custom': {
#             'handlers': ['console', 'mail_admins'],
#             'level': 'INFO',
#             'filters': ['special']
#         }
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            #配置日志级别
            'level': 'INFO',
            'class': 'logging.FileHandler',
            #配置日志输出的文件路径
            'filename': os.path.join(BASE_DIR, 'logs/logs.log'),
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

#数据模型迁移替换当前的用户模型
AUTH_USER_MODEL = 'users.User'

#设置邮件服务器,这里配置用的是163邮箱进行邮件发送。
#指定邮件发送的后端，user和password放在另外的文件email_config，可以自行配置里了
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#指定邮箱发送的服务器
EMAIL_HOST = 'smtp.163.com'
#smtp默认端口
EMAIL_PORT = '25'
#指定发送的邮箱账号
EMAIL_HOST_USER = email_config.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = email_config.EMAIL_HOST_PASSWORD

# login_required()装饰器，重定向到登录页面
LOGIN_URL = '/login/'

#添加django_filters过滤器
REST_FRAMEWORK = {
    # 全局过滤
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'apps.core.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
