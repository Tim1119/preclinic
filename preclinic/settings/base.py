from pathlib import Path
import os
import logging.config
import logging
from django.utils.log import DEFAULT_LOGGING
import environ
from django.contrib import messages
env = environ.Env(DEBUG=(bool, False))

#---------------------------------------------------------- READING ENV FILES ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(BASE_DIR / ".env")


#----------------------------------------------  PRODUCTION VARIABLES ---------------------------------------------------------------
SECRET_KEY=env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(" ")


# Application definition

# ---------------------------------------------- APPLICATIONS  DEFINITION   -----------------------------------------------------------

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.accounts',
    'apps.appointments',
    'apps.profiles',
    'apps.utilities',
    'apps.ailment',
    'apps.course',
    'apps.departments',
    'apps.institution',
]

# ----------------------- MESSAGE TAG ------------------------
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

THIRD_PARTY_APPS = [
    'imagekit',
    'django_cleanup.apps.CleanupConfig',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

ROOT_URLCONF = 'preclinic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'preclinic.wsgi.application'



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }




DATABASES = {
    'default': {
        'ENGINE':env('DATABASE_ENGINE'),
        'NAME':env('DATABASE_NAME'),
        'USER':env('DATABASE_USER'),
        'PASSWORD':env('DATABASE_PASSWORD'),
        'HOST':env('DATABASE_HOST'),
        'PORT':env('DATABASE_PORT'),
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# -------------------------------------------------------------INTERNALIZATION ---------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------- STATIC AND  MEDIA PATHS --------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"


# --------------------------------------------------------------USER MODEL ---------------------------------------------------------
AUTH_USER_MODEL = 'accounts.User'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# --------------------------------------------------------------LOGGERS --------------------------------------------------------
logger = logging.getLogger(__name__)

LOG_LEVEL = "INFO"

if ('DEBUG') == 'True':
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "console": {
                    "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                },
                "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
                "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "console",
                },
                "file": {
                    "level": "INFO",
                    "class": "logging.FileHandler",
                    "formatter": "file",
                    "filename": "logs/preclinic.log",
                },
                "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
            },
            "loggers": {
                "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
                "apps": {"level": "INFO", "handlers": ["console"], "propagate": False},
                "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
            },
        }
    )




WSGI_APPLICATION = 'preclinic.wsgi.app'