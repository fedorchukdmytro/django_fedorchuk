"""
Django settings for django_fedorchuk project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from decouple import config

from pathlib import Path

from celery.schedules import crontab
# from celery import Celery
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", 'django-insecure-r8p=+a)6$s1cc5**e#=!2l90z$1r!x*r$3gbgep(!ih&zm%-zf')
# SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']

# CELERY_BROKER_URL = 'pyamqp://guest@localhost//'
CELERY_BROKER_URL = os.getenv('CLOUDAMQP_URL', "")

CELERY_BEAT_SCHEDULE = {
    'beat_log': {
        'task': 'students.tasks.beat_log',
        'schedule': crontab(15, 12),
    },
    'currecy': {
        'task': 'currency.tasks.get_currency_rates',
        'schedule': 300,
    },
    'currecy_mono': {
        'task': 'currency.tasks.get_currency_mono',
        'schedule': 300,
    },
    'currecy_national': {
        'task': 'currency.tasks.get_currency_national',
        'schedule': 300,
    },
    # 'curr_nah': {
    #     'task': 'currency.tasks.cur_nah',
    #     'schedule': crontab(15, 12)
    # }

}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students.apps.StudentsConfig',
    'teachers.apps.TeachersConfig',
    'group.apps.GroupConfig',
    'currency.apps.CurrencyConfig',
    'django_extensions'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'students.middleware.LoggerMiddleware'
]

ROOT_URLCONF = 'django_fedorchuk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_fedorchuk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresgl',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.ukr.net'
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
EMAIL_PORT = 465
EMAIL_HOST_USER = 'fedorchuk.dmytro@ukr.net'
EMAIL_HOST_PASSWORD = 'RXNJtIz2H5GzeIBy'

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)




SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True