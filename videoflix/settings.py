"""
Django settings for videoflix project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qyp^e6tcmkofekajo%l3=)=zmeeko3a4a=#8ciga(-krx)i7*4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # Andere Authentifizierungsklassen nach Bedarf
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # Andere Berechtigungsklassen nach Bedarf
    ],
}




IMPORT_EXPORT_USE_TRANSACTIONS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "users_app",
    "videos_app.apps.VideosConfig",
    'corsheaders',
    "rest_framework.authtoken",
    "debug_toolbar",
    "django_rq",
    'import_export',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
]


def show_toolbar(request):
    # Deaktivieren für Media URLs
    if request.path.startswith('/media/'):
        return False
    # Weitere Bedingungen können hier hinzugefügt werden
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'videoflix.settings.show_toolbar',  # Pfad zur Funktion anpassen
}



# RQ_QUEUES = {
#     'WORKER_CLASS': 'rq_win.WindowsWorker',
#     "default": {
#         'HOST': 'localhost',
#         'PORT': 6379,
#         'DB': 0,
#         "DEFAULT_TIMEOUT": 360,
#         'PASSWORD': 'foobared',
#     }
# }
RQ_QUEUES = {
    'default': {
        'HOST': '127.0.0.1',
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': 360,
       # 'PASSWORD': 'foobared',
    },
}


DJANGO_RQ = {
    'default': {
        'USE_REDIS_CACHE': True,
       # 'WORKER_CLASS': 'rq_win.WindowsWorker',
    }
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
           # "PASSWORD": "foobared",
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "videoflix"
    }
}


INTERNAL_IPS = [
    "127.0.0.1",
]



ROOT_URLCONF = 'videoflix.urls'

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

WSGI_APPLICATION = 'videoflix.wsgi.application'


#CACHE_TTL = 60 * 15
CACHE_TTL = 0


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'videoflixdb',         # Name deiner PostgreSQL-Datenbank
        'USER': 'postgres',       # Datenbank-Benutzer
        'PASSWORD': '',   # Passwort des Benutzers
        'HOST': 'localhost',           # Falls PostgreSQL lokal läuft
        'PORT': '5432',                # Standardport von PostgreSQL
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


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
#MEDIA_URL = 'https://wilhelm-teicke.developerakademie.org/media/'


AUTH_USER_MODEL = 'users_app.CustomUser'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/videoflix/static/staticfiles/'

###
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),  
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static/staticfiles')
# STATICFILES_DIR = [
#     BASE_DIR / "static",
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


ALLOWED_HOSTS = ["localhost", "127.0.0.1", 'wilhelm-teicke.developerakademie.org', 'wilhelm-teicke.developerakademie.net']

CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:5173',
#     'https://wilhelm-teicke.developerakademie.net',
# ]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "OPTIONS",
    "PUT",
    "DELETE",
]
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",  # Falls du mit Auth-Headern arbeitest
    "cache-control",
]

CORS_ALLOW_MEDIA = True



CSRF_EXEMPT_PATHS = ['/logout/']


#FRONTEND_URL = 'http://localhost:5173'
FRONTEND_URL = 'https://wilhelm-teicke.developerakademie.net/videoflix'

DEFAULT_FROM_EMAIL = 'wilhelm.teicke@googlemail.com'

env = environ.Env()

# Laden Sie .env-Datei aus dem Projektverzeichnis, falls vorhanden
environ.Env.read_env()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


APPEND_SLASH = False


