import os
from celery.schedules import crontab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '89di$5_t-fo8f*z0!kvbli20gcz^6f)8&2!e1g3o4pbe7v(h^q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'ipa.dataocean.us',
]

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "data_oceanv2",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.01",
        "PORT": "5432",
        'CONN_MAX_AGE': 60 * 10,  # 10 minutes
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# CORS settings
# https://github.com/adamchainz/django-cors-headers

CORS_ORIGIN_WHITELIST = [
    'https://dataocean.us',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'http://localhost:3000',
]

CSRF_TRUSTED_ORIGINS = [
    'dataocean.us',
    'localhost',
    '127.0.0.1',
]

LOCAL_FILE_NAME_KOATUU = ''
LOCAL_FOLDER = ''
FILE_URL_KVED = ''
LOCAL_FILE_NAME_KVED = ''

# celery settings

CELERY_BROKER_URL = 'redis://localhost:6379' # redis://:password@hostname:port/db_number

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

CELERY_BEAT_SCHEDULE = {
    'fill_in_ratu_table':{
        'task': 'location_register.tasks.fill_in_ratu_table',
        'schedule': crontab(hour=14, minute=10, day_of_week=5),
    },
    'fill_in_koatuu_table':{
        'task': 'location_register.tasks.fill_in_koatuu_table',
        'schedule': crontab(hour=1, minute=10, day_of_week=6),
    }
}
