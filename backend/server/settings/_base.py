import sys
from pathlib import Path

import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

EXTERNAL_BASE = BASE_DIR / 'externals'
EXTERNAL_LIBS_PATH = str(EXTERNAL_BASE / 'libs')
EXTERNAL_APPS_PATH = str(EXTERNAL_BASE / 'apps')
BASE_APPS = str(BASE_DIR / 'server' / 'apps')  # apps debería estar fuera

sys.path = ['', EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH, BASE_APPS] + sys.path

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'SECRET_KEY',
    default='django-insecure-(r7cet+an(xt8x&n)tv^)r_+z2#sm1tomtpwfd_(qmllaebh9t',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS',
    default=[
        '127.0.0.1',
        'localhost',
        '0.0.0.0',  # nosec
    ],
)

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

THIRD_APPS = [
    'corsheaders',
    'drf_spectacular',
    'rest_framework',
]

LOCAL_APPS = [
    'users',
    'web',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / 'server' / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB', default='postgres'),
        'USER': env('POSTGRES_USER', default='postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='postgres'),
        'HOST': env('POSTGRES_HOST', default='db'),
        'PORT': 5432,
        'ATOMIC_REQUESTS': True,
    },
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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'public'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'users.CustomUser'

# REST Config
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'SEARCH_PARAM': 'filter[search]',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
}


# API SCHEMA
SPECTACULAR_SETTINGS = {
    'TITLE': 'Keeper Solutions API',
    'DESCRIPTION': 'Servicios para prueba técnica',
    'VERSION': '1.0.0',
    'SCHEMA_PATH_PREFIX': '/api/v1',
}


SESSION_ENGINE = 'django.contrib.sessions.backends.cache'


# Security
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Cors
# CSRF_TRUSTED_ORIGINS = ['http://keeper-solutions.pe']
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOWED_ORIGINS = [  # TODO: Add domain
    'http://localhost:8000',
    'http://localhost:3000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
]

SECURE_REFERRER_POLICY = 'strict-origin'
