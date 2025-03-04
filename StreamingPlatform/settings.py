import logging
from pathlib import Path
import os
from datetime import timedelta
import environ
import psycopg2
from celery.schedules import crontab

# region ---------------------- BASE CONFIGURATION -----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])
# endregion --------------------------------------------------------------------------------

# region ---------------------- CORS HEADERS -----------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CSRF_COOKIE_SECURE = False
# endregion ---------------------------------------------------------------------------------


INSTALLED_APPS = [
    # region ----------------- BASE DJANGO PACKAGES -----------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # endregion ------------------------------------------------

    # region ----------------- REST FRAMEWORK MODULES -----------
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    # endregion -------------------------------------------------

    # region ----------------- APPLICATIONS --------------------
    'api',  # приложения где будут все апи
    'common',  # приложения, где будут функции которые чаще используются для DRY
    'users',
    # endregion --------------------------------------------------

    'drf_spectacular',  # всегда указывать после всех других созданных приложений проекта или же в конце
]

# region -------------------- MD & TEMP & WSGI & VALIDATORS & URLCONF -----------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'StreamingPlatform.urls'

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

WSGI_APPLICATION = 'StreamingPlatform.wsgi.application'

# endregion ------------------------------------------------------------------------

# region ---------------------- DATABASE ----------------------------------------------------
logger = logging.getLogger(__name__)

def is_postgres_available():
    """Проверяет доступность PostgreSQL"""
    try:
        with psycopg2.connect(
            dbname=env.str('DB_NAME', 'postgre'),
            user=env.str('DB_USERNAME', 'postgre'),
            password=env.str('DB_PASSWORD', 'postgre'),
            host=env.str('DB_HOST', 'localhost'),
            port=env.int('DB_PORT', 5432),
        ) as conn:
            return True
    except psycopg2.OperationalError as e:
        logger.warning(f"PostgreSQL недоступен: {e}")
        return False

# Выбор БД
if is_postgres_available():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env.str('DB_NAME', 'postgre'),
            'USER': env.str('DB_USERNAME', 'postgre'),
            'PASSWORD': env.str('DB_PASSWORD', 'postgre'),
            'HOST': env.str('DB_HOST', 'localhost'),
            'PORT': env.int('DB_PORT', 5432),
        },
    }
else:
    logger.warning("Переключение на SQLite, так как PostgreSQL недоступен.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3'
        }
    }

# endregion ---------------------------------------------------------------------------------

# region ---------------------- REST FRAMEWORK ----------------------------------------------
REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ),

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
# endregion -------------------------------------------------------------------------

# region ---------------------- SIMPLE JWT & DJOSER -----------------------------------------
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {},
}
# endregion -------------------------------------------------------------------------=========

# region ---------------------- SPECTACULAR SETTINGS --------------------------------------
SPECTACULAR_SETTINGS = {
    'TITLE': '',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_PERMISSIONS': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'SERVE_AUTHENTICATION': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        "displayOperationId": True,
        "syntaxHighlight.active": True,
        "syntaxHighlight.theme": "arta",
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "filter": True,
        "requestSnippetsEnabled": True,
    },

    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATIONS': False,

    'ENABLE_DJANGO_DEPLOY_CHECK': False,
    'DISABLE_ERRORS_AND_WARNINGS': True,
}
# endregion -------------------------------------------------------------------

# region ---------------------- LOCALIZATION ------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
# endregion ----------------------------------------------------------------------------------

# region ---------------------- SMTP -----------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# Настройка почтового сервера по SMTP-протоколу
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# endregion ------------------------------------------------------------------------------------

AUTH_USER_MODEL = 'users.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# AUTHENTICATION_BACKENDS = ('users.backends.AuthBackend',)
GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')
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


# region ---------------------- CELERY ------------------------------------------------

# Использование брокера сообщений для Celery (Redis)
CELERY_BROKER_URL = os.getenv("REDDIS_URL", "redis://localhost:6379/0")

# Использование Redis для хранения результатов выполнения задач
CELERY_RESULT_BACKEND = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Отслеживание состояния выполнения задач (по умолчанию выключено)
CELERY_TASK_TRACK_STARTED = os.getenv("CELERY_TASK_TRACK_STARTED", "False").lower() in ("true", "1", "yes")

# Максимальное время выполнения задачи (30 минут)
CELERY_TASK_TIME_LIMIT = 30 * 60

# Поддерживаемые форматы сериализации данных
CELERY_ACCEPT_CONTENT = [os.getenv("ACCEPT_CONTENT", "json")]
CELERY_RESULT_SERIALIZER = os.getenv("RESULT_SERIALIZER", "json")
CELERY_TASK_SERIALIZER = os.getenv("TASK_SERIALIZER", "json")

# Указание временной зоны сервера для корректного выполнения задач по расписанию
CELERY_TIMEZONE = os.getenv("TIMEZONE",)

# Настройка периодических задач Celery Beat
CELERY_BEAT_SCHEDULE = {
    "backup_database": {
        # Путь к задаче, указанной в model_tk.py
        "task": "common.tasks.db_backup_task",
        # Резервное копирование БД каждый день в полночь
        "schedule": crontab(hour=0, minute=0),
    },
}

# endregion ---------------------------------------------------------------------------------

# region ------------------------- STATIC AND MEDIA ----------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_TEST_ROOT = os.path.join(BASE_DIR, 'media/test/')
# endregion ---------------------------------------------------------------------------------

