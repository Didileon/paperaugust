"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)7zntv0g(&im797-gra4#%%4&m@^y)!%2#foh3-g5f5h4d)uhg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_apscheduler',
    #'allauth.socialaccount.providers.yandex',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                #'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'NewsPaper.wsgi.application'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'c:/Users/didil/PycharmProjects/paper/NewsPaper/cache_files'),
        'TIMEOUT': 2,# Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/posts"


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

SITE_URL = 'http://127.0.0.1:8000'

ADMINS = (
    ('admin', '*****@yandex.ru'),
)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = '****'
EMAIL_HOST_PASSWORD = '****'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = 60
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@yandex.ru'


APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"


APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://default:****@redis-14798.c246.us-east-1-4.ec2.cloud.redislabs.com:14798'
CELERY_RESULT_BACKEND = 'redis://default:****@redis-14798.c246.us-east-1-4.ec2.cloud.redislabs.com:14798'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s: %(message)s',
            'datefmt': '%Y.%m.%d %H:%M:%S',
    #'loggers': {
     #   'django': {
            #'handlers': ['news'],
            #'level': 'DEBUG',
        },

       'myformatter': {
           'format': '{levelname} {message} {asctime} {pathname}',
           'datetime': '%m. %d %H:%M:%S',
           'style': '{',
        },

        'myformatter2': {
            'format': '{levelname} {message} {asctime} {pathname} {exc_info}',
            'datetime': '%m. %d %H:%M:%S',
            'style': '{',
        },

        'myformatter3': {
            'format': '{levelname} {message} {asctime} {module}',
            'datetime': '%m. %d %H:%M:%S',
            'style': '{',
        }
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },

        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'news': {
            'level': 'DEBUG',
            #'level': 'INFO',
            #'filters': ['require_debug_true'], #Знаю что надо поставить этот вариант дебурга, но при нем у меня вываливается миллион ошибок. поэтому он закрыт у меня
            #'class': 'logging.FileHandler',
            'class': 'logging.StreamHandler',
            #'filename': 'bug.log',
            #'formatter': 'myformatter',
            'filters': ['require_debug_false'],
            'formatter': 'simple',
        },
        'warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            # 'class': 'logging.FileHandler',
            'class': 'logging.StreamHandler',
            # 'filename': 'bug.log',
            # 'formatter': 'myformatter',
            # 'filters': ['require_debug_false'],
            'formatter': 'myformatter',
        },
        'error': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            #'class': 'logging.StreamHandler',
            'filename': 'errors.log',
            'filters': ['require_debug_true'],
            'formatter': 'myformatter2',
        },
        'critical': {
            'level': 'CRITICAL',
            #'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            #'class': 'logging.StreamHandler',
            'filename': 'errors.log',
            'filters': ['require_debug_true'],
            'formatter': 'myformatter2',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'filters': ['require_debug_false'],
            'formatter': 'myformatter',
        },
        'info': {
            #'level': 'DEBUG',
            'level': 'INFO',
            #'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            #'class': 'logging.StreamHandler',
            'filename': 'general.log',
            'formatter': 'myformatter3',
            'filters': ['require_debug_false'],
            #'formatter': 'simple',
        },
        'security': {
            #'level': 'DEBUG',
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            #'class': 'logging.StreamHandler',
            'filename': 'security.log',
            'formatter': 'myformatter3',
            #'filters': ['require_debug_false'],
            #'formatter': 'simple',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['news', 'error', 'info', 'critical'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.server': {
            'handlers': ['error', 'mail_admins', 'critical'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['error', 'mail_admins', 'critical'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['error', 'critical'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['error', 'critical'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['error', 'security'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}



