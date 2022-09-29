import os
from datetime import timedelta
from pathlib import Path

from loguru import logger

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", default='django-insecure-nm_h-x*1#se4anh9uf)')

DEBUG = bool(int(os.environ.get("DEBUG", default=1)))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", default="localhost 127.0.0.1").split(" ")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',

    'apps.currencies',
    'apps.api',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', default='django.db.backends.mysql'),
        'NAME': os.environ.get('SQL_NAME', default='db'),
        'USER': os.environ.get('SQL_USER', default='root'),
        'PASSWORD': os.environ.get('SQL_ROOT_PASSWORD', default='12345'),
        'HOST': os.environ.get('SQL_HOST', default='localhost'),
        'PORT': os.environ.get('SQL_PORT', default='3306'),
    }
}


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


LANGUAGE_CODE = 'ru'

TIME_ZONE = os.environ.get('TIME_ZONE', default='Europe/Moscow')

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,


    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}



# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#
#     'formatters': {
#         'main_formatter': {
#             "format": "{asctime} - {levelname} - {module} - {message}",
#             "style": "{"
#         },
#         'json_formatter': {
#             '()': CustomJsonFormatter
#         }
#     },
#
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'main_formatter',
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'formatter': 'json_formatter',
#             'filename': 'log.log'
#         },
#     },
#     'loggers': {
#         'main': {
#             'handlers': ['console', 'file'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#             'propagate': False,
#         },
#     },
# }


logger.add(
    "logs/log.json",
    format="{time} - {level} - {file} - {module} - {message}",
    level=os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
    rotation="10 MB",
    compression="zip",
    serialize=True,
)

logger.add(
    "logs/log.log",
    format="{time} - {level} - {file} - {module} - {message}",
    level=os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
    rotation="10 MB",
    compression="zip",
    serialize=False,
    backtrace=False,
    diagnose=False
)

logger.add(
    "logs/log_full_traceback.log",
    format="{time} - {level} - {file} - {module} - {message}",
    level=os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
    rotation="10 MB",
    compression="zip",
    serialize=False,
    backtrace=True,
    diagnose=True
)